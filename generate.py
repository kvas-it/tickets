#!/usr/bin/env python

import operator
import argparse
import re
import sys


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}.items()


def precise_eval(expr):
    expr = re.sub('\d+', lambda s: str(int(s.group(0))), expr)
    expr = expr.replace('/', '* 1.0 /')
    return eval(expr)


def checkio(ticketi, withCheck=True):
    subresults = {}

    def calculate(start, end):
        p = (start, end)
        if p not in subresults:
            n = ticket[start:end + 1]
            sr = subresults[p] = {int(n): n}
            for s in xrange(start, end):
                for op_name, op_func in OPERATORS:
                    for r1, e1 in calculate(start, s).items():
                        for r2, e2 in calculate(s + 1, end).items():
                            try:
                                res = op_func(r1, r2)
                            except ZeroDivisionError:
                                continue
                            if start == 0 and end == 5:
                                if (not isinstance(res, int) and
                                        abs(res - 100) < 0.000001):
                                    res = int(round(res))
                            if res not in sr:
                                sr[res] = '(%s %s %s)' % (e1, op_name, e2)
        return subresults[p]

    results = calculate(0, len(ticket) - 1)
    if 100 in results:
        expr = results[100]
        res = precise_eval(expr)
        if withCheck and abs(res - 100) > 0.00001:
            return '-> ' + expr + ' but failed check: %g' % res
        else:
            return '-> ' + expr
    else:
        return 'is lucky'


if __name__ == '__main__':
    all_tickets = xrange(1000000)

    ap = argparse.ArgumentParser(description='Generate solutions table for '
            'the Mathematically Lucky Tickets task.')
    ap.add_argument('-i', help='Use integer division', dest='intdiv',
            action='store_true')
    ap.add_argument('-n', help='Calculate specific answer', dest='number',
            action='store', type=int, metavar='XXXXXX', default=None)
    args = ap.parse_args()

    if args.intdiv:
        OPERATORS[3] = ('/', operator.div)
    if args.number is not None:
        all_tickets = [args.number]

    for i in all_tickets:
        ticket = '%06d' % i
        print ticket, checkio(ticket, withCheck=not args.intdiv)
        if i % 10000 == 0:
            sys.stderr.write('%d\n' % i)
        elif i % 100 == 0:
            sys.stderr.write('.')
            sys.stderr.flush()
