#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import json
import MySQLdb as mdb # need to install plugin first

# configuration to connect database
__server = 'localhost'
__user = 'root'
__password = 'ambercat'
__db = 'imail'

# connect to database
# return connection
def connect_db(server, user, password, db):
	try:
		con = mdb.connect(server, user, password, db)
		return con
	except: _mysql.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])

# close connection to database
def close_db(con):
	con.close()

# tokenize an email
def tokenize(email_JSON, doc_id):
	con = connect_db(__server, __user, __password, __db)
	email = json.loads(email_JSON)
	tokens = email.splitlines();
	for token in tokens:
		insert_token_to_token(con, token, doc_id)

	close_db(con)

# insert a token into dictionary table group by document id
def insert_token_to_dictionary(con, token):
	cur = con.cursor()
	cur.execute("SELECT * FROM dictionary WHERE term = %s" % token)

	if cur.rowcount > 0 :
		cur.execute("UPDATE dictionary SET df = df + 1 WHERE term = %s" % token)
	else :
		cur.execute("INSERT INTO dictionary VALUES (%s, 1)" % token)

# insert a token in a document into token table
def insert_token_to_token(con, token, doc_id):
	cur = con.cursor()
	cur.execute("SELECT * FROM tokens WHERE term = %s AND doc_id = %d" % token, doc_id)

	if cur.rowcount > 0 :
		cur.execute("UPDATE tokens SET tf = tf + 1 WHERE term = %s AND doc_id = %d" % token, doc_id)
	else :
		cur.execute("INSERT INTO tokens VALUES (%d, %s, 1)" % doc_id, token)

# insert tfidf calculation of a term in a document into term weight table
# return terms weight array
def insert_terms_weight(con):
	terms_weight = {}
	cur = con.cursor()

	cur.execute("SELECT * FROM emails") 
	doc_count = cur.rowcount

	dicts = get_dicts(con)

	cur.execute("SELECT * FROM tokens");
	tokens = cur.fetchall()

	for token in tokens:
		tfidf = calc_tfidf(doc_count, token['tf'], dicts[token['term']])
		terms_weight[token['doc_id']][token['term']] = tfidf

	return terms_weight

# get dictionary table and transform into array key structure
# for easier access to df value
# return dicts array
def get_dicts(con):
	dicts = {}
	cur = con.cursor()

	cur.execute("SELECT * FROM dictionary")
	datas = cur.fetchall()

	for data in datas:
		dicts[data['term']] = df;

	return dicts

