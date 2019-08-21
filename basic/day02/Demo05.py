str_a = "i love "
str_a += "python"
print(str_a)  # i love python
print(str_a*3)  # i love pythoni love pythoni love python

word = "PYTHON"

print(word[0], word[5])  # P N
print(word[-1], word[-6])  # N P

stra = "I love python "
print(stra[0])  # 截取第一个字符
print(stra[0:3])  # 截取从第一个字符开始到第三个字符结束
print(stra[0:6])  # 截取从第一个字符开始到第6个字符结束
print(stra[0:12])  # 截取从第一个字符开始到第12个字符结束
print(stra[0:13])  # 截取从第一个字符开始到第13个字符结束
print(stra[0:20])  # 截取从第一个字符开始到第13个字符结束，整个字符串才13个
print(stra[2:10])  # 截取从第3个字符开始到第10个字符结束
print(stra[3:-1])  # 截取从第4个字符开始到倒数第一个字符
print(stra[3:-2])  # 截取从第4个字符开始到倒数第一个字符
