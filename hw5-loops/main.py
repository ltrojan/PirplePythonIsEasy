# -*- coding: utf-8 -*-

"""
main.py: Homework #4: Lists (Python Is Easy course by Pirple)

Details:

You're about to do an assignment called "Fizz Buzz", which is one of the
classic programming challenges. It is a favorite for interviewers, and a
shocking number of job-applicants can't get it right. But you won't be
one of those people. Here are the rules for the assignment (as specified
by Imran Gory):

Write a program that prints the numbers from 1 to 100.

But for multiples of three print "Fizz" instead of the number and for
the multiples of five print "Buzz".

For numbers which are multiples of both three and five print "FizzBuzz".

The one hint you'll likely need is:

There is a Python operator called "modulo", represented by the
percentage sign (%) that gives you the remainder left over after
division. So for example:

 6 % 3

Equals zero. Because after dividing 6 by 3, there is zero leftover.
Whereas:

6 % 4

Equals 2. Because after dividing 6 by 4, there are 2 left over from the
six.

If that was confusing, don't worry. It will make more sense as you use
it. The point is: the modulo operator is useful for finding out if X is
a multiple of Y. If it is, then X % Y will yield zero. Knowing this
should help you complete this assignment without any issue.


Extra Credit:

Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth
print statement: "prime". You should print this whenever you encounter
a number that is prime (divisible only by itself and one). As you
implement this, don't worry about the efficiency of the algorithm you
use to check for primes. It's okay for it to be slow.



Turning it In:

Zip up your code files and attach them here to receive a grade and
continue with the course.

Submit your assignment
You may only submit one file with maximum 100 MB in size
"""

__author__ = "Corrado Lanera"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"


# ----------------------------------------------------------------------


# ---- Functions' checks ----

print("\n\n=== Checks starts ===\n")
check_res = [
    False
]

if all(check_res):
    print("\n=== All checks passed ===\n\n")
else:
    wrong = [i + 1 for i, x in enumerate(check_res) if not x]
    print("\n=== !!! Check(s) not passed:", wrong, "!!! ===\n\n")
    exit()

