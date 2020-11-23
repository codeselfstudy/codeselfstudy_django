use JSON::Tiny;
# Usage:
#     say from-json('{ "a": 42 }').perl;
#     say to-json { a => [1, 2, 'b'] };

grammar Command {
    rule TOP { <source> <difficulty> }

    token source { <codewars> | <leetcode> | <projecteuler> }
    token difficulty { <word-rating> | <level> | <kyu> }

    token codewars { codewars | cw | 'code wars' }
    token leetcode { leetcode | lc | 'leet code' }
    token projecteuler { projecteuler | pe | 'project euler' }

    token num { \d }

    token word-rating { novice | easy | medium | hard }
    token kyu { <num>\h*kyu }
    token level { [ level\h*<num> | \d ] }
}

# say Command.parse('cw 1'); say "=======";
# say Command.parse('codewars 8 kyu'); say "=======";
# say Command.parse('lc medium'); say "=======";
# say Command.parse('pe level 3'); say "=======";
# say Command.parse('pe level3'); say "=======";
# say Command.parse('project euler 1'); say "=======";

# lvl    leet cwar eulr
# 1      N    8    1-3
# 2      E    6-7  4-8
# 3      M    4-5  9-17
# 4      H    1-3  18-20
# Converts a kyu level (1-8) to a codeselfstudy level (0-4)
sub kyu-to-difficulty (Int $kyu) {
    given $kyu {
        when 8 { 1 }
        when 6..7 { 2 }
        when 4..5 { 3 }
        when 1..3 { 4 }
        default { 0 }
    }
}

sub word-rating-to-difficulty ($word-rating) {
    given $word-rating {
        'novice' { 1 }
        'easy' { 2 }
        'medium' { 3 }
        'hard' { 4 }
        default { 0 }
    }
}

sub difficulty-to-css-rating ($difficulty) {
    given $difficulty {
        $difficulty<level> { $<difficulty<level><num> }
        $difficulty<kyu> { kyu-to-difficulty($difficulty<kyu>) }
        $difficulty<word-rating> { word-rating-to-difficulty($difficulty<word-rating>) }
    }
}

say "#######";
my $m = Command.parse('lc level 3');
say $m<difficulty><level><num>;

my $difficulty-level = 0;
given $m {
    when $m<difficulty><level> { $difficulty-level = $m<difficulty><level><num> }
    when $m<difficulty><kyu> { $difficulty-level = $m<difficulty><kyu><num> }
}
say "difficulty level is $difficulty-level";

