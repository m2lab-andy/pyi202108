#第一題
words = input()
words = words.split(' ')
for word in words:
    print(word.upper(),end='')
words.reverse()
for word in words:
    print(word.lower(),end='')
    
    
#第二題
words = input()
words = words.split(' ')
words.append("python")
words.insert(0, "python")
print(words)

second = []
i = 1
while i <= len(words) - 1:
    second.append(words[i])
    i += 2
print(second)

three = words[:int(len(words)/2)]
print(three[::-1])

four = words[int(len(words)/2):]
print(four[::-1])


#第三題
num = int(input())
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 != 0 and num % 5 != 0:
    print(num)
elif num % 3 == 0:
    print("Fizz")
else:
    print("Buzz")
    
    
#第四題
num = int(input())
if num == 10:
    print(10)
elif num > 10:
    print("這個數字超過10了")
else:
    print("請輸入10")
