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

commitDict = {}

def clusterKMeans(repository_id):
    X,commitkeyList,commitmessList = getTFIDFMatrix(repository_id)
    clf = MiniBatchKMeans(n_clusters=100)  
    s = clf.fit(X)
    #clf.plot()
    print s

    #9个中心
    print '中心',clf.cluster_centers_

    #每个样本所属的簇
    print '每个样本所属的簇',clf.labels_,type(clf.labels_)

    #用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
    print '评估簇的个数是否合适',clf.inertia_
    print 'endTime',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    saveClusterResult(commitkeyList,commitmessList,clf.labels_)
    print 'saveTime',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    #进行预测
    #print clf.predict(feature)

    #保存模型
    joblib.dump(clf , '/home/happy/model/all.pkl')

    #载入保存的模型
    #clf = joblib.load('/home/happy/model/km.pkl')

    #用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
    #for i in range(5,30,1):
    #clf = KMeans(n_clusters=i)
    #s = clf.fit(feature)
    #print i , clf.inertia_


def saveClusterResult(commitkeyList,commitmessList,labels):
    global commitDict
    length = len(commitkeyList)/10000 + 1
    for i in range(length):
        if (i*10000 + 9999) > len(commitkeyList) - 1:
            temp_commitkeyList = commitkeyList[(i*10000):(len(commitkeyList) - 1)]
        else:
            temp_commitkeyList = commitkeyList[(i*10000):(i*10000 + 9999)]
        clusterList = []
        for i in range(len(temp_commitkeyList)):
            clusterList.append((temp_commitkeyList[i].split('_')[0],temp_commitkeyList[i].split('_')[1],commitDict[temp_commitkeyList[i]][1],commitDict[temp_commitkeyList[i]][2],labels[i],commitDict[temp_commitkeyList[i]][3],commitDict[temp_commitkeyList[i]][4],commitDict[temp_commitkeyList[i]][5],commitDict[temp_commitkeyList[i]][6],commitDict[temp_commitkeyList[i]][7]))
        saveClusterToDB(clusterList)



def saveClusterToDB(clusterList):
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
        cur=conn.cursor()
        cur.execute('set names utf8mb4')
        conn.select_db('vccfinder')
        sqli='insert into commit_cluster_minibatch (original_id,repository_id,sha,message,cluster,is_bug_fixed,author_email,committer_email,additions,deletions) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        cur.executemany(sqli,clusterList)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print e
        raise

def getTFIDFMatrix(repository_id):
    print 'getTime',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    contentDict = getCommitMessListByReposId(repository_id)
    print 'end-getTime',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    for item in contentDict.keys():
        try:
            contentDict[item] = contentDict[item].decode('utf-8').encode('utf-8')
        except:
            del contentDict[item]
    commitkeyList = contentDict.keys()
    commitmessList = contentDict.values()
    transformer=TfidfTransformer()
    vectorizer=CountVectorizer()
    tfidf=transformer.fit_transform(vectorizer.fit_transform(commitmessList))
    word=vectorizer.get_feature_names()
    print "feature维度：",len(word)
    print 'startTime',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #weight=tfidf.toarray()
    return tfidf,commitkeyList,commitmessList



def getCommitMessListByReposId(repository_id):
    global commitDict
    contentDict = {}
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
        cur=conn.cursor()
        conn.select_db('vccfinder')
        count=cur.execute('SELECT id,repository_id,sha,message,is_bug_fixed,author_email,committer_email,additions,deletions FROM commits_words where repository_id < %s;'%repository_id)
        result = cur.fetchall()
        if None != result:
            for item in result:
                contentDict[str(item[0])+'_'+str(item[1])] = item[3]
                commitDict[str(item[0])+'_'+str(item[1])] = (item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8])
        conn.commit()
        cur.close()
        conn.close()
        return contentDict
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    clusterKMeans(500)


