#第一題解答
c = int(input())
f = c * 9/5 + 32
print(f)

#第二題解答
month = int(input())
day = int(input())
print("你的生日是", month, '/', day)
print("幸運數字是", month+day)

#第三題解答
word = input()
answer = word + word[::-1]
print(answer)
