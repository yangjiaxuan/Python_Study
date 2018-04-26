#!/usr/bin/Python3
#encoding="utf-8"

print("======================= 分布式多进程 =======================")

print("|------------------------ master ------------------------|")

"""
	在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process
可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

	Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多
进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网
络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式
多进程程序。

	举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，
由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎
么用分布式进程实现？

	原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就
可以让其他机器的进程访问Queue了。

	我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里
面写入任务：
"""

import random, time, queue 
from multiprocessing.managers import BaseManager
class MyManager(BaseManager):
	pass
	# def __init__(self):
	# 	super(MyManager, self).__init__()

# 发送任务的队列
master_queue = queue.Queue()
# 接受任务的队列
worker_queue = queue.Queue()

# 把两个Queue都注册到网络上 callable 关联 queue 对象
MyManager.register("com_masterQueue_ys", callable=lambda : master_queue)
MyManager.register("com_workerQueue_ys", callable=lambda : worker_queue)

# 绑定端口5000，验证码为 abc
manager = MyManager(address=("", 5000), authkey=b"abc")

# 启动queue
manager.start()

# 获得通过网络获得的 queue 对象
master = manager.com_masterQueue_ys()
worker = manager.com_workerQueue_ys()

# 发放任务
for x in range(0, 6):
	n = random.randint(1, 1000)
	print("=== 放进了一个数字： ===",n)
	master.put(n)

print("=== 等待返回结果数据。。。 ===\r\n")

# 从 result 队列中读取任务
for x in range(0,6):
	ret = worker.get(timeout=10)
	print("=== 结果： %s ==="%ret)

# 关闭
manager.shutdown()
print("=== master 已关闭 ===")



"""
	当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式
多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过
了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添
加。

	先启动 MultiProcessMaster.py  然后再启动 MultiProcessWorker.py
"""



"""
	执行过程：

	1： 执行了  MultiProcessMaster.py 会根据延时 10s, 在这期间未获取就会报错

		|------------------------ master ------------------------|
		=== 放进了一个数字： === 400
		=== 放进了一个数字： === 832
		=== 放进了一个数字： === 73
		=== 放进了一个数字： === 969
		=== 放进了一个数字： === 508
		=== 放进了一个数字： === 636
		=== 等待返回结果数据。。。 ===


	2：执行了 MultiProcessWorker.py

		|------------------------ worker ------------------------|
		获取到任务值： 400
		把任务结果返回到 worker 队列
		获取到任务值： 832
		把任务结果返回到 worker 队列
		获取到任务值： 73
		把任务结果返回到 worker 队列
		获取到任务值： 969
		把任务结果返回到 worker 队列
		获取到任务值： 508
		把任务结果返回到 worker 队列
		获取到任务值： 636
		把任务结果返回到 worker 队列
		worker 处理结束


	3：执行了MutiProcessWoker.py 后， 它会把返回数据抛回来，
	   MultiProcessMaster.py 接收到数据 立马执行接下来的数据。

	   这是在 MultiProcessMaster.py
	   
	    === 结果： ret: 400 * 400 = 160000 ===
		=== 结果： ret: 832 * 832 = 692224 ===
		=== 结果： ret: 73 * 73 = 5329 ===
		=== 结果： ret: 969 * 969 = 938961 ===
		=== 结果： ret: 508 * 508 = 258064 ===
		=== 结果： ret: 636 * 636 = 404496 ===
		=== master 已关闭 ===
"""

























