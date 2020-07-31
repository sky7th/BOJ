# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
d = {'b':'d', 'd':'b', 'i':'i', 'l':'l', 'm':'m', 'n':'n', 'o':'o', 'p':'q', 'q':'p', 's':'z', 'z':'s', 'u':'u', 'v':'v', 'w':'w', 'x':'x'}


def solution():
	T = int(input())
	for _ in range(T):
		word = input()
		print('Mirror' if isMirrorWord(word) else 'Normal')


def isMirrorWord(word):
	mirror_word = ''
	for i in range(len(word)-1, -1, -1):
		c = word[i]
		if c in d:
			c = d[c]
		mirror_word += c
	return word == mirror_word


solution()
