#第一題
def fb(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fb(n-1) + fb(n-2)

#主程式開始
n = int(input())
print(fb(n))

#第二題
def upper(word):
    word = word[0].upper() + word[1:]
    return word

words = input()
old = words.split(' ')
new = []
for word in old:
    new.append(upper(word))
ans = " ".join(new)
print(ans)

#第三題
n = int(input())
for i in range(n):
    for j in range(n-(i+1)):
        print(" ", end='')
    for k in range(2*(i+1)-1):
        print("*", end='')
    print("")
print(" "*(n-1) + "|")
