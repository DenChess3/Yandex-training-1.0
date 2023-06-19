from sys import stdin


dct = {}
for line in stdin:
    words_in_line = line.split()
    for word in words_in_line:
        dct[word] = dct.get(word, 0) + 1

max_value = max(dct.values())
most_frequent = [key for key, value in dct.items() if value == max_value]
print(min(most_frequent))
