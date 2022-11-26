######################################################################
# Authors: Dimitrios Ntentia, Justin Roberts
# Username: ntentiad, robertsj12
#
# Assignment: T06: Funky Functions Test Suite
# Purpose:  Test suite to test the fruitfull function
#
######################################################################

import sys

from t06_fruitful_function import *


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """
    # This function works correctly--it is verbatim from the text, Chapter 6

    linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)






def testsuite():
    """
    The test_suite function utilizes the testit() function,
    """
    print("\nRunning our function()).")
    ##########################################


    testit(hypo(3, 4) == 5)
    testit(hypo(7, 8) == 9)
    testit(hypo(28, 45) == 52)
    testit(hypo(39, 80) == 89)
    testit(hypo(65, 72) == 97)




    ##########################################


def main():
    """
    :return: None
    """
    testsuite()


if __name__ == "__main__":
    main()
