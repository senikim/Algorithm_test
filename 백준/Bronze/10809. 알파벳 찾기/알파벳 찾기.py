# a-z가 word안에서
# 처음 등장하는 위치
# 없으면 -1

word = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for a in alphabet:
    if a in word:
        print(word.find(a), end = ' ')
    else:
        print(-1, end = ' ')