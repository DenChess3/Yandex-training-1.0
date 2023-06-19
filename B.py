from sys import stdin

words_older = {}
for line in stdin:
    words_in_line = line.split()
    for word in words_in_line:
        print(words_older.get(word, 0), end=' ')
        words_older[word] = words_older.get(word, 0) + 1