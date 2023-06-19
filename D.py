from sys import stdin
import re

s = set()
for line in stdin:
    for i in line.split():
        s.add(i)
print(len(s))