#!/usr/bin/env python
import operator


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}.items()


def checkio(ticket):
    subresults = {}

    def calculate(start, end):
        p = (start, end)
        if p not in subresults:
            n = ticket[start:end+1]
            sr = subresults[p] = {int(n): n}
            for s in xrange(start, end):
                for op_name, op_func in OPERATORS:
                    for r1, e1 in calculate(start, s).items():
                        for r2, e2 in calculate(s+1, end).items():
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
    return 100 not in results


if __name__ == '__main__':
    assert checkio('000100') is False
    assert checkio('000101') is True
    assert checkio('238756') is False
    assert checkio('876543') is False
    assert checkio('654321') is False
    assert checkio('000042') is True
    assert checkio('022088') is True
    assert checkio('383330') is False
    assert checkio('383309') is True
    assert checkio('401854') is False
    assert checkio('401877') is True
    print 'looks sane!'
