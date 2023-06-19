s1 = input()
s2 = input()
dict_s1 = {}
dict_s2 = {}
for i in range(len(s1) - 1):
    dict_s1[s1[i:i + 2]] = dict_s1.get(s1[i:i + 2], 0) + 1
for i in range(len(s2) - 1):
    dict_s2[s2[i:i + 2]] = dict_s2.get(s2[i:i + 2], 0) + 1
dist = 0
for key, value in dict_s1.items():
    if dict_s2.get(key, 0) != 0:
        dist += value
print(dist)