list_a = [12,13,1,56,768]
print(list_a) #[12, 13, 1, 56, 768]
list_b = ['ad','gr','dvbkd']
print(list_b) #['ad', 'gr', 'dvbkd']

#列表可以储存不同类型的数据
list_c = [12,'fdf',65,'ggg']
print(list_c)   #[12, 'fdf', 65, 'ggg']

#列表内可以嵌套列表
list_d = [12,'fdf',list_a,list_b,list_c]
print(list_d)   #[12, 'fdf', [12, 13, 1, 56, 768], ['ad', 'gr', 'dvbkd'], [12, 'fdf', 65, 'ggg']]

#列表可以重复操作
print(list_a*3) #[12, 13, 1, 56, 768, 12, 13, 1, 56, 768, 12, 13, 1, 56, 768]

#通过索引值获取列表对应索引值元素
print(list_a[3])    # 56

#如果索引值为负数，则从尾部开始，从右边往左边数，下标值从1开始
print(list_a[-2])  #  56

#截取列表，从第1个开始，到第2个结束
print(list_a[0:2])  #[12, 13]

#通过索引值改变列表对应元素值
list_a[0] = 111
print(list_a)   #[111, 13, 1, 56, 768]