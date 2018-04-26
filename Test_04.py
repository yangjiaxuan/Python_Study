#!/usr/bin/python3
#encoding="utf-8"

print("================== 开始测试 ==================")
print("================== 高阶函数 开始 ==================")
"""
	高阶函数：
		把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是
		指这种高度抽象的编程范式。
	注：
		其实，函数也是变量，函数名是指向函数代码的指针。
"""

# 加法运算
def sum(nums):
	sum = 0
	for num in nums:
		if isinstance(num,(int,float)):
			sum += num
	return sum
# 减法运算
def div(nums):
	div = nums[0]
	for num in range(1,len(nums)):
		div -= nums[num]
	return div

# 四则运算器
# func 是函数引用， 暂时不知道怎么判断一个变量的引用是一个函数
def arithmometer(func, *nums):
	# 此时 nums 是一个数组
	return func(nums)

sum_func = sum
sum_ = arithmometer(sum_func, 1,2,3,4,5)
div_func = div
div_ = arithmometer(div_func, 10,2,3)
print("高阶函数 sum_:",sum_)
print("高阶函数 div_:",div_)








print("=================== map() ================")
'''
		map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数
	依次作用到序列的每个元素，并把结果作为新的Iterator返回。
		利用上面的高阶函数，实现了 map 函数
'''
# 求数组中的元素的平方
def square_func(x):
	if isinstance(x, (int, float)):
		return x * x
	else:
		return None
# 返回的是一个 map 对象，而不是一个list
square_map = map(square_func, [1,2,3,4,5,6]) 

# 遍历 map 对象用 map(list)
square_list = list(square_map) # [1, 4, 9, 16, 25, 36]

print("map() 之 square_list:",list(square_list))  







print("====================== reduce() start ===================")
"""
		reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收
	两个参数，reduce把结果继续和序列的下一个元素做累积计算
		
		def func(a, b):
			....
		这个函数必须有两个入参和一个返回值
		reduce(func, [x1, x2, x3, x4, x5...])
		效果：
		a = func(x1, x2)
		a = func(a , x3)
		a = func(a , x4)
		a = func(a , x5)
		...
		最终返回 a
"""
from functools import reduce
# 求和运算
def sum_2(a, b):
	return a+b
# 求差运算
def div_2(a, b):
	return a-b
sum_ = reduce(sum_2,[1,2,3,4,5])
div_ = reduce(div_2,[10, 2,3])
print("reduce() 之 sum_", sum_)
print("reduce() 之 div_", div_)


print("============== reduce str to int =============")
def strToInt(string):
	def charToNum(char):
		return {"0":0, "1":1, "2":2, "3":3, "4":4, 
				"5":5, "6":6, "7":7, "8":8, "9":9}[char]
	return reduce(lambda x,y : x*10+y, map(charToNum,string))
"""
	lambda: 是一个表达式，而不是一个函数体，他比 def 定义容易许多，
		但是也只能写有限的逻辑
	lambda x,y... : x+y...
		: 是参数和执行体的分界线
		:前 是参数
		:后 是执行体 同时结果是返回值
	lambda 本身也可以作为参数，当然也可以做返回值

	a = lambda x : lambda y : x + y
	b = a(2)
	b(3)    结果是 5

	如果把 lambda 理解为简单函数，上面的代码可以理解为：
	def f(x):
		def sub(y):
			return x+y
		return sub
	a = f
	b = a(2)
	b(3)
"""
string = "123456"
print("string =",string)
print("str to int : strToInt(string)-10 =",strToInt(string)-10)




print("=================== filter() ====================")
"""
		filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的
	函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
"""

def is_odd(n):
	if isinstance(n, (int, float)):
		return n % 2 == 1
	else:
		return False

filter_odd = filter(is_odd, [1,2,3,4,5,6,7,8])
odd_list   = list(filter_odd)

print("filter_odd odd_list:",odd_list)  # [1, 3, 5, 7]


# 删除空字符串
def isStrNotEmpty(string):
	return string and string.strip()

filter_Del_Empty_str = filter(isStrNotEmpty, ['A', '', 'B', None, 'C', '  '])
string_no_empty = list(filter_Del_Empty_str) # ['A', 'B', 'C']

filter_Del_Empty_str = filter(isStrNotEmpty, "  A B C E _This is a str! ")
string_no_empty = list(filter_Del_Empty_str) # ['A', 'B', 'C', 'E', '_', 'T', 'h', 'i', 's', 'i', 's', 'a', 's', 't', 'r', '!']
string_no_empty = reduce(lambda ch1, ch2: ch1+ch2, string_no_empty) # ABCE_Thisisastr!

print("删除空字符串项：string_no_empty =",string_no_empty)








print("==================== sorted() start ========================")
"""
	sorted()函数也是一个高阶函数，
	它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
"""
list_ = [30,-20,5,-12,42,2,1]
list_ = sorted(list_)    # [-20, -12, 1, 2, 5, 30, 42]
# 按绝对值拍
list_ = sorted(list_, key=abs) # [1, 2, 5, -12, -20, 30, 42]


list_ = ["bob", "about", "zoo", "Credit"]

# 区分大小写
list_ = sorted(list_)  # ['Credit', 'about', 'bob', 'zoo']
# 按小写排
list_ = sorted(list_, key=str.lower) # ['about', 'bob', 'Credit', 'zoo']
# 反向排
list_ = sorted(list_, key=str.lower, reverse=True) # ['zoo', 'Credit', 'bob', 'about']



print("sorted() list_ =",list_)











		












