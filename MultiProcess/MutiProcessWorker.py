#!/usr/bin/Python3
#encoding="utf-8"

print("======================= 分布式多进程 =======================")

print("|------------------------ worker ------------------------|")

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的 MyManager
class MyManager(BaseManager):
 	pass


# 由于MyManager只从网上获取 Queue ，所以注册时只提供名字。
MyManager.register("com_masterQueue_ys")
MyManager.register("com_workerQueue_ys")


# 连接服务器 也就是 MultiProcessMaster.py 运行的服务器地址
masterIP = "127.0.0.1"

# 端口和验证码 注意要和 MultiProcessMaster.py 保持一致
manager = MyManager(address=(masterIP, 5000), authkey=b"abc")

# 从网络连接
manager.connect()

# 获取Queue
master = manager.com_masterQueue_ys()
worker = manager.com_workerQueue_ys()

# 从队列中获取 任务数据
for x in range(6):
	try:
		task = master.get(timeout=1)
		print("获取到任务值：",task)
		r = "ret: %d * %d = %d"%(task, task,task * task)
		worker.put(r)
		print("把任务结果返回到 worker 队列")
	except Queue.Empty:
		print("任务已经完成")
	except Exception as e:
		print("=== 异常结束 ===")

print("worker 处理结束！")






