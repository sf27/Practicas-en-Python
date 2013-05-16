#!/usr/bin/python
# -*- coding: UTF-8 -*-

def space(n):
	for i in range(n):
		print '',

def triangle(n):
	if n <= 0:
		return []
	l = [[1]]
	for h in range(n-1):
		r = []
		a = 0
		for i in l[-1]:
			r.append(i+a)
			a = i
		r.append(a)
		l.append(r)
	return l
n = triangle(10)
k = len(n)
for i in n:
	space(k*2) 
	print i
	k -= 1

#                    [1]
#                  [1, 1]
#                [1, 2, 1]
#              [1, 3, 3, 1]
#            [1, 4, 6, 4, 1]
#          [1, 5, 10, 10, 5, 1]
#        [1, 6, 15, 20, 15, 6, 1]
#      [1, 7, 21, 35, 35, 21, 7, 1]
#    [1, 8, 28, 56, 70, 56, 28, 8, 1]
#  [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]