#!/usr/bin/Python3
#encoding="utf-8"
print("|_ 1 _|========= 错误处理 =========|_ 1 _|");
try:
	print("== 准备执行异常 ==")
	res = 10/0
	print("== 执行异常结束 ==")
except ValueError as e:
	print("=== ValueError === :",e)
except ZeroDivisionError as e:
	print("=== ZeroDivisionError === : ",e)
else:
	print("=== else no error ===")
finally:
	print("=== finally ===")

"""
	== 准备执行异常 ==
	=== ZeroDivisionError === :  division by zero
	=== finally ===
"""



import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
"""
	ERROR:root:division by zero
	Traceback (most recent call last):
	  File "Test_08.py", line 33, in main
	    bar('0')
	  File "Test_08.py", line 29, in bar
	    return foo(s) * 2
	  File "Test_08.py", line 26, in foo
	    return 10 / int(s)
	ZeroDivisionError: division by zero
	END

	logging可以记录错误信息，错误出现的位置。
	logging还可以把错误记录到日志文件里，方便事后排查。
"""


#抛出错误 raise
def raise_exception(a):
	if a==0:
		raise ValueError("出现0错误")

def raise_exception_test(a):
	try:
		raise_exception(a)
	except Exception as e:
		raise e
	else:
		return "没有错误"
"""
try:
	value = raise_exception_test(0)
except Exception as e:
	print("===== raise_exception =====",e)
"""
"""
	===== raise_exception ===== 出现0错误
"""
	

# 断言
"""
	凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
"""
def a_01(a):
	bool_ = isinstance(a,(int, float))
	# 如果条件为假，则断言
	assert bool_, "a 必须为数字"
	assert a!=0, "a 不能为0"
	print("******* 测试断言结束 符合条件 *********")

try:
	a_01(0)
except AssertionError as e:
	print(e)
else:
	print("====== 断言没错 ======")



# logging
"""
		这就是logging的好处，它允许你指定记录信息的级别，
	有debug，info，warning，error等几个级别，当我们指定
	level=INFO时，logging.debug就不起作用了。同理，指定
	level=WARNING后，debug和info就不起作用了。这样一来，
	你可以放心地输出不同级别的信息，也不用删除，最后统一控制
	输出哪个级别的信息。
		和assert比，logging不会抛出错误，而且可以输出到文件：
		logging.info()就可以输出一段文本。
"""
logging.basicConfig(level=logging.INFO)
def a_02(a):
	
	logging.info("a = %d",a)
	n = 10 / a

# a_02(0)



#pdb
"""
	启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。
	终端启动方法：
		python3 -m pdb err.py
	输入命令 l 来查看代码：
	输入命令 n 可以单步执行代码：
	任何时候都可以输入命令 p 变量名来查看变量：
		p a
	输入命令 q 结束调试，退出程序：

		pdb.set_trace()这个方法也是用pdb，但是不需要单步执行，我们只
	需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就
	可以设置一个断点：

"""
import pdb
pdb.set_trace()
a = 0
haha = 10



"""
	IDE

		如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。
	目前比较好的Python IDE有PyCharm：

		http://www.jetbrains.com/pycharm/

		另外，Eclipse加上pydev插件也可以调试Python程序。
"""






print("|_ 2 _|========= 单元测试 =========|_ 2 _|");
"""
	分别查看 Dict.py 和 UnitTestDict.py 
	其中 Dict.py 是原类，UnitTestDict.py是测试类 
"""










print("|_ 3 _|========= 文档测试 =========|_ 3 _|");
# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319170285543a4d04751f8846908770660de849f285000












