#!/usr/bin/python3
#encoding="utf-8"

print("===================== 开始测试 ==================")
print(" |-- 1 ============== 返回函数 ==================")
"""
	把函数作为返回值进行返回
"""
def handle(x):
	def add(y):
		return x+y
	return add
add_ = handle(5)
add_res = add_(10) # 15
print("返回函数 之 add:",add_res)











print(" |-- 2 ============== 闭包 ==================")
"""
		注意到返回的函数在其定义内部引用了局部变量args，所以，
	当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
	所以，闭包用起来简单，实现起来可不容易。
"""
def func_builder():
	funcs = []
	for x in range(1,4):
		def f():
			return x*x
		funcs.append(f)
	return funcs

f1,f2,f3 = func_builder()
f1_ = f1()
f2_ = f2()
f3_ = f3()
"""
	f1_:9 f2_:9 f3_:9
	全是 9
		因为闭包中引用了 x funcs装载了闭包，在for循环中，闭包还没有执行，是在
	外边才被调用的，但是在for循环中，x 的引用值随着for 循环在变化，直到循环结束，
	x = 3， 在外边调用的时候 所有引用的 x 值都是 3，所以结果都是 9。

"""
print("闭包测试 f1_:%d f2_:%d f3_:%d"%(f1_,f2_,f3_))
# 上面代码换一种写法
def func_builder():
	def f(x):
		def g():
			return x*x
		return g
	funcs = []
	for x in range(1,4):
		funcs.append(f(x))
	return funcs

f1,f2,f3 = func_builder()
f1_ = f1()
f2_ = f2()
f3_ = f3()

"""
	f(x) 把for 循环中的 x 转换为自己的 x 引用，两个引用不指向同一个内存
"""
# 闭包测试--plus f1_:1 f2_:4 f3_:9
print("闭包测试--plus f1_:%d f2_:%d f3_:%d"%(f1_,f2_,f3_))









print(" |-- 3 ============== 匿名函数 ==================")
"""
	lambda 匿名函数，更像一个表达式
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
def square(x):
	if isinstance(x, (int, float)):
		return x * x
	else:
		return None
square_ = square(2) # 4

square_la = lambda x : x*x
square_ = square_la(3) # 9
print("匿名函数： square =",square_)  











print(" |-- 4 ============== 装饰器 ==================")

def now():
	print("2017-5-10")

"""
	需求：我希望在调用函数时打印 函数名
"""
func = now
# 获取函数名
func_name = func.__name__  # now


def log(func):
	def wrapper(*args, **kw):
		print("call %s()"%func.__name__)
		return func(*args, **kw)
	return wrapper
# 在函数上面加了一个 @+定义装饰的函数名 即可 示例说明看上边
@log  # 此处的 log 就是一个装饰器
def a__a():
	print("2017-5-10 -- a --")
@log
def b__b():
	print("2017-5-10 -- b --")

# call a__a()
# 2017-5-10 -- a --
a__a()
# call b__b()
# 2017-5-10 -- b --
b__b()

"""
		由于log()是一个decorator，返回一个函数，所以，原来的now()
	函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()
	将执行新函数，即在log()函数中返回的wrapper()函数。
		wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()
	函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接
	着调用原始函数。
		如果decorator本身需要传入参数，那就需要编写一个返回decorator
	的高阶函数，写出来会更复杂。
"""
def log_2(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print("%s %s()"%(text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator
			
@log_2("装饰器 log_2:")
def log_2_test():
	print("这是在测试 log_2_test")

# 装饰器 log_2: log_2_test()
# 这是在测试 log_2_test
log_2_test()











print(" |-- 5 ============== 偏函数 ==================")
"""
		Python的functools模块提供了很多有用的功能，其中一个就是偏函数
	（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。
		通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到
	 这一点。
"""
import functools
int_char = "12345"
# 字符串转 int
int_ = int(int_char) # 12345

# 原字符串为 8进制, 转成 10进制
int_ = int(int_char, base=8) # 5349

# 原字符串为 16进制, 转成 10进制
int_ = int(int_char, 16) # 74565



"""
	如果经常使用，原字符为 2进制
	使用下面方法可以为 int()函数设定默认值，然后附一个新的函数名
""" 

int2 = functools.partial(int, base=2)

int_ = int2("1111")  # 15

print("=== int_char : %d ==="%int_)



















