#!/usr/bin/Python3
#encoding="utf-8"

class Dict(dict):

	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError("在Dict中没有找到 %s 键对应的值"%key)

	def __setattr__(self, key, value):
		self[key] = value
