#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
import DBConnect


class Tokens:

	_email_id = 0
	_table = 'tokens'
	_con = null
	_email = null

	def __init__(self):
		self._con = DBConnect()

	# tokenize an email
	def tokenize(self):
		email = self._email
		tokens = email.splitlines();

		for token in tokens:
			self._add_token(token)

	# insert a token in a document into token table
	def _add_token(self, token):
		con = self._con
		table = self._table
		email_id = self._email_id
		cur = con.cursor()

		cur.execute("SELECT * FROM %s WHERE term = %s AND email_id = %d" % table, token, email_id)

		if cur.rowcount > 0 :
			cur.execute("UPDATE %s SET tf = tf + 1 WHERE term = %s AND email_id = %d" % table, token, email_id)
		else :
			cur.execute("INSERT INTO %s VALUES (%d, %s, 1)" % table, email_id, token)

		con.close()

	def fetch_all(self):
		tokens = {}
		con = self._con
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s" % table)
		rows = cur.fetchall()

		for row in rows:
			tokens[row['email_id']][row['token']] = row['tf']

		con.close()

		return tokens
