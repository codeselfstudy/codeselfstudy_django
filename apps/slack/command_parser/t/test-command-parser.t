# For information on testing, see this document:
# https://design.raku.org/S24.html
use Test;
use JSON::Tiny;

use lib '.';
use CommandParser;

# ok True, 'true works';
# nok False, 'not true';
# is 'ab'.uc, 'AB', 'string comparison';

# TODO:
# test all the difficulties
# test <url>
#
my $m = Command.parse('lc hard');

# is '3', $m<difficulty><level><num>;
# say Command.parse('cw 1'); say "=======";
# say Command.parse('codewars 8 kyu'); say "=======";
# say Command.parse('lc medium'); say "=======";
# say Command.parse('pe level 3'); say "=======";
# say Command.parse('pe level3'); say "=======";
# say Command.parse('project euler 1'); say "=======";

done-testing;
