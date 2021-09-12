import re
import os
import sys

import pandas as pd
import numpy as nb
import spacy
import unicodedata

from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup

#Get words Count from the text
def _get_wordscount(x):
	length= len(str(x).split())
	return length

#Get Character Count from the text
def _get_charcounts(x):
	s=x.split()
	x=''.join(s)
	return len(x)

#Get Average Count from the text
def _get_averagecount(x):
	count=_get_charcounts(x)/_get_wordscount(x)
	return count


def _get_stopwords(x):
	l= len([t for t in x.split() if t in stopwords])
	return l

def _get_hashtagcounts(x):
	h=len([t for t in x.split() if t.startswith('#')])
	return h

def _get_mentioncounts(x):
	m=len([t for t in x.split() if t.startswith('@')])
	return m

def _get_digitcounts(x):
	d=len([t for t in x.split() if t.isdigit()])
	return d

def _get_uppercount(x):
	u=len([t for t in x.split() if t.isupper()])
	return u


def _get_emails(x):
	email= re.findall(r'([a-zA-Z0-9+._]+@[a-zA-Z0-9+._]+\.[a-zA-Z0-9+._]+\b)',x)
	count=len(email)
	return email, count

def _remove_emails(x):
	return re.sub(r'([a-zA-Z0-9+._]+@[a-zA-Z0-9+._]+\.[a-zA-Z0-9+._]+\b)',x)

def _remove_rt(x):
	return re.sub(r'\brt\b',' ',str(x))

def _remove_specialcharacter(x):
	x=re.sub(r'[\W ]+'," ",x)
	x=''.join(x.split())
	return x

def _remove_html_tags(x):
	return BeautifulSoup(x,'lxml').get_text().strip()


def _remove_accentedchar(x):
	 x=unicodedata.normalize('NFKD',x).encode('ascii','ignore').decode('utf-8','ignore')
	 return x

def _spelling_correction(x):
	x=TextBlob(x).correct()
	return x