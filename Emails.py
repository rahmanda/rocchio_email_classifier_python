#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
from DB import DB

class Emails:
	_table = 'emails'
	email_id = 0
	

	@classmethod
	def add_email(self, email, class):
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("INSERT INTO %s VALUES ("+"'"+email+"','"+class+"'")

		DB.connect(con)