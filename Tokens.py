#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
from DB import DB


class Tokens:

	_table = 'tokens'
	# list of constants that represents fields on the table
	email_id = 0
	term = 1
	tf = 2
	class = 3

	# tokenize an email
	@classmethod
	def tokenize(self, email, class):
		tokens = email.splitlines()

		for token in tokens:
			self.add_token(token, class)

	# insert a token in a document into token table
	@classmethod
	def add_token(self, token, class):
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s WHERE term = %s AND class = %s" % table, token, class)
		term = cur.fetchone()

		if cur.rowcount > 0 :
			cur.execute("UPDATE %s SET tf = tf + 1 WHERE term = %s AND email_id = %ld" % table, token, term[email_id])
		else :
			cur.execute("INSERT INTO %s VALUES (%d, %s, 1)" % table, token, term[class])

		DB.close(con)

	@classmethod
	def fetch_all(self):
		tokens = {}
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s" % table)
		rows = cur.fetchall()

		for row in rows:
			tokens[row[email_id]][row[token]] = row[tf]

		DB.close(con)

		return tokens

	@classmethod
	def get_count_term_on_class(self, term, class):
		con = DB.connect()
		cur = con.cursor()
		cur.execute("SELECT * FROM %s WHERE term = %s AND class = %s" % self._table, term, class)

		count = cur.rowcount

		DB.close(con)

		return count

	@classmethod
	def get_count_term_not_on_class(self, term, class):
		con = DB.connect()
		cur = con.cursor()
		cur.execute("SELECT * FROM %s WHERE term = %s AND class != %s" % self._table, term, class)

		count = cur.rowcount

		DB.close(con)

		return count

	@classmethod
	def get_count_not_term_on_class(self, term, class):
		con = DB.connect()
		cur = con.cursor()
		cur.execute("SELECT * FROM %s WHERE term != %s AND class = %s" % self._table, term, class)

		count = cur.rowcount

		DB.close(con)

		return count

	@classmethod
	def get_count_not_term_not_on_class(self, term, class):
		con = DB.connect()
		cur = con.cursor()
		cur.execute("SELECT * FROM %s WHERE term != %s AND class != %s" % self._table, term, class)

		count = cur.rowcount

		DB.close(con)

		return count

	@classmethod
	def get_count_email(self):
		con = DB.connect()
		cur = con.cursor()
		cur.execute("SELECT * FROM %s" % self._table)

		count = cur.rowcount

		DB.close(con)

		return count
