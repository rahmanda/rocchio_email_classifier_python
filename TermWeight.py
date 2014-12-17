#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
import math
from DB import DB

class TermWeight:

	_table = 'TermWeight'

	# insert tfidf calculation of a term in a document into term weight table
	# return terms weight array
	@classmethod
	def add_terms_weight(self):
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM emails") 
		email_count = cur.rowcount

		dicts = get_dicts(con) #what is this

		cur.execute("SELECT * FROM tokens");
		tokens = cur.fetchall()

		for token in tokens:
			tfidf = self.calc_tfidf(email_count, token['tf'], dicts[token['term']])
			cur.execute("INSERT INTO %s VALUES (%d, %s, %d)" % table, token['email_id'], token['term'], tfidf)

	def calc_tfidf(self, email_count, tf, df):
		return tf * math.log(email_count / df)

	def fetch_all(self):
		# TODO
