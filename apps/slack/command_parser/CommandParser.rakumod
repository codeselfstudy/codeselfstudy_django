unit module CommandParser;

use JSON::Tiny;

# Parses the slash-commands that come from Slack.
grammar Command is export {
    # there are two types of commands
    rule TOP { <source-command> | <url-command> }

    # `languages` is not greedy, because a language cannot be a `difficulty`.
    rule source-command { <source> <languages>* <difficulty> <languages>? }
    token url-command { <url> }

    token url { <protocol>'://'<address> }

    # number token
    token num { \d }

    # sources
    token source { <codewars> | <leetcode> | <projecteuler> | <codeselfstudy> }

    token codewars { 'codewars' | 'cw' | 'code wars' }
    token leetcode { 'leetcode' | 'lc' | 'leet code' }
    token projecteuler { 'projecteuler' | 'pe' | 'project euler' }
    token codeselfstudy { 'codeselfstudy' | 'css' | 'code self study' }

    # difficulty tokens
    token difficulty { <word-rating> | <level> | <kyu> }
    token word-rating { <novice> | <easy> | <medium> | <hard> }
    # a kyu can be something like '5kyu', '5 kyu', 'kyu5', or 'kyu 5'
    token kyu { <num>\h*kyu | kyu\h*<num> }
    # a level can be something like 'level 3', 'level3', or just '3'
    token level { [ level\h*<num> | <num> ] }

    token novice { 'novice' | 'beginner' | 'simple' | 'simplest' }
    token easy { 'easy' | 'basic' }
    token medium { 'medium' | 'intermediate' }
    token hard { 'hard' | 'advanced' | 'difficult' | 'impossible' | 'crazy' }

    # To avoid duplication, a language is any word not included in the above.
    # The receiver of the JSON will decide whether that language exists or not.
    token language { <!difficulty> \w+ }
    rule languages { <language> + }

    # url tokens
    token protocol { 'http' | 'https' }
    rule address { [ <subdomain> '.' ]? <domain> '.' <tld> '/' <path> }
    rule subdomain { <segment> }
    rule domain { <segment> }
    rule tld { <segment> }
    token segment { <[ a..z A..Z 0..9 - ]>+ }
    rule path { .+ }
}

class Command-actions {
    # Converts a kyu level (1-8) to a codeselfstudy level (0-4)
    method kyu-to-difficulty ($kyu) {
        given $kyu {
            when 8 { 1 }
            when 6..7 { 2 }
            when 4..5 { 3 }
            when 1..3 { 4 }
            default { 0 }
        }
    }
}

# lvl    leet cwar eulr
# 1      N    8    1-3
# 2      E    6-7  4-8
# 3      M    4-5  9-17
# 4      H    1-3  18-20
# Converts a kyu level (1-8) to a codeselfstudy level (0-4)
sub kyu-to-difficulty ($kyu) {
    given $kyu<num>.Int {
        when 8 { 1 }
        when 6..7 { 2 }
        when 4..5 { 3 }
        when 1..3 { 4 }
        default { 0 }
    }
}

sub word-rating-to-difficulty ($word-rating) {
    given $word-rating {
        when $word-rating<novice> { 1 }
        when $word-rating<easy> { 2 }
        when $word-rating<medium> { 3 }
        when $word-rating<hard> { 4 }
        default { 0 }
    }
}

sub difficulty-to-css-rating ($difficulty) {
    given $difficulty {
        when $difficulty<level> { $<difficulty><level><num>.Int }
        when $difficulty<kyu> { kyu-to-difficulty($difficulty<kyu>) }
        when $difficulty<word-rating> { word-rating-to-difficulty($difficulty) }
    }
}

sub get-source ($m) {
    given $m {
        when $m<source><leetcode> { 'leetcode' }
        when $m<source><codewars> { 'codewars' }
        when $m<source><projecteuler> { 'projecteuler' }
        when $m<source><codeselfstudy> { 'codeselfstudy' }
        default { 'any' }
    }
}

sub get-difficulty ($m) {
    given $m {
        when $m<difficulty><kyu> { kyu-to-difficulty($m<difficulty><kyu>) }
        when $m<difficulty><word-rating> {word-rating-to-difficulty($m<difficulty><word-rating>) }
        when $m<difficulty><level> { $m<difficulty><level><num> }
        default { 0 }
    }
}

sub get-languages ($m) {
    # There is probably a better way to do this.
    $m<languages>.Str.split(' ').Array.grep(none '');
}

sub process-source-command (Match $source) {
    my %query = (
        source => get-source($source),
        difficulty => get-difficulty($source).Int,
        languages => get-languages($source)
    );

    %query;
}

sub process-url-command (Match $url) {
    # TODO: this should use the URL parsing rules from the Command grammar, if
    # that's possible. In the meantime, this at least ensures that the URL
    # doesn't have multiple args.
    my $split-url = $url.split(/\s+/);
    my $cleaned-url;
    if $split-url.elems() > 1 {
        $cleaned-url = $split-url[0];
    } else {
        $cleaned-url = $url;
    }
    my %query = (
        url => $cleaned-url.Str
    );

    %query;
}

sub dispatch-command (Str $s) {
    my $m = Command.parse($s);
    # If the grammar doesn't match, it seems to return an (Any). So, if we
    # don't get a (Command) back, it shouldn't return anything to the caller
    # (until someone figures out a better way to do this).
    if !($m ~~ Command) {
        return Nil;
    }
    given $m {
        when $m<source-command> { process-source-command($m<source-command>) }
        when $m<url-command> { process-url-command($m<url-command><url>) }
        default { Nil }
    }
}

sub send-puzzle-json ($h) { to-json($h); }
sub send-error-json () { to-json({status => 'error', reason => 'could not parse command'}); }

# entrypoint
sub process-command(Str $s) is export {
    my $result = dispatch-command($s);
    if $result {
        send-puzzle-json($result);
    } else {
        send-error-json();
    }
}

# I tried a MAIN sub here, but that didn't produce output. Maybe the module
# needs to be loaded in a script?
my $inp = @*ARGS;
my $cmd = $inp.join(' ');
my $result = process-command($cmd);
say $result;
