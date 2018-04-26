#!/usr/bin/Python3
#encoding="utf-8"


print("======================= IO =======================")
"""
		IO在计算机中指Input/Output，也就是输入和输出。由于程序和运行时
	数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地
	方，通常是磁盘、网络等，就需要IO接口。
		以计算机为 参照：
			计算机向外输出即为：Output
			向计算机内不输入即为： Input

	IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数
据就是水管里的水，但是只能单向流动。Input Stream就是数据从外面（磁盘、网络）
流进内存，Output Stream就是数据从内存流到外面去。对于浏览网页来说，浏览器
和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。

	由于CPU和内存的速度远远高于外设的速度，所以，在IO编程中，就存在速度严重
不匹配的问题。举个例子来说，比如要把100M的数据写入磁盘，CPU输出100M的数据只
需要0.01秒，可是磁盘要接收这100M数据可能需要10秒，怎么办呢？有两种办法：

	第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，
再接着往下执行，这种模式称为同步IO；
	另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，
于是，后续代码可以立刻接着执行，这种模式称为异步IO。

	异步比同步高效的多，但是，异步的复杂度要不同步高太多。

	注意，本章的IO编程都是同步模式，异步IO由于复杂度太高。

r 读； w写； a追加；
"""

# 读文件
def readTest():
	try: 
		""" 
		    encoding: 默认 utf-8 若不是传入值即可。
		    error: 挡在编码的时候遇到错误的处理方式，简单的直接忽略。
	    """
		f = open("../IOTest_01.rtf"
			 ,"r", encoding='gbk', errors="ignore")
	except Exception as e: # 此处 e 实际为IOError
		return None
	return f


# 不用调用 close()函数
# string = f.read()  
# print("string:\n",string)

f = readTest()
if f != None:
	line = f.readline() # 读取一行
	print("一行:",line)

f = readTest()
if f != None:
	for line in f.readlines():
		print("逐行：",line.strip()) # 把末尾的'\n'删掉


"""
	file-like Object:
		像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like
	 Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like 
	 Object不要求从特定类继承，只要写个read()方法就行。

		StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
"""

"""
		前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，
	比如图片、视频等等，用'rb'模式打开文件即可：
"""

f = open("../IOImage.jpeg", "rb")
image = f.read()


# 写文件
def writeTest():
	try:
		f = open("../IOTest_02.txt" ,"w")
		return f
	except Exception as e:
		return None

f = writeTest()
if f != None:
	f.write("\n====== 我擦嘞... wakaka new! ======")

f = open("/Users/yangxu/Desktop/Python/2017-05-08/IOTest.rtf"
			 ,"r")
print("newRead:\n",f.read())










print("===================== StringIO和BytesIO ================")
"""
	StringIO顾名思义就是在内存中读写str。
"""
from io import StringIO

f = StringIO()

byte_num = f.write("hello") # 5
byte_num = f.write(" ")     # 1
byte_num = f.write("world!")# 6

value    = f.getvalue() # hello world!


f = StringIO(" Lili: Hi\n Lucy:Hi\n Lili: what are you 弄啥哩！")
for line in f.readlines():
	print(line)

"""
	Lili: Hi

	Lucy:Hi

	Lili: what are you 弄啥哩！
"""

# BytesIO
"""
	StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
"""
from io import BytesIO
f = BytesIO()
byte_num = f.write("中国很牛！！！".encode('utf-8')) # 21

# b'\xe4\xb8\xad\xe5\x9b\xbd\xe5\xbe\x88\xe7\x89\x9b\xef\xbc\x81\xef\xbc\x81\xef\xbc\x81'
byte = f.getvalue() 

byte = f.read()  # b''







print("================= 操作文件和目录 ====================")
"""
		其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，
	Python内置的os模块也可以直接调用操作系统提供的接口函数。
"""
import os
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
value = os.name  # posix

# 获取详细信息
value = os.uname()
"""
	posix.uname_result(
		sysname='Darwin', 
		nodename='yangsendeMacBook-Pro.local', 
		release='15.6.0', 
		version='Darwin Kernel Version 15.6.0: Mon Aug 29 20:21:34 PDT 2016; 
		root:xnu-3248.60.11~1/RELEASE_X86_64', 
		machine='x86_64')

	注意uname()函数在Windows上不提供
"""
"""
	================ 环境变量 =============
	获取某个环境变量的值，可以调用os.environ.get('key')：
"""

# /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Users/yangxu/.rvm/bin
value = os.environ.get("PATH")
value = os.environ.get("x", "default") # default 设置 x 对应的值为 default


# 操作文件和目录
"""
		操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，
	这一点要注意一下。查看、创建和删除目录可以这么调用：
"""
# 查看当前目录的绝对路径:
value = os.path.abspath('.') #/Users/yangxu/Desktop/Python/2017-05-08/01
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# value = os.path.join(value,"add") # Users/yangxu/Desktop/Python/2017-05-08/01/add/a

# value = os.mkdir(value) # None
# value = os.mkdir(value+"/a")

# 合并路径 自己加 '/'' 拼接也行，但这种拼接方式是跨平台的
# Linux/Unix/Mac 中间加的是 '/'    
# window 中间加的是 '\'
value_ = os.path.join(value,"test") # /Users/yangxu/Desktop/Python/2017-05-08/01


import os
# 创建文件夹
def createDir(path):
	if os.path.isdir(path) and os.path.exists(path):
		return "文件已存在！"
	else:
		bool_ = os.mkdir(path)
		return "文件创建成功！"
	
# import pdb
# pdb.set_trace()

bool_ = createDir(value_)
bool_ = createDir(value+"/test_01")
bool_ = createDir(value+"/test_02")

# 删除文件夹
bool_ = os.rmdir(value+"/test")

# 拆分路径 后一部分总是最后级别的目录或文件名：
value = os.path.split(value_) # ('/Users/yangxu/Desktop/Python/2017-05-08/01', 'test')
value = value[0] # /Users/yangxu/Desktop/Python/2017-05-08/01

# 得到文件扩展名
value_ = "/Users/yangxu/Desktop/Python/2017-05-08/01/Test_09.py"
extend = os.path.splitext(value_)[1] # .py

# 创建一个文件
f = open("1.txt" ,"w")
f.write("1111111")

# 重命名
# 假设当前目录有一个 1.txt 如果文件不存在会报错
# 如果存在 1.txt 和 2.txt 那么，会直接把 1.txt 改成 2.txt,同时删掉 2.txt
bool_ = os.rename("1.txt","2.txt") 

print(extend)
print(value)









print("|- ==================== 序列化 ================= -|")
"""
	pickle
		序列化： 
			dumps(dic)  
				方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
			dump(dic,f)
				直接序列化 并写入文件。
		反序列化：
			load(f)
				从文件中加载序列化数据，并反序列化。

"""
import pickle

dic = dict(name="lisi", age=20)
# 序列化
pickleDic = pickle.dumps(dic)
f = open("../pickle.txt", "wb")
f.write(pickleDic)
f.close

dic = dict(name="zhangsan", age=10)
# 序列化并存到文件中
f = open("../pickle.txt", "ab")
pickle.dump(dic,f)
f.close()

# 反序列化
f = open("../pickle.txt", "rb")
dic = pickle.load(f) # {'name': 'lisi', 'age': 20}
print("=== 反序列化 ===",dic)

dic = pickle.load(f) # {'name': 'zhangsan', 'age': 10}
print("=== 反序列化 ===",dic)




"""
		如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
	比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可
	以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准
	格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

		JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的
	数据类型对应如下：

		JSON类型	Python类型":
			{}				dict
			[]				list
			"string"		str
			1234.56			int或float
			true/false		True/False
			null			None
		Python内置的os模块也可以直接调用操作系统提供的接口函数。的json模块提
	供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成
	一个JSON：

		json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, 
				check_circular=True, allow_nan=True, cls=None, indent=None, 
				separators=None, default=None, sort_keys=False, **kw)
				
		json.dumps(obj, *, skipkeys=False, ensure_ascii=True, 
					check_circular=True, allow_nan=True, cls=None, 
					indent=None, separators=None, default=None, 
					sort_keys=False, **kw)
		
		json.load(fp, *, cls=None, object_hook=None, parse_float=None, 
				 parse_int=None, parse_constant=None, object_pairs_hook=None,
				  **kw)

		json.loads(s, *, encoding=None, cls=None, object_hook=None, 
				   parse_float=None, parse_int=None, parse_constant=None, 
				   object_pairs_hook=None, **kw)
"""
import json

# 序列化字符串
json_str = '{"age":20 , "name":"Tom"}'
json_str = json.dumps(json_str) # "{\"age\":20 , \"name\":\"Tom\"}"
print("=== json ===", json_str) #

class Student(object):
	def __init__(self, name, age, score):
		super(Student, self).__init__()
		self.name  = name
		self.age   = age
		self.score = score

	def modelToDic(self):
		return {"name"  : self.name,
				"age"   : self.age,
				"score" : self.score}

	@classmethod  # 定义静态方法 或者说 类方法 或者用 @staticmethod
	def dicToModel(self, dic):
		return Student(dic["name"], dic["age"], dic["score"])
		

stu = Student("Lucy", 11, 100)

# 其实在 Python 中有一个封装好的属性 __dict__ 他返回的就是 模型的字典
# stu.__dict__
# {"name": "Lucy", "age": 11, "score": 100}
stu_dumps = json.dumps(stu, default=lambda stu : stu.modelToDic())
# {"name": "Lucy", "age": 11, "score": 100}
stu_dumps = json.dumps(stu, default=lambda stu : stu.__dict__)


stu_loads = json.loads(stu_dumps, object_hook=lambda stu_dumps : Student.dicToModel(stu_dumps))
name  = stu_loads.name
age   = stu_loads.age
score = stu_loads.score  

print("=== class loads ===", name, age, score) # Lucy 11 100


stu = Student("Devi", 23, 60)
f = open("../model_dumps.txt", "w")
stu_dump = json.dump(stu,f, default=lambda stu : stu.modelToDic())
f.close

f = open("../model_dumps.txt", "r")
stu_load = json.load(f, object_hook=lambda stu_dumps : Student.dicToModel(stu_dumps)) # {"name": "Lucy", "age": 11, "score": 100}
name  = stu_load.name
age   = stu_load.age
score = stu_load.score  

print("=== class load ===", name, age, score) # Devi 23 60













