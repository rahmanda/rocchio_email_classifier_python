#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
import DB
import math

class TermWeight:

	_table = 'TermWeight'

	# insert tfidf calculation of a term in a document into term weight table
	# return terms weight array
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
			tfidf = self._calc_tfidf(email_count, token['tf'], dicts[token['term']])
			cur.execute("INSERT INTO %s VALUES (%d, %s, %d)" % table, token['email_id'], token['term'], tfidf)

	def _calc_tfidf(email_count, tf, df):
		return tf * math.log(email_count / df)

	def fetch_all(self):
		# TODO
