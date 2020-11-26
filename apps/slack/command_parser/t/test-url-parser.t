# For information on testing, see this document:
# https://design.raku.org/S24.html
use Test;
use JSON::Tiny;

use lib '.';
use URLParser;

# my $codewars = URL.parse('https://www.codewars.com/kata/5265b0885fda8eac5900093b');
# say $codewars;
# say '-------';
# my $leetcode = URL.parse('https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/');
# say $leetcode;
# say '-------';
# my $projecteuler = URL.parse('https://projecteuler.net/problem=1');
# say $projecteuler;
# say '-------';
# my $codeselfstudy = URL.parse('https://api.codeselfstudy.com/puzzles/12345');
# say $codeselfstudy;
# say '-------';

# ok True, 'true works';
# nok False, 'not true';
# is 'ab'.uc, 'AB', 'string comparison';

done-testing;
