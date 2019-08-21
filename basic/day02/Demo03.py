a = 4
b = 2
c = 0
print(a > b and b > c)  # a>b为True继续计算b>c，b>c也为True则结果为True
print(a > b and b < c)  # a>b为True继续计算c<b，b>c结果为False则结果为False
print(a > b or c < b)  # a>b为True则不继续计算c<b，结果为True
print(not c < b)  # c<b为True not True结果为False
print(not a < b)  # a<b为False not Flase结果为True
