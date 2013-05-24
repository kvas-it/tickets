#!/usr/bin/env python

import argparse
import importlib
import random
import sys


VERBOSE = False


def info(s):
    if VERBOSE:
        sys.stderr.write(s)
        sys.stderr.flush()


def run_tests(module=None, num_tests=100, answers_file='answers.txt',
        exact_number=None, **kw):
    """Import checkio from <module> and run tests on it."""
    if module.endswith('.py'):
        module = module[:-3]
    checkio = importlib.import_module(module).checkio
    info('loaded checkio from {}\n'.format(module))
    if exact_number:
        tests = set([int(exact_number)])
    else:
        tests = set(random.randint(0, 999999) for _ in xrange(num_tests))
    for i, line in enumerate(open(answers_file).xreadlines()):
        if i in tests:
            num, result = line.split(' ', 1)
            assert num == '{:06d}'.format(i)
            info('testing {}: '.format(num))
            answer = checkio(num)
            correct_answer = True if result.startswith('is lucky') else False
            result = answer == correct_answer
            info('{} ({})\n'.format(answer, 'pass' if result else 'fail'))
            if not result:
                return False
    return True


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='Test tickets solutions')
    ap.add_argument('module')
    ap.add_argument('-a', dest='answers_file', metavar='ANSWERS',
            help='File with correct answers', action='store',
            default='answers.txt')
    ap.add_argument('-e', dest='exact_number', metavar='NUMBER',
            help='Run just one test for NUMBER', action='store', type=int,
            default=None)
    ap.add_argument('-n', dest='num_tests', metavar='NUM_TESTS', type=int,
            help='Run NUM_TEST tests.', action='store', default=100)
    ap.add_argument('-v', dest='verbose', action='store_true')
    args = ap.parse_args()

    VERBOSE = args.verbose
    if run_tests(**args.__dict__):
        print 'all tests passed'
    else:
        print 'some tests failed'
