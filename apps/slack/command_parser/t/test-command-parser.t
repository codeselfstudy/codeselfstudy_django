# For information on testing, see this document:
# https://design.raku.org/S24.html
use Test;
use JSON::Tiny;

use lib '.';
use CommandParser;

# Test the grammar.
ok Command.parse('js', :rule<language>), '<language> parses: js';
ok Command.parse('js python cobol', :rule<languages>), '<languages> parses: js python cobol';


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

my $bad-url = process-command('https://api.codeselfstudy.com/puzzles/12345 this text should be ignored');
my $h5 = from-json($bad-url);
is $h5<url>, 'https://api.codeselfstudy.com/puzzles/12345';

# Test the source commands.
my $cw-with-difficulty = process-command('cw 2 python js cobol');
my $h6 = from-json($cw-with-difficulty);
is $h6<difficulty>, 2;
is $h6<source>, 'codewars';
is $h6<languages>.sort() eq ['cobol', 'js', 'python'], True;

# This also tests putting a `difficulty` in the middle of languages.
my $codewars-with-difficulty = process-command('codewars fortran hard bf');
my $h7 = from-json($codewars-with-difficulty);
is $h7<difficulty>, 4;
is $h7<languages>.sort() eq ['bf', 'fortran'], True;
is $h7<source>, 'codewars';

my $leetcode-with-difficulty = process-command('leetcode basic');
my $h8 = from-json($leetcode-with-difficulty);
is $h8<difficulty>, 2;
is $h8<source>, 'leetcode';
is $h8<languages> eq [], True;

# This will include a language in the output, even though the receiver of the
# JSON will ignore it. It might have uses later.
my $pe-with-difficulty = process-command('pe crazy python');
my $h9 = from-json($pe-with-difficulty);
is $h9<difficulty>, 4;
is $h9<source>, 'projecteuler';
is $h9<languages>.sort() eq ['python'], True;

done-testing;
