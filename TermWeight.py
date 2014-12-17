#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from DB import DB
from Emails import Emails
from Tokens import Tokens
from Dictionary import Dictionary

class TermWeight:

	_table = 'TermWeight'
	email_id = 0
	term = 1
	tfidf = 2
	classs = 3

	# insert tfidf calculation of a term in a document into term weight table
	# return terms weight array
	@classmethod
	def add_terms_weight(self):
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		email_count = Emails.get_email_count()

		dictionary = Dictionary.fetch_all()

		tokens = Tokens.fetch_token_all()

		for token in tokens:
			tfidf = self.calc_tfidf(email_count, token[Tokens.tf], dictionary[token[Tokens.term]])
			cur.execute("INSERT INTO %s VALUES (%ld, %s, %d, %s)" % (table, token[Tokens.email_id], token[Tokens.term], tfidf, token[Tokens.classs]))

		DB.close(con)

	@classmethod
	def calc_tfidf(self, email_count, tf, df):
		return tf * math.log(email_count / df)

	@classmethod
	def fetch_all(self):
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s" % table)

		rows = cur.fetchall()

		DB.close(con)

		return rows

	@classmethod
	def fetch_term_by_class(self, classs, term):
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("SELECT * FROM %s WHERE class = %s AND term = %s" %(table, classs, term))

		rows = cur.fetchall()

		DB.close(con)

		return rows