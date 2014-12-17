#!/usr/bin/python
# -*- coding: utf-8 -*-
from DB import DB
from TermWeight import TermWeight 


class Centroids:

	_table = 'centroids'
	term = 0
	classs = 1
	centroid = 2

	@classmethod
	def add_centroid(self, term, classs):
		centroid = self.calc_centroid(term, classs)

		con = DB.connect()
		cur = con.cursor()
		table = self._table

		cur.execute("INSERT INTO %s VALUES (%s, %s, %f)" % (table, term, classs, centroid))

		DB.close(con)

	@classmethod
	def update_centroid(self, term, classs):
		centroid = self.calc_centroid(term, classs)

		con = DB.connect()
		cur = con.cursor()
		table = self._table

		count = self.get_count_centroid(term, classs)

		if count > 0:
			cur.execute("UPDATE %s SET centroid = %f WHERE term = %s AND class = %s" % (table, centroid, classs))
		else:
			cur.execute("INSERT INTO %s VALUES (%s, %s, %f)" % (table, term, classs, centroid))

		DB.close(con)

	@classmethod
	def get_count_centroid(self, term, classs):
		con = DB.connect()
		cur = con.cursor()
		table = self._table

		rows = cur.execute("SELECT * FROM %s WHERE term = %s AND class = %s" % (table, term, classs))

		count = rows.rowcount

		return count

	@classmethod
	def calc_centroid(self, term, classs):
		sums = 0.0
		count = 0
		con = DB.connect()
		cur = con.cursor()
		table = self._table

		term_weight = TermWeight.fetch_term_by_class(classs, term)

		if term_weight != null:
			for item in term_weight:
				sums = sums + term_weight[TermWeight.tfidf]
				count++
		else:
			return sums

		avg = sums / count

		DB.close(con)

		return avg

