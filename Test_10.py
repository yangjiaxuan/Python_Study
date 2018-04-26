#!/usr/bin/Python3
#encoding="utf-8"


print("======================= 多线程 =======================")
"""
		Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的
	数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统
	自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程
	和子进程内返回。

		子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程
	可以fork出很多子进程，所以，父进程要记下每个子进程的ID(fork时返回的pid)，
	而子进程只需要调用getppid()就可以拿到父进程的ID。

	os.getpid() 获取当前线程 线程ID
	os.getppid() 获取父线程 线程ID

	注：
	 windows 中没有 fork()

"""

import os
pid = 0

# pid = os.fork() # 会调两次，所以注释了

if pid != 0: # 在父线程中返回的 
	# === 父线程(38113) 创建新的子线程(38114) ===
	print("=== 父线程(%d) 创建新的子线程(%d) ==="%(os.getpid(), pid))
else: # 在子线程中返回的
	# === 子线程(38114) 被父线程(38113)创建 ===
	print("=== 子线程(%d) 被父线程(%d)创建 ==="%(os.getpid(), os.getppid()))
print(" ======== fork ========")



from multiprocessing import Process
"""
# 使用 Process 创建线程
"""
def process_run(text):
	print("=== Process === 运行了... %s 当前线程:%s 父线程:%s==="%(text, os.getpid(), os.getppid()))

p = Process(target=process_run, args=("test",))
# === Process === 子线程将要执行 本线程： 38442
print("=== Process === 子线程将要执行 本线程：",os.getpid())
p.start()
# === Process === 运行了... test 当前线程:38443 父线程:38442===
p.join()
# === Process === 子线程执行结束 38442
print("=== Process === 子线程执行结束",os.getpid())



"""
# Pool 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
"""
from multiprocessing import Pool
import os, time, random

def pool_task(taskID):
	start = time.time()
	print("=== pool_task 线程：%s === 开始时间：%d"%(os.getpid(), start))

	time.sleep(random.random() * 3)
	print("执行任务：",taskID)

	end = time.time()
	print("=== pool_task 线程：%s === 结束时间：%d"%(os.getpid(), end))
	print("执行时间：",(end - start))

p = Pool(4)
for i in range(5):
	p.apply_async(pool_task, args=(i,))


print("准备执行子线程程序！")
p.close()
p.join()
print("所有子线程已经执行完毕")
# 准备执行子线程程序！
# === pool_task 线程：38658 === 开始时间：1494832956
# === pool_task 线程：38659 === 开始时间：1494832956
# === pool_task 线程：38660 === 开始时间：1494832956
# === pool_task 线程：38661 === 开始时间：1494832956
# 执行任务： 1
# === pool_task 线程：38659 === 结束时间：1494832957
# 执行时间： 1.2386257648468018
# === pool_task 线程：38659 === 开始时间：1494832957
# 执行任务： 0
# === pool_task 线程：38658 === 结束时间：1494832958
# 执行时间： 1.674133062362671
# 执行任务： 2
# === pool_task 线程：38660 === 结束时间：1494832959
# 执行时间： 2.8070361614227295
# 执行任务： 3
# === pool_task 线程：38661 === 结束时间：1494832959
# 执行时间： 2.991152763366699
# 执行任务： 4
# === pool_task 线程：38659 === 结束时间：1494832959
# 执行时间： 1.9476888179779053
# 所有子线程已经执行完毕

"""
	代码分析：
	对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调
用close()，调用close()之后就不能继续添加新的Process了。

	请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task
完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。
这是Pool有意设计的限制，并不是操作系统的限制。如果改成：

	p = Pool(5)
	就可以同时跑5个进程。

	由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才
能看到上面的等待效果。

"""


"""
	子进程

	很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程
输入和输出。
	subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
"""

import subprocess
print("准备启动一个子线程！")

p = subprocess.call(["nslookup", 'www.python.org'])

print("退出子线程！", p)
# 准备启动一个子线程！
# Server:		192.168.1.1
# Address:	192.168.1.1#53

# Non-authoritative answer:
# www.python.org	canonical name = python.map.fastly.net.
# Name:	python.map.fastly.net
# Address: 151.101.76.223

# 退出子线程！ 0


"""
	如果需要输入！
"""

print("准备启动一个子线程 ====== 2")

p = subprocess.Popen(['nslookup'], 
					 stdin=subprocess.PIPE, 
					 stdout=subprocess.PIPE, 
					 stderr=subprocess.PIPE)

out ,err = p.communicate(b"set q=mx\npython.org\nexit\n")
# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：
# set q=mx
# python.org
# exit

print(out.decode('utf-8'))
print("Exit code:", p.returncode)

# 准备启动一个子线程 ====== 2
# Server:		192.168.1.1
# Address:	192.168.1.1#53

# Non-authoritative answer:
# python.org	mail exchanger = 50 mail.python.org.

# Authoritative answers can be found from:

# Exit code: 0




"""
	进程间通信

	Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种
方式来交换数据。
"""
from multiprocessing import Queue

# 使用 Queue 进行进程间通讯
# 写数据进程 执行的代码
def writeFunc(queue):

	print("写进程 进程ID,",os.getpid())
	for x in ["A", "B", "C"]:
		queue.put(x)
		time.sleep(random.random())

def readFunc(queue):

	print("读进程 进程ID",os.getpid())
	while True:
		value = queue.get(True)
		print("读进程读到数据了",value)


# 创建Queue
q = Queue()

writeProcess = Process(target=writeFunc, args=(q,))
readProcess  = Process(target=readFunc, args=(q,))

# 启动子进程writeProces 写入：
writeProcess.start()

# 启动子进程readProcess 读取：
readProcess.start()

# 等待writeProcess结束
writeProcess.join()

# pr进程里是死循环，无法等待其结束，只能强行终止:
readProcess.terminate()

# 写进程 进程ID, 39604
# 读进程 进程ID 39595
# 读进程读到数据了 A
# 读进程读到数据了 B
# 读进程读到数据了 C






print("====================== 多线程 ========================")
"""
	进程是由若干线程组成的，一个进程至少有一个线程。

	由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，
Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线
程。

	Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，
threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用
threading这个高级模块。
"""

import time, threading
# 新线程执行的代码
def loop():
	print("==线程：%s 开始执行=="%threading.current_thread().name)
	n = 0
	while n<5:
		n += 1
		print("子线程：%s 编号：%d 正在执行..."
			  %(threading.current_thread().name, n))
	print("==线程：%s 执行结束=="%threading.current_thread().name)


print("=== 多线程 === 当前线程：",threading.current_thread().name)

t = threading.Thread(target=loop, name="LoopThread")
print("=== 多线程 === 子线程：%s 准备执行！"%t.name)

t.start()
t.join()

print("=== 多线程 === 子线程：%s 执行结束！"%t.name)

# === 多线程 === 当前线程： MainThread
# === 多线程 === 子线程：LoopThread 准备执行！
# ==线程：LoopThread 开始执行== 
# 子线程：LoopThread 编号：1 正在执行...
# 子线程：LoopThread 编号：2 正在执行...
# 子线程：LoopThread 编号：3 正在执行...
# 子线程：LoopThread 编号：4 正在执行...
# 子线程：LoopThread 编号：5 正在执行...
# ==线程：LoopThread 执行结束==
# === 多线程 === 子线程：LoopThread 执行结束



"""
	Lock:
	多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个
进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以
被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，
把内容给改乱了。
"""

def saleTickets(n):
	
	if n > 0:
		n -= 1
		print("线程：%s 卖掉一张票，剩余 %d 张"%(threading.current_thread().name, n))
		return n
	else:
		return -1

lock = threading.Lock()

def forSale():
	global ticketsNum
	while True:
		lock.acquire() # 获取锁
		ticketsNum = saleTickets(ticketsNum)
		lock.release() # 用完释放

		if ticketsNum == -1:
			ticketsNum = 0
			break

ticketsNum = 100

t1 = threading.Thread(target=forSale, name="sale_01")
t2 = threading.Thread(target=forSale, name="sale_02")
# 如果函数有参数 例子为两个参数
# t2 = threading.Thread(target=forSale, name="sale_02",args=(a,b,))
t1.start();
t2.start();

t1.join()
t2.join()

print("剩余票数：",ticketsNum)





"""
	启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，
也就是仅使用了一核。

	但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，
8核就跑到800%，为什么Python不行呢？

	因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global 
Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字
节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的
执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU
上，也只能用到1个核。

	GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，
要真正利用多核，除非重写一个不带GIL的解释器。

	所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多
线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

	不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程
实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

"""

import multiprocessing
# 获取当前 CPU 内核数量：
multiprocessing.cpu_count()






print("======================== ThreadLocal =====================")
"""
	ThreadLocal: threading.local()
		可以绑定线程，成为线程中的全部变量，不同线程之间的数据是不一样的。
	可以把 Threading.local() 想象成线程的局部变量，在该线程中是全局的，
	不同线程之间也就不会一样了。
"""
class Student(object):
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name 
		
local = threading.local()
def process_student():
	# 从当前线程中获取绑定的对象
	std = local.student 
	print("student:%s 当前线程:%s"%(std.name, threading.current_thread().name))

def process_thread(std):
	# 把 std 绑定给当前线程
	local.student = std
	process_student()

std1 = Student("Tom")
std2 = Student("Lucy")
t1 = threading.Thread(target=process_thread, name="thread_01", args=(std1,))
t2 = threading.Thread(target=process_thread, name="thread_02", args=(std2,))

t1.start()
t2.start()

# student:Tom 当前线程:thread_01
# student:Lucy 当前线程:thread_02



"""
	我们介绍了多进程和多线程，这是实现多任务最常用的两种方式。现在，我们来讨论一下这
两种方式的优缺点。

	首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，
Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。
如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。
如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。
多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。
（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名
的Apache最早就是采用多进程模式。

	多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在
Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和
CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。

	多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是
任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。在Windows上，
果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将
关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。

	在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。
由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。为了缓解这个问题，IIS和Apache
在又有多进程+多线程的混合模式，真是把问题越搞越复杂。

	线程切换

	无论是多进程还是多线程，只要数量一多，效率肯定上不去，为什么呢？

	我们打个比方，假设你不幸正在准备中考，每天晚上需要做语文、数学、英语、物理、化学
这5科的作业，每项作业耗时1小时。

	如果你先花1小时做语文作业，做完了，再花1小时做数学作业，这样，依次全部做完，一共
5小时，这种方式称为单任务模型，或者批处理任务模型。

	假设你打算切换到多任务模型，可以先做1分钟语文，再切换到数学作业，做1分钟，再切换
英语，以此类推，只要切换速度足够快，这种方式就和单核CPU执行多任务是一样的了，以幼儿园
小朋友的眼光来看，你就正在同时写5科作业。

	但是，切换作业是有代价的，比如从语文切到数学，要先收拾桌子上的语文书本、钢笔
（这叫保存现场），然后，打开数学课本、找出圆规直尺（这叫准备新环境），才能开始做数学作
业。操作系统在切换进程或者线程时也是一样的，它需要先保存当前执行的现场环境（CPU寄存器
状态、内存页等），然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），
才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，操作
系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，
点窗口无反应，系统处于假死状态。

	所以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务
都做不好。

	计算密集型 vs. IO密集型

	是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型。

	计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行
高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越
多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算
密集型任务同时进行的数量应当等于CPU的核心数。

	计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本
语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

	第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的
特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存
的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都
是IO密集型任务，比如Web应用。

	IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速
度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。对于IO密
集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

	异步IO

	考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，
单进程单线程模型会导致别的任务无法并行执行，因此，我们才需要多进程模型或者多线程模型来
支持多任务并发执行。

	现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操
作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件
驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地
支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。
由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务
是一个主要的趋势。

	对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件
驱动编写高效的多任务程序。我们会在后面讨论如何编写协程。
"""




