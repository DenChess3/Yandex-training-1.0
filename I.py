n = int(input())
wordbook = set()
wordbooklow = set()
for i in range(n):
    word = input()
    wordbook.add(word)
    wordbooklow.add(word.lower())

text = input().split()
error = 0
for word in text:
    if [i.isupper() for i in word].count(True) != 1 or word in wordbooklow and word not in wordbook:
        error += 1
print(error)
