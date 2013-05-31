tickets
=======

Mathematically lucky tickets problem (developed for CheckIO.org)

The "Mathematically lucky tickets" concept is similar to the well known "Lucky tickets" from the former Soviet Union. It refers to the Soviet era public transportation tickets that had 6-digit numbers printed on them.

Given a ticket number, a combination of its digits is a mathematical expression that is made according to the following rules.

    1. Digits of the number can be split into a number of groups.
    2. It's not allowed to change the order of groups or the order of digits in
    the groups.
    3. Each group is treated as one integer number.
    4. Operation signs (+, -, * and /) are placed between the groups.
    5. Parenthesis are placed around subexpressions to eliminate any ambiguity
    in evaluation order.

For example:

    * 238756 -> (2 * (38 + ((7 + 5) * 6)))
    * 000859 -> (0 + (00 + (8 + (5 + 9))))
    * 561403 -> (5 * (6 + (1 + (40 / 3))))

The ticket is considered mathematically lucky if no combination of its digits evaluates to 100. For example:

    * 000000 is obviously lucky; whatever combinations you construct, they all
    evaluate to zero,
    * 707409 and 561709 are also lucky, but less obviously so,
    * 595347 is not lucky: (5 + ((9 * 5) + (3 + 47))) = 100,
    * 593347 is not lucky: (5 + ((9 / (3 / 34)) - 7)) = 100,
    * 271353 is not lucky: (2 - (7 * (((1 / 3) - 5) * 3))) = 100,

The combination has to evaluate to 100 exactly to be counted. Fractions can occur in intermediate calculations (like in above examples for 593347 and 271353) but the result must be integer.

Task: Given a 6-digit number of the ticket, the program should determine whether it's mathematically lucky or not.

Input: A string, containing 6 digits.

Output: True or False.

Example:

checkio('000000') == True
checkio('707409') == True
checkio('595347') == False
checkio('271353') == False
