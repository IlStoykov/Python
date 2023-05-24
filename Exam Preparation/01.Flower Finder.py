# 83 points
from collections import deque
result = ""
find_word = False
flowers_dict = {"rose":'', "tulip":'', "lotus":'', "daffodil":''}
vowels = deque([str(x) for x in input().split(" ")])
consonants = ([str(x) for x in input().split(" ")])

while vowels and consonants and not find_word:
    vow = vowels.popleft()
    cons = consonants.pop()
    for item in flowers_dict.keys():
        for letter in item:
            if vow == letter and vow not in flowers_dict[item]:
                flowers_dict[item] += vow
            if cons == letter and cons not in flowers_dict[item]:
                flowers_dict[item] += cons
            for k, v in flowers_dict.items():
                if len(k) == len(v):
                    result = k
                    find_word = True
                    break

if find_word:
    print(f"Word found: {result}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(str(x) for x in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(str(x) for x in consonants)}")




#
# print(flowers_dict)
# d = ''
# fl = "rose"
# w ='r'
# for item in fl:
#     if w == item:
#         d += w
#         print(d)

