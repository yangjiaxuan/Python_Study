#!/usr/bin/python3
#encoding="utf-8"

print("======================= 开始测试 ====================")
print(" |--1--| ============== 面向对象 start =================")
class Student(object):


	# 注意 第一个参数永远是 self
	def __init__(self, name, score):
		self.name  = name
		self.score = score
	def description(self):
		return "name:%s score:%s"%(self.name, self.score)
		

lili = Student("lili", 89)
print("lili 名字:",lili.name)
# ------ 面向对象 lili_desc : name:lili score:89
print("------ 面向对象 lili_desc :",lili.description())

xiaohua = Student("xiaohua", 100)
print("xiaohua 名字:",xiaohua.name)
# ------ 面向对象 xiaohua_desc : name:xiaohua score:100
print("------ 面向对象 xiaohua_desc :",xiaohua.description())

"""
		双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
	不能直接访问__name是因为Python解释器对外把__name变量改成了
	_Student__name，所以，仍然可以通过_Student__name来访问__name
	变量。

		在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以
	双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
	,所以，定义私有变量时，不能用__name__、__score__这样的变量名。
"""






print(" |--2--| ============== 面向对象 权限 start =================")
# 如果类内部的属性不希望被外部访问话，可以在属性的前面加上两个下划线 "__"
class Animal(object):
# Animal 继承与 Object
	def __init__(self, name):
		self.__name = name
	def getName(self):
		return self.__name

	def speak(self):
		return ""

class Cat(Animal):
# Cat 继承与 Animal
	def __init__(self):
		# 调用父类的初始化方法，然后再调用他的 init
		super(Cat, self).__init__("cat")
	def speak(self):
		return "喵喵..."
		
animal = Animal("cat")
# animal.__name 会报没有这个属性
# ------- 权限 ----- animal:name= cat
print("------- 权限 ----- animal:name=",animal.getName())

cat = Cat()
# ------- 权限 ----- cat:name= cat
print("------- 权限 ----- cat:name=",cat.getName())
# ------- 权限 ----- cat.speak(): 喵喵...
print("------- 权限 ----- cat.speak():",cat.speak())

class Robot(object):

	def __init__(self):
		super(Robot, self).__init__()
	def speak(self):
		return "编号89757！..."
		

# 此处在调用的时候，animal 不一定非要传一个 Animal类型或其子类类型的，
# 只需要该对象有speak方法即可。
# Python像OC一样是动态的语言，不像swift是非动态的
def speak(animal):
	return animal.speak()

robot = Robot()
# ---------- 权限 -------- robot speak: 编号89757！...
print("---------- 权限 -------- robot speak:",robot.speak())








print(" |--3--| ============== 获取对象信息 start =================")
# 对于一般类型 使用 type() 函数就可以了，
# 但对于类就不太方便，类使用 isinstance()
bool_ = type(123)  == int   # True
bool_ = type(12.3) == float # True
bool_ = type("123") == str  # True

import types
bool_ = type(speak) == types.FunctionType # True
bool_ = type(abs)   == types.BuiltinFunctionType # True
bool_ = type(lambda x,y:x) == types.LambdaType # True
bool_ = type((x for x in range(1,10)))== types.GeneratorType # True

# None 其实是一个 class
print(type(None)) # <class 'NoneType'>

bool_ = isinstance(cat, Cat) # True
bool_ = isinstance(animal, Cat) # False
bool_ = isinstance(cat, (Cat, Animal)) # True

# cat 是否包含 __name 属性
bool_ = hasattr(cat, '__name')  # False
# 虽然 __name被私有化了，其实他只是被转化为了 _类名+私有变量名
bool_ = hasattr(cat, '_Animal__name') # True
# 获取对象属性信息
name_ = getattr(cat, '_Animal__name') # cat
# 设置对象属性信息
bool_ = setattr(cat, '_Animal__name', "super cat")
name_ = getattr(cat, '_Animal__name') # super cat

print(" --- 获取对象信息 --- name_",name_)

print(" --- 获取对象信息 --- bool_",bool_)








print(" |--4--| ============== 类属性 和 实例属性 start =================")
"""
	类属性  : 在类内部添加，通过类创建的对象都拥有类属性
	实例属性 ：在对象创建时，专门为对象添加的属性，其他对象不会拥有该属性。
"""
class Shap(object):
	def __init__(self, sideNum):
		super(Shap, self).__init__()
		# 在类中添加的属性焦作类属性
		self.sideNum = sideNum
		
shap_1 = Shap(3)
# 这是在类外添加的焦作 实例属性
shap_1.lineW = 1

# shap_2 不具备linew属性
shap_2 = Shap(4)



