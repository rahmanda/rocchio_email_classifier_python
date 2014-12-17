#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import Tokens
from DB import DB

class ChiSquare:
	
	_table = 'chisquare'
	email_id = 0
	term = 1
	chi_square = 2

	@classmethod
	def calculate_chi_square(self, term, classs):
		N = Tokens.get_count_email()
		a = Tokens.get_count_term_on_class(term, classs)
		b = Tokens.get_count_term_not_on_class(term, classs)
		c = Tokens.get_count_not_term_on_class(term, classs)
		d = Tokens.get_count_not_term_not_on_class(term, classs)

		nom = (N * (A * D - B * C) * (A * D - B * C))
		denom = ((A + C) *  (B + D) * (A + B) * (C + D))

		chi_square = nom / denom  

		return chi_square

	@classmethod
	def add_chi_square(self, chi_square, email_id, token):
		con = DB.connect()
		table = self._table
		cur = con.cursor()

		cur.execute("INSERT INTO %s VALUES (%ld, %s, %f)" % (table, email_id, token, chi_square))

		DB.close(con)