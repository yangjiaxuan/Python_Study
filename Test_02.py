
#!/usr/bin/python3
#encoding="utf-8"


print("========== 测试开始 ========")

# =========================== 函数 start =============================
# 函数
def test_01():
	print("这是在调用函数 test_01")

test_01()


# 内置函数
print("取绝对值： abs(-12): %d"%abs(-12))
print("找最大值：max(1,2,3): %d"%max(1,2,3))

def my_abs(a):
	if not isinstance(a,(int, float)):
		print("值不是数字类型")
	else:
		if a >= 0:
			return a
		else:
			return -a

a = my_abs("10")
a = my_abs(-20)
print("my_abs(-20):%d"%a)


def isNumType(a):
	if not isinstance(a,(int, float)):
		return False
	else:
		return True


'''
	这是可变参数
'''
def sum(*numbers):
	_sum = 0
	for num in numbers:
		_sum += num
	return _sum
'''
	这仅仅是参一个参数，但参数可能是数组或者元祖
'''
def sum_a(numbers):
	_sum = 0
	for num in numbers:
		_sum += num
	return _sum

print("---------可变参数 sum(1,2,3):%s"%(sum(1,2,3)))
sum_ = sum_a([1,2,3])
print("---------参数 sum([1,2,3]):%s"%sum_)
sum_ = sum_a((1,2,3))
print("---------参数 sum((1,2,3):%s"%sum_)


print("====================== 此处高能 start ========================")
"""
 函数总结:
    在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
    这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
    顺序：
    	必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
    注意：定义默认参数时一定要指定一个不可变类型，

 	a,b,d ：必选参数
 	c ：拥有默认值 默认参数
 	* : 命名关键字参数 分界符 
 	*args : 可变参数 是一个元祖，元祖的元素不包含其他几种参数，包含字典，其余全在元祖中
 	**dic : 关键字参数 是一个字典，赋值的时候可以直接传 {key1:value1, key2:value2} 也可以传 key1=value1等
"""
def test_HHHH(a, b, d, c=0, *args, **dic):
	print("a=%d b=%d c=%d d=%d args=%s dic=%s"%(a,b,c,d,args,dic))

test_HHHH(1,2,3,4,5,6,7,8,x=10)

# a,b位置参数，不能指定，只能按先后顺序传入， c, d，需要指定
def test_HHHH_01(a, b, *, c, d):
	print("a=",a, " b=",b, " c=",c, "d=",d)
test_HHHH_01(1,2,c=3,d=4)
test_HHHH_01(1,2,d=4,c=3)
test_HHHH_01(1,2)
print("====================== 此处高能 end ========================")

# =========================== move start =============================
import math
'''
	游戏中根据当前点，步幅，角度 计算下一点
'''
def move(x, y, step, angle):
	if not (isNumType(x) and isNumType(y) and isNumType(step) and isNumType(angle)):
		return
	else:
		desX = x + step*math.cos(angle)
		desY = y + step*math.sin(angle)
		return desX, desY

desX, desY = move(10.0,20.0,10.0,2.0)
print("desX:%f desX:%f"%(desX,desY))


# =========================== 递归 start =============================
# 递归

'''
	简单power
	a, b 均为数字，且 b为正整数
'''
def my_power_detail(a, b):

	res = a
	if  b != 1:
		b = b - 1
		res *= my_power_detail(a, b)
	else:
		return a
	return res

def my_power(a, b):
	if not (isNumType(a) and isNumType(b)):
		return 
	else:
		return math.power(a, b)

power = my_power_detail(10,2)
# print("my_power(10,2): %d"%my_power(10,2))
print("my_power_detail(10,2): %d"%power)







