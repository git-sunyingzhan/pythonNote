a = {12,324,546,76,87}
print(a)    #{546, 324, 12, 76, 87}
print(type(a))  #<class 'set'>

#运用set(str)可以创建一个set集合，此方法会自动删除重复的元素，且是无序集合
set1 = set('asasds1221')
print(set1)     #{'d', 's', '1', '2', 'a'}

#创建一个空集合必须用 set() 而不是{ }，因为{ } 是用来创建一个空字典
set2 = set()
print(type(set2))   #<class 'set'>

#判断集合内是否有12这个元素
print(12 in a)  #True

#差集
a=set('we2431212')
b=set('w2324dffrw')

print(a-b)  #{'e', '1'}
print(a.difference(b))  #{'e', '1'}

#并集
a=set('1234')
b=set('abcdef')
print(a|b) #{'3', 'e', '4', 'b', '1', 'd', '2', 'a', 'c', 'f'}
print(a.union(b))   #{'3', 'e', '4', 'b', '1', 'd', '2', 'a', 'c', 'f'}

#交集
a=set('we2323')
b=set("sdsd21qeqwe")

print(a&b)  #{'2', 'w', 'e'}
print(a.intersection(b))  #{'2', 'w', 'e'}

#对称差集：a^b,a集合中的元素不在b集合中，或者b集合中的元素不在a集合中，
# 其结果是所有这些元素的集合，两个列表里面，互相没有的取出来，也就是只去掉那些互相都有的值

a=set("sdwew1212")
b=set("1234erwwe")

print(a^b) #    {'r', 'd', '4', '3', 's'}
print(a.symmetric_difference(b)) #{'r', 'd', '4', '3', 's'}

#add() 添加一个元素
a = {12,324,546,76,87}
a.add(2)
print(a)    #{546, 2, 324, 12, 76, 87}

#update() 添加多个元素
a = set("12345")
a.update("67890")
a.update(["67890","11"])
print(a) #{'0', '7', '1', '67890', '5', '4', '9', '8', '2', '11', '6', '3'}

#clear()  清空集合
a.clear()
print(a)  #set()

#copy()  拷贝集合
b=set("sdq1f12131")
a=b.copy()
print(a)

#remove(str) 删除指定元素,如果没有就会报错

a=set("1278abfg")
a.remove('a')
print(a) #{'7', 'f', '2', 'b', '1', '8', 'g'}

#discard(): 删除指定元素,元素不存在不报错
a.discard('a')
print(a) #{'2', '8', 'b', '1', '7', 'g', 'f'}

#pop()取出集合对象的顶部元素
a = set('123456')
a.pop()
print(a) #{'5', '2', '6', '3', '4'}
a.pop()
print(a) #{'2', '6', '3', '4'}


print(a.__len__())  #4

