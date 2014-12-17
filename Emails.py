#!/usr/bin/python
# -*- coding: utf-8 -*-
from DB import DB

class Emails:
	_table = 'emails'
	email_id = 0
	recipient = 1
	email = 2
	classs = 3

	@classmethod
	def add_email(self, email, classs):
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("INSERT INTO %s VALUES ("+"'"+email+"','"+classs+"'")

		DB.close(con)

	@classmethod
	def get_email_count(self):
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s" % table)

		count = cur.rowcount

		DB.close(con)

		return count

	@classmethod
	def fetch_by_recipient(self, recipient):
		emails = {}
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s WHERE to = %s" % (table, recipient))

		rows = cur.fetchall()
		for row in rows:
			emails[row[email_id]] = row[email]

		DB.close(con)
		return emails

	@classmethod
	def fetch_by_class(self, classs):
		emails = {}
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s WHERE class = %s" % (table, classs))

		rows = cur.fetchall()

		for row in rows:
			emails[row[email_id]] = row[email]

		DB.close(con)
		return emails