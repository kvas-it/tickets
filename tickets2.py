#!/usr/bin/env python

def checkio(data):
    return not any(abs(x - 100) < 0.00001 for x in comb_values(data))

def comb_values(s):
    yield int(s)
    for i in range(len(s) - 1):
        for l in comb_values(s[:i + 1]):
            for r in comb_values(s[i + 1:]):
                yield l + r
                yield l - r
                yield l * r
                if r != 0: yield l * 1.0 / r


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
