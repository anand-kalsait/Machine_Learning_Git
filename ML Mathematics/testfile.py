dictt = {0:'lol'}
for _ in range(int(input())):
    name = input()
    score = float(input())
    dictt[score] = name
print(dictt)

scores = list(dictt.keys())
print(scores)
scores.sort()
print(scores)
print(dictt[scores[-2]])
