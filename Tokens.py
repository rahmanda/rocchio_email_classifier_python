#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
import DB


class Tokens:

	_email_id = 0
	_table = 'tokens'
	_email = null

	# tokenize an email
	def tokenize(self, doc_id):
		email = self._email
		tokens = email.splitlines();

		for token in tokens:
			self._add_token(token)

	# insert a token in a document into token table
	def _add_token(self, token):
		con = DB.connect()
		table = self._table
		email_id = self._email_id
		cur = con.cursor()

		cur.execute("SELECT * FROM %s WHERE term = %s AND email_id = %d" % table, token, email_id)
		term = cur.fetchone()

		if cur.rowcount > 0 :
			cur.execute("UPDATE %s SET tf = tf + 1 WHERE term = %s AND email_id = %d" % table, token, email_id)
		else :
			cur.execute("INSERT INTO %s VALUES (%d, %s, %s, 1)" % table, email_id, token, term['class'])

		DB.close(con)

	def fetch_all(self):
		tokens = {}
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s" % table)
		rows = cur.fetchall()

		for row in rows:
			tokens[row['email_id']][row['token']] = row['tf']

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
