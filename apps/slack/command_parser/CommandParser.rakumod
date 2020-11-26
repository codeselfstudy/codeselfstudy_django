unit module CommandParser;

use JSON::Tiny;

# Parses the slash-commands that come from Slack.
grammar Command {
    # there are two types of commands
    rule TOP { <source-command> | <url-command> }

    # token source-command { [ <source> <language>*? <difficulty> <language>*? ] }
    token source-command { <source> <difficulty> }  # TODO: add languages back
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

    # TODO: language tokens
    token language {
        'raku'
    }

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
        say "kyu is ", $kyu.WHAT;
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
    say "kyu is ", $kyu<num>.Int;
    given $kyu<num>.Int {
        when 8 { 1 }
        when 6..7 { 2 }
        when 4..5 { 3 }
        when 1..3 { 4 }
        default { 0 }
    }
}

sub word-rating-to-difficulty ($word-rating) {
    say "HERE: ", $word-rating;
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

# my $difficulty-level = 0;
# given $m {
#     when $m<difficulty><level> { $difficulty-level = $m<difficulty><level><num> }
#     when $m<difficulty><kyu> { $difficulty-level = $m<difficulty><kyu><num> }
# }
# say "difficulty level is $difficulty-level";

say '=======';

# TODO change $m to $source
sub get-source (Match $m) {
    given $m {
        when $m<source><leetcode> { 'leetcode' }
        when $m<source><codewars> { 'codewars' }
        when $m<source><projecteuler> { 'projecteuler' }
        when $m<source><codeselfstudy> { 'codeselfstudy' }
        default { 'any' }
    }
}

# TODO change $m to $difficulty
sub get-difficulty (Match $m) {
    given $m {
        when $m<difficulty><kyu> { kyu-to-difficulty($m<difficulty><kyu>) }
        when $m<difficulty><word-rating> {word-rating-to-difficulty($m<difficulty><word-rating>) }
        when $m<difficulty><level> { $m<difficulty><level><num> }
        default { 0 }
    }
}

sub process-source-command (Match $m) {
    my %query = (
        source => get-source($m),
        difficulty => get-difficulty($m)
    );

    %query;
}

sub process-url-command (Match $m) {
    say 'process-url-command';
    my %query = (
        url => $m.Str
    );

    %query;
}

sub dispatch-command (Str $s) {
    say 'dispatch-command';
    my $m = Command.parse($s);
    given $m {
        when $m<source-command> { process-source-command($m<source-command><source>) }
        when $m<url-command> { process-url-command($m<url-command><url>) }
    }
}

# entrypoint
sub process-command(Str $s) is export {
    say "process-command";
    my $result = dispatch-command($s);
    say "result:";
    say $result;
    to-json($result);
}

# say %query;
# say to-json %query;

# my $cmd = @*ARGS;
# say "cmd is $cmd";

# my $m = Command.parse($cmd);
# say $m<url>;

# say '+++++++ RETURN +++++++';
# my $result = process-command($m);
# say $result;

