# For information on testing, see this document:
# https://design.raku.org/S24.html
use Test;
use JSON::Tiny;

use lib '.';
use CommandParser;

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

# Test the grammar.
ok Command.parse('js', :rule<language>), '<language> parses: js';
ok Command.parse('js python cobol', :rule<languages>), '<languages> parses: js python cobol';

say 'HERE';


# Test the url-style commands
my $codewars = process-command('https://www.codewars.com/kata/5265b0885fda8eac5900093b');
my $h1 = from-json($codewars);
is $h1.keys, ('url');
is $h1<url>, 'https://www.codewars.com/kata/5265b0885fda8eac5900093b';

my $leetcode = process-command('https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/');
my $h2 = from-json($leetcode);
is $h2<url>, 'https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/';

my $projecteuler = process-command('https://projecteuler.net/problem=1');
my $h3 = from-json($projecteuler);
is $h3<url>, 'https://projecteuler.net/problem=1';

my $codeselfstudy = process-command('https://api.codeselfstudy.com/puzzles/12345');
my $h4 = from-json($codeselfstudy);
is $h4<url>, 'https://api.codeselfstudy.com/puzzles/12345';

done-testing;
