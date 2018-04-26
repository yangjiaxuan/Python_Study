#!/usr/bin/python3

#coding="utf-8"

print ("============= 开始测试 ==============")

print ("============= 条件语句 开始 ==============")
# 条件语句：
a = 10
if a < 3:
	print ("a 小于3")
else :
	print ("a 大于3")

a = input("你的出生年份：")
a = int(a) # 输入为字符型 转int
if a > 2000:
	print("哇咔咔！ 00 后！")
elif a > 1990:
	print("90后！")
else:
	print("90年以前")



print ("============= 变量 开始 ==============")
# 变量
a = 1
print("整形 a:%d"%a)
b = 1.1
print("浮点型 b:%f"%b)
c  = "哇咔咔"
print("字符 c:%s"%c)
c1 =  "a1 \'有转义\'"
print("字符 c1:%s"%c1)
c2 = r"wakaka"
print("字符 c2:%s"%c2)
c3 = r'''wakaka,
         类似注释 
         拥有换行'''
print("字符 c3:%s"%c3)





print ("============= Unicode 与 字符的互转 开始 ==============")
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
a =  ord('A')
print("A 的 Unicode码：%d"%a)
b = chr(65)
print("Unicode 为 65代表的字符：%s"%b)


print ("============= 字符编码 与 解码  开始 ==============")
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
a = "ABC".encode("ascii")
print("ABC 的 ascii码: %s"%a)
a = "ABC".encode("utf-8")
print("ABC 的 UTF-8码: %s"%a)
a = "中国".encode("utf-8")
print("中国 的 UTF-8码: %s"%a)
# 注： 中文不是 Unicode格式， 中文可以转UTF-8码

a = b"ABC".decode("ascii")
print("b 'ABC'的 ascii 解码为:%s"%a)
a = b'\xe4\xb8\xad\xe5\x9b\xbd'.decode("utf-8")
print("b'\xe4\xb8\xad\xe5\x9b\xbd'的 utf-8 解码为:%s"%a)




print ("============= 数组 开始 ==============")
# 数组
list_ = [10, 2, 13, 4]
# 遍历
for x in list_:
	print("数组遍历：list: %d"%x)
# 增
print("------数组增之前%s------"%list_)
list_.insert(4,5) # 在 index=4 的位置插入 5
print("------数组增之后%s------"%list_)
# 删
list_.pop(3) # 删除 index=3 的元素 如果要删的是最后一个，直接写pop()即可
print("------数组删之后%s------"%list_)
# 改
list_[3] = 10 # 把 index=3 的元素改为 10
print("------数组删之后%s------"%list_)
# 查
a = list_[3]
print("list index=3 的元素为:%s"%a)
# 排序
list_.sort()
print("list 排序后:%s"%list_)





print ("============= 元祖 开始 ==============")
# 元祖
# 注： 元祖一旦创建就不可修改，但是内部如果有 list 的话，list的元素是可以修改的
typle = ("A", "B", ["0", "1"])
print("元祖 %s"%str(typle))

typle[2][1] = "1111"
print("元祖 %s"%str(typle))



print ("============= 字典 开始 ==============")
# 字典
dic = {"1" : "1A", "2" : "2A", "3" : "3A"}
print("字典 dic:%s"%dic)
# 增
dic["6"] = "6A"
print("字典 增之后 dic%s"%dic)
# 删
dic.pop("1")
print("字典 删之后 dic%s"%dic)
#改
dic["2"] = "2B"
print("字典 改之后 dic%s"%dic)
#查 2种方式
a = dic["2"]
a = dic.get("2")
print("键值为 '2' 的value:%s"%a)





print ("============= 集合 开始 ==============")
set_ = set([1,2,3])
print("set value%s"%set_)
# 增
set_.add(6)
print("set 增之后value%s"%set_)
# 删
set_.remove(1)
print("set 删之后value%s"%set_)



