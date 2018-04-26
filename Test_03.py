#!/usr/bin/python3
#encoding="utf-8"

print("====================== 开始测试 ======================")

print("====================== 切片 ======================")

list_ = list(range(100))

print("--------list :",list_)

# 切片
# 前3个元素
subList = list_[0:3]

# 后三个元素
count = len(list_) # 100
subList = list_[-3:count] # [97, 98, 99]

"""
	注：		
		正数 0              -    len(list) 是从前往后数，元素依次位置
		负数 -len(list)     -    -1        也是从前往后数，元素的依次位置
		上面是两行是 一一对应的

		[a : b]    [a:b) 前开后闭 也就是包含 a 处元素，不包含 b 处元素。
		a: 起始位置 如果没有默认为 0
		b: 终止位置 如果没有默认为 len(list)
		条件 ： a > b, 不然取不到值
"""

subList = list_[8 : 9]  # [8]
subList = list_[9 : 8]  # []
print ("--------subList :",subList)










print("=========================== 迭代 ========================")
# 数组迭代
list_ = [1,2,3,4,5,6]
for x in list_:
	print("数组迭代：",x)
list_ = [(1,2), (3,4), (5,6)]
for x, y in list_:
	print("数组迭代——plus：x = %d, y = %d"%(x, y))

# 元祖迭代
tuple_ = (1,2,3,4,5,6)
for x in tuple_:
	print("元祖迭代：",x)
tuple_ = ((1,2), (3,4), (5,6))
for x, y in tuple_:
	print("元祖迭代——plus：x = %d, y = %d"%(x, y))

# 字典迭代
dic_ = {"1":"1V", "2":"2V", "3":"3V"}
for key in dic_:
	print("字典迭代：key = %s, value = %s"%(key, dic_[key]))
for key, value in dic_.items():
	print("字典迭代--plus：key = %s, value = %s"%(key, value))




# 判断类型是否可以迭代
from collections import Iterable # Iterable : 迭代器
"""
	isinstance() 判断类型 两种写法
		1: isinstance(a, x)  a 是否为 x 类型
		2: isinstance(a, (x, y...)) a 是否为 (x, y...)中类型的一种
"""
bool_ = isinstance("abc",Iterable)    # True
bool_ = isinstance([1,2,3], Iterable) # True
bool_ = isinstance((1,2,3), Iterable) # True
bool_ = isinstance(123, Iterable)     # False  


print(bool_)










print("===================== 列表生成式 ===================")
# 生成list
list_ = list(range(2, 8)) # [2, 3, 4, 5, 6, 7]

list_ = []
for x in range(1,10):
	list_.append(x * x)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 上面的另一种生成方法
list_ = [x * x for x in range(1,10)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 后面加上判断条件
list_ = [x * x for x in range(1,10) if x%2 == 0]
# [4, 16, 36, 64]


list_ = [m+n for m in "ABC" for n in "XYZ"]
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
list_ = []
# 上面类似于下面的实现
for m in "ABC":
	for n in "XYZ":
		list_.append(m+n)
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

"""
	总结： 
		列表生成式分为三部分
		1 m+n : 列表元素内容
		2 循环体 : 元素来源
		3 判断式 : 根据判断式的返回值 来确定该
"""











import os

list_ = []
# 找出当前文件所在文件夹中带 "." 的文件
list_ = [d for d in os.listdir('.')]
# ['.DS_Store', 'Test_01.py', 'Test_02.py', 'Test_03.py']
print(list_)  


print("================================ 生成式 ====================")
# 生成式
"""
	通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限
的。创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几
个元素，那后面绝大多数元素占用的空间都白白浪费了。
	所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算
出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边
环一边计算的机制，称为生成器：generator。
	生成方法：
	1: 只要把一个列表生成式的[]改成()
	    generator = (x for x in range(1,10))
	2: yield 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，
	而是一个generator
"""

generator = (x for x in range(1,10)) # <generator object <genexpr> at 0x1045b01a8>

next_gen = next(generator) # 1   会把 generator 的指针向后移动一位。
next_gen = next(generator) # 2

# 注： 当generator 的指针指向了最后一个元素，generator 也就没有了
# 遍历 generator
for x in generator:
	print(x)          # 没遍历一次会把指针向后移动一位     





print("======= 打印 斐波拉契数列（Fibonacci）====== ")
def fibonacci(max):
	n, a, b = 0, 0, 1
	while n < max:
	 	print(b)
	 	a, b = b, a+b
	 	n = n + 1

fibonacci(15)    # 1、1、2、3、5、8、13、21、34、55、89、144、233、377、610

print("----------- 斐波拉契数列 generator ------------")
"""
		generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后
	一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到
	yield语句返回，再次执行时从上次返回的yield语句处继续执行。
"""
def fibonacci_generator(max):
	n, a, b = 0, 0, 1
	while n < max:
	 	yield b
	 	a, b = b, a+b
	 	n = n + 1
	return "done"

generator = fibonacci_generator(15)
next_gen = next(generator) # 1
next_gen = next(generator) # 1
next_gen = next(generator) # 2
next_gen = next(generator) # 3
next_gen = next(generator) # 5

print(next_gen)

# for 循环无法获取 返回值 done
for next_gen in fibonacci_generator(15):
	print(next_gen)

g = fibonacci_generator(8)
# 使用while循环，采用捕捉的方法可以获取返回值
while True:
	try:
		print(next(g))
	except StopIteration as e:
		print(e.value) # e.value 内装的就是返回值
		break
		
	
	












