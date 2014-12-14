#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
import DBConnect


class Centroids:

	_table = 'centroids'
	_con = null

	def __init__(self):
		self._con = DBConnect()

	def calc_centroid(self, terms):

