#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json

class DBConnect:
	# configuration to connect database
	__server = 'localhost'
	__user = 'root'
	__password = 'ambercat'
	__db = 'imail'

	# connect to database
	# return connection
	def connect(self):
		try:
			con = mdb.connect(self.__server, self.__user, __password, __db)
			return con
		except: _mysql.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])

	# close connection to database
	def close(self, con):
		con.close()

	def set_config(self, server, user, password, db):
		self.__server = server
		self.__user = user
		self.__password = password
		self.__db = db

	def reset_config():
		self.__server = 'localhost'
		self.__user = 'root'
		self.__password = 'ambercat'
		self.__db = 'imail'
