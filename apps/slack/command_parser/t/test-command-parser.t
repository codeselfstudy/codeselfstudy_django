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
is $h1.keys, ('url'), 'codewars url command outputs a url';
is $h1<url>, 'https://www.codewars.com/kata/5265b0885fda8eac5900093b', 'codewars understands a codwars url';

my $leetcode = process-command('https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/');
my $h2 = from-json($leetcode);
is $h2<url>, 'https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/', 'leetcode url command sends back the url';

my $projecteuler = process-command('https://projecteuler.net/problem=1');
my $h3 = from-json($projecteuler);
is $h3<url>, 'https://projecteuler.net/problem=1', 'projecteuler url command sends back url';

my $codeselfstudy = process-command('https://api.codeselfstudy.com/puzzles/12345');
my $h4 = from-json($codeselfstudy);
is $h4<url>, 'https://api.codeselfstudy.com/puzzles/12345', 'codeselfstudy url command sends back url';

my $bad-url = process-command('https://api.codeselfstudy.com/puzzles/12345 this text should be ignored');
my $h5 = from-json($bad-url);
is $h5<url>, 'https://api.codeselfstudy.com/puzzles/12345', 'bad-url ignores extra text after the url';

# Test the source commands.
my $cw-with-difficulty = process-command('cw 2 python js cobol');
my $h6 = from-json($cw-with-difficulty);
is $h6<difficulty>, 2, 'cw-with-difficulty understands the difficulty';
is $h6<source>, 'codewars', 'cw-with-difficulty understands the source';
is $h6<languages>.sort() eq ['cobol', 'js', 'python'], True, 'cw-with-difficulty understands multiple languages';

# This also tests putting a `difficulty` in the middle of languages.
my $codewars-with-difficulty = process-command('codewars fortran kyu 1 bf');
my $h7 = from-json($codewars-with-difficulty);
is $h7<difficulty>, 4, 'codewars-with-difficulty found difficulty';
is $h7<languages>.sort() eq ['bf', 'fortran'], True, 'codewars-with-difficulty found multiple languages';
is $h7<source>, 'codewars', 'codewars-with-difficulty found source';

my $leetcode-with-difficulty = process-command('leetcode basic');
my $h8 = from-json($leetcode-with-difficulty);
is $h8<difficulty>, 2, 'leetcode-with-difficulty found difficulty';
is $h8<source>, 'leetcode', 'leetcode-with-difficulty found source';
is $h8<languages> eq [], True, 'leetcode-with-difficulty didnt fail when language is blank';

# This will include a language in the output, even though the receiver of the
# JSON will ignore it. It might have uses later.
my $pe-with-difficulty = process-command('pe crazy python');
my $h9 = from-json($pe-with-difficulty);
is $h9<difficulty>, 4, 'pe-with-difficulty understood "crazy"';
is $h9<source>, 'projecteuler', 'pe-with-difficulty get source';
is $h9<languages>.sort() eq ['python'], True, 'pe-with-difficulty understood language, even though not needed';

done-testing;
