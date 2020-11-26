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
# my $m = Command.parse('lc hard');

# is '3', $m<difficulty><level><num>;
# say Command.parse('cw 1'); say "=======";
# say Command.parse('codewars 8 kyu'); say "=======";
# say Command.parse('lc medium'); say "=======";
# say Command.parse('pe level 3'); say "=======";
# say Command.parse('pe level3'); say "=======";
# say Command.parse('project euler 1'); say "=======";

# Test the url-style commands
my $codewars = process-command('https://www.codewars.com/kata/5265b0885fda8eac5900093b');
my $h = from-json($codewars);
is $h<url>, 'https://www.codewars.com/kata/5265b0885fda8eac5900093b';
is $h.keys, (url);

my $leetcode = process-command('https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/');
my $h = from-json($leetcode);
is $h<url>, 'https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/';

my $projecteuler = process-command('https://projecteuler.net/problem=1');
my $h = from-json($projecteuler);
is $h<url>, 'https://projecteuler.net/problem=1';

my $codeselfstudy = process-command('https://api.codeselfstudy.com/puzzles/12345');
my $h = from-json($codeselfstudy);
is $h<url>, 'https://api.codeselfstudy.com/puzzles/12345';

# ok True, 'true works';
# nok False, 'not true';
# is 'ab'.uc, 'AB', 'string comparison';

done-testing;
