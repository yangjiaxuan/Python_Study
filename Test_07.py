#!/usr/bin/Python3
#encoding="utf-8"


print(" |--1--| ============== 使用__slots__ start =================")
"""
		当我们定义了一个class，创建了一个class的实例后，我们可以给该实例
	绑定任何属性和方法，这就是动态语言的灵活性。
		在python中，我们可以动态给对象绑定属性，绑定方法。
"""
class Animal(object):
	def __init__(self):
		super(Animal, self).__init__()

class Cat(Animal):
	def __init__(self):
		super(Cat, self).__init__()

		
cat = Cat()
# 绑定属性
cat.name = "小花"  # 小花

from types import MethodType

def set_Name(self, name):
	self.name = name

# 绑定方法
cat.setName = MethodType(set_Name, cat)

cat.setName("可爱小花") # cat.name  可爱小花


"""
	当我们希望对一个类进行限制，不希望随便加属性 或者 方法，这是可以使用 __slots__
	eg : 
		__slots__ = ('name', 'age')
	允许绑定 name 和 age 属性


	注意： 
		这个类必须是继承于 object,否则将限定失败。
"""


class Dog(Animal):

	# 只希望拥有一个 name 属性，如果类内部没有声明，则外部可以追加。
	__slots__ = ('name')
	def __init__(self):
		super(Dog, self).__init__()

dog = Dog()
dog.name = "xzp" # xzp
dog.age  = 11    # 由于Dog的父类是Animal,所以绑定成功  11


print(" |--1--| dog.age",dog.age)






print(" |--2--| ============== 使用@property start =================")
"""
	set get 方法，是在我们的属性不希望外面随便更改，要求更改的时候要满足一定的条件才行。
	这时，把属性隐藏起来，监听 set方法，就很有效了。
"""
class Cat(Animal):

	def __init__(self):
		super(Cat, self).__init__()

	@property    # get 方法
	def legs(self):
		return self._legs

	@legs.setter # set 方法
	def legs(self, legs_):
		self._legs = legs_

	@property
	def type(self):
		return "cat"
	
	
cat = Cat()
# 有没有很爽，像OC一样设置属性 调用属性值
cat.legs = 4  # 4
# cat.type = "super cat" 由于仅有只读属性，所以不能设置
print(" |--2--| cat.legs",cat.legs,"cat.type",cat.type)









print(" |--3--| ============== 多继承 start =================")

class Runable(object):
	def __init__(self):
		super(Runable, self).__init__()
	def run(self):
		return "开始跑了..."
		
class Flyable(object):
	def __init__(self):
		super(Flyable, self).__init__()
	def fly(self):
		return "天啊，我飞起来了..."

class Bird(Runable, Flyable):
	def __init__(self):
		super(Bird, self).__init__()

bird = Bird()
bird.name = "我是一只小小小鸟🐦"
# |--3--| 我是一只小小小鸟🐦 开始跑了...
print(" |--3--| %s %s"%(bird.name, bird.run()))
# |--3--| 我是一只小小小鸟🐦 天啊，我飞起来了...
print(" |--3--| %s %s"%(bird.name, bird.fly()))







print(" |--4--| ============== 定制类 start =================")
"""
	__slots__ : 限定属性
	__len__() : 为了能让class作用于len()函数。
	__str__() : 类似于 OC中的 description方法 可以在打印的时候，显示定制的内容
	__repr__(): 不使用print() 直接使用 显示时 可以显示定制内容
	__iter__(): 把对象变成可迭代的,可以被 for 循环遍历 再循环的过程中会调用__next__()

	__getitem__(): __iter__()只是让对象可以迭代，但并不可以根据index去取值
				   __getitem__() 可以实现这种需求,同时，也可以实现切片功能。

	__getattr__(): 正常情况下，获取属性时，如果没有这个属性就会报错，这个方法和已监听
				   所有 不存在 属性的调用，在这个函数可以对没有的属性进行补救。
"""
class A(object):

	def __init__(self):
		super(A, self).__init__()
		self.a = 0
		self.b = 1
	def __len__(self):
		return 10

	def __str__(self):
		return "A len:%d"%len(self)

	__repr__ = __str__

	def __iter__(self):
		return self

	def __next__(self):
		# 赋值 类似于 a,b = 1,2 即 a=1 b=2
		self.a, self.b = self.b, self.a + self.b
		if self.a > 50: # 退出迭代条件
			raise StopIteration() # 不可迭代了，到头了
		else:
			return self.a

	def __getitem__(self, index):
		if isinstance(index, int):
			a,b = 0,1
			for x in range(0,index+1):
				a,b = b, a+b
			return a
		
		# 如果是切片 此处切片并没有对 负数做处理，也没对[:2:3]这种情况做处理
		elif isinstance(index, slice):
			start = index.start
			stop  = index.stop
			if start == None:
				start = 0
			if stop == None:
				stop = 100
			L = []
			for index_r in range(start,stop):
				v = self[index_r]
				L.append(v)
			return L
		
		return None

	def __getattr__(self, attr):
		if attr == "score":
			return 100
		else:
			return None
	

a = A()
# a : A len:10
print(" |--4--| a :",a)

#  1 1 2 3 5 8 13 21 34
for x in a:
	print("",x)
# 3
print(" |--4--| a[3] :",a[3])
# [1, 1, 2]
print(" |--4--| a[:5] :",a[:3])
# 100
print(" |--4--| a.score :",a.score)
a.score = 98
# 98 上面已经添加了属性
print(" |--4--| a.score :",a.score)



print(" |--5--| ============== 使用枚举类 start =================")

"""
	定义一个月份的class类型，然后，每个常量都是class的一个唯一实例！
"""
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
					   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name ,member in Month.__members__.items():
	print(" |--5--| name:%s member:%s"%(name, member))
"""
	name:Jan member:Month.Jan
	name:Feb member:Month.Feb
	name:Mar member:Month.Mar
	name:Apr member:Month.Apr
	name:May member:Month.May
	name:Jun member:Month.Jun
	name:Jul member:Month.Jul
	name:Aug member:Month.Aug
	name:Sep member:Month.Sep
	name:Oct member:Month.Oct
	name:Nov member:Month.Nov
	name:Dec member:Month.Dec
"""

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique

# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weak(Enum):
	Sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day_01 = Weak.Sun
# Weak.Sun
print(" |--5--| day_01 ",day_01)
# 0
print(" |--5--| day_01.value ",day_01.value)

day_02 = Weak["Mon"]
# Weak.Mon
print(" |--5--| day_02 ",day_02)	

day_03 = Weak(3)
# Weak.Wed
print(" |--5--| day_03 ",day_03)	







print(" |--6--| ============== 使用元类 start =================")
"""
		动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，
	而是运行时动态创建的。
		
"""

a = A()

type_ = type(A)
# |--6--| type(A): <class 'type'>
print(" |--6--| type(A):",type_)
type_ = type(a)
# |--6--| type(a): <class '__main__.A'>
print(" |--6--| type(a):",type_)

"""
	type()函数可以查看一个类型或变量的类型。
	A是一个class，它的类型就是type，而a是一个实例，它的类型就是class A。
	class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

	要创建一个class对象，type()函数依次传入3个参数：

	1、class的名称；
	2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，
	   别忘了tuple的单元素写法；
	3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名A上。

	   通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇
	到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出
	class。

	metaclass
	除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

	metaclass，直译为元类，简单的解释就是：
		当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后
	创建实例。

	   按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这
	是一个metaclass：
"""

# metaclass是类的模板，所以必须从`type`类型派生：
class BaseMetaclass(type):

	def __new__(cla, name, bases, attrs):
		attrs['add'] = lambda self, value:self.append(value)
		return type.__new__(cla,name,bases,attrs)
"""
	cla:   当前准备创建的类的对象；
	name:  类的名字；
	bases: 类继承的父类集合；
	attrs: 类的方法集合。
"""

"""
		有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来
	定制类，传入关键字参数metaclass。
"""

# 继承于 list 同时指向：metaclass
class MyList(list, metaclass=BaseMetaclass):
	pass

list_ = MyList()
list_.add(1) # [1]
print(" |--6--| list_",list_)		


"""
		ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据
	库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作
	SQL语句。

		要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构
	定义出对应的类来。
"""

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		if name=='Model':
		    return type.__new__(cls, name, bases, attrs)
		print('Found model: %s' % name)
		mappings = dict()
		for k, v in attrs.items():
		    if isinstance(v, Field):
		        print('Found mapping: %s ==> %s' % (k, v))
		        mappings[k] = v
		for k in mappings.keys():
		    attrs.pop(k)
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		attrs['__table__']    = name # 假设表名和类名一致
		return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
	# 定义类的属性到列的映射：
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()







