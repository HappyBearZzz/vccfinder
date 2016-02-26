#coding=utf-8 
import urllib2  
import os
import sys
import socket
import MySQLdb
import ssl
import time          
import re          
import os
import string
import sys
import math
import nltk
import sklearn
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import random
from sklearn.cluster import KMeans 
from sklearn.cluster import MiniBatchKMeans 
from sklearn.externals import joblib
import numpy
import string
from string import punctuation  
import re
import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords

def transToWords():
    reposIdResult = getAllRepositoryId()
    if None != reposIdResult:
        for item in reposIdResult:
            repos_id = item[0]
            print 'repos_id:',repos_id,str(repos_id)#str(repos_id)[0:len(str(repos_id))-1]
            commitList = getCommitMessListByReposId(str(repos_id))
            insertCommitWordsListToDB(commitList)


def insertCommitWordsListToDB(commitList):
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
        conn.set_character_set('utf8')
        cur=conn.cursor()
        cur.execute('SET CHARACTER SET utf8mb4;')
        cur.execute('SET character_set_connection=utf8mb4;')
        cur.execute('set names utf8mb4')
        conn.select_db('vccfinder')
        sqli='insert into commits_words (id,repository_id,is_bug_fixed,sha,url,author_email,author_name,author_when,committer_email,committer_name,committer_when,additions,deletions,total_changes,message,patch,cve,files_changed) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        cur.executemany(sqli,commitList)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print e
        raise



def getAllRepositoryId():
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
        cur=conn.cursor()
        conn.select_db('vccfinder')
        count=cur.execute('SELECT distinct(repository_id) FROM commits;')
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


def getCommitMessListByReposId(repository_id):
    commitList = []
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
        cur=conn.cursor()
        conn.select_db('vccfinder')
        count=cur.execute('SELECT * FROM commits where repository_id = %s;'%repository_id)
        result = cur.fetchall()
        if None != result:
            for item in result:
                mess = getStem(removePunctuationNum(item[14]))
                commitList.append((item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12],item[13],mess,item[15],item[16],item[17]))
        conn.commit()
        cur.close()
        conn.close()
        return commitList
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def removePunctuationNum(text):
    text = re.sub(r'[{}]+'.format('!"$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'),' ',text.decode('utf-8','ignore').encode('utf-8'))
    return text

def getStem(text):
    st = nltk.LancasterStemmer()
    wordList = text.split(' ')
    #print 'wordList',wordList
    stemList = []
    for word in wordList:
        #print 'word',word
        if word != '':
            try:
                temp_word = st.stem(word.decode('utf-8','ignore').encode('utf-8'))
                if not temp_word in stopwords.words('english'):
                    stemList.append(temp_word)
            except:
                print 'error-word',word
                pass
    return ' '.join(stemList)

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    transToWords()


