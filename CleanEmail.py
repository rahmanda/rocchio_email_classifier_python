#!/usr/bin/python
# -*- coding: utf-8 -*-
import email
import re
import json
import _mysql
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup # need install plugin


# class CleanEmail
# contain every method to clean single email document 
class CleanEmail:

	# cleaned email container
	__cleaned_email = {} 

	# constructor
	# automatically clean the email after instantiation
	def __init__(self, raw_email):
		cleaned_email = {}
		document = email.message_from_string(raw_email)
		# what is the purpose of using array?
		cleaned_email['subject'] = self._get_email_subject(document)
		cleaned_email['sender'] = self._get_email_sender(document)
		cleaned_email['recipient'] = self._get_email_recipient(document)
		cleaned_email['body'] = self._get_email_body(document)

		self.__cleaned_email = cleaned_email

	# get subject from email and cleanup
	def _get_email_subject(self, document):
		# TODO cleaning
		return document['Subject']

	# get sender from email and cleanup
	def _get_email_sender(self, document):
		# TODO cleaning
		return document['From']

	# get recipient from email and cleanup
	def _get_email_recipient(self, document):
		# TODO cleaning
		return document['To']

	# get email body (main content) from email and cleanup
	def _get_email_body(self, document):
		maintype = document.get_content_maintype()
		if maintype == 'multipart':
			email_body = self._get_multipart(document)
		elif maintype == 'text':
			email_body = self._get_text(document)
		return self._clean_email_body(email_body)

	# get content of email body for multipart type
	def _get_multipart(self, document):
		for part in document.get_payload():
			if part.get_content_maintype() == 'text':
				return part.get_payload()

	# get content of email body for text type
	def _get_text(self, document):
		email = document.get_payload()
		soup = BeautifulSoup(email)
		return soup.get_text()

	# cleanup email body from quoted printable, links, numbers and special character
	def _clean_email_body(self, email_body):
		cleaned_email = email_body.decode('quopri')
		cleaned_email = re.sub(r'''(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', cleaned_email, flags=re.MULTILINE)
		cleaned_email = re.sub(r'\(\w*\)', '', cleaned_email)
		cleaned_email = re.sub(r'[-+=:;\*\(\)\[\]\<\>\|!?.,\'\"\\\/0-9]+', '', cleaned_email)
		cleaned_email = cleaned_email.replace('%', ' ')
		cleaned_email = re.sub(r'[\n\t]+', ' ', cleaned_email)
		cleaned_email = re.sub(r'\s+',' ', cleaned_email, flags=re.MULTILINE)
		cleaned_email = '\n'.join(cleaned_email.split())
		cleaned_email = cleaned_email.lower();
		return cleaned_email

	# get cleaned email in JSON
	def get_cleaned_email(self):
		return json.dumps(self.__cleaned_email)