#第一題
i = 0
while i <= 20:
    print(i)
    i+=1
    
    
#第二題
string = "hello python"
for word in string:
    print(word)
    
    
#第三題
num = int(input())
ans = []
i = num
while i > 0:
    if num % i == 0:
        ans.append(i)
    i -= 1
ans.sort()
print(ans)

#第四題
items = input()
items = items.split(' ')
print(items)
ans = input()
if ans in items:
    print(ans, "in", items.index(ans)+1)
else:
    print(False)
