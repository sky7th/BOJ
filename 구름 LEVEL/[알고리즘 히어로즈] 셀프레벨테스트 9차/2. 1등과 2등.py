# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    ret = 'No'
    ranks = input()
    for i in range(len(ranks) - 3):
        if ranks[i:i + 2] == '21':
            if isContains(ranks[i + 2:], '12'):
                ret = 'Yes'
                break

        if ranks[i:i + 2] == '12':
            if isContains(ranks[i + 2:], '21'):
                ret = 'Yes'
                break

    print(ret)
    return


def isContains(s, target):
    for i in range(len(s) - 1):
        if s[i:i + 2] == target:
            return True
    return False


solution()