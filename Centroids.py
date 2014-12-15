#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
import DB


class Centroids:

	_table = 'centroids'

	def calc_centroid(self, terms):

