#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
import DBConnect

class Dictionary:

	_table = 'dictionary'
	_con = null

	def __init__(self):
		self._con = DBConnect()

	# insert a term into dictionary table group by document id
	def add_dictionary(self, term):
		self._con.connect()

		table = self._table
		cur = self._con.cursor()

		cur.execute("SELECT * FROM %s WHERE term = %s" % table, term)

		if cur.rowcount > 0 :
			cur.execute("UPDATE %s SET df = df + 1 WHERE term = %s" % table, term)
		else :
			cur.execute("INSERT INTO %s VALUES (%s, 1)" % table, term)

		self._con.close()

	# get dictionary table and transform into array key structure
	# for easier access to df value
	# return dicts array
	def fetch_all(self):
		df = {}
		self._con.connect()
		table = self._table
		cur = self._con.cursor()

		cur.execute("SELECT * FROM %s" % table)
		rows = cur.fetchall()

		for row in rows:
			df[row['term']] = row['df'];

		self._con.close()

		return df