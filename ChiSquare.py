#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
import DB
import math
import Tokens

class ChiSquare:
	
	_con = null
	_table = 'chisquare'

	@classmethod
	def calculate_chi_square(self, term, class):
		N = Tokens.get_count_email()
		a = Tokens.get_count_term_on_class(term, class)
		b = Tokens.get_count_term_not_on_class(term, class)
		c = Tokens.get_count_not_term_on_class(term, class)
		d = Tokens.get_count_not_term_not_on_class(term, class)

		nom = (N * (A * D - B * C) * (A * D - B * C))
		denom = ((A + C) *  (B + D) * (A + B) * (C + D))

		chi_square = nom / denom  

		return chi_square

	@classmethod
	def add_chi_square(self, chi_square)
		
	