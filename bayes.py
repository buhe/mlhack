#encoding=utf-8
from numpy import *
def loadDataSet():
	postingList=[['my','dog','has','flea','problems','help','please'],
				['maybe','not','take','him','to','dog','park','dtupid'],
				['my','dalmation','is','so','cute','I','love','him'],
				['stop','posting','stipid','worthless','garbage'],
				['mr','licks','ate','my','steak','how','to','stop','him'],
				['quit','buying','worthless','dog','food','stupid']
				]
	classVec = [0,1,0,1,0,1]
	return postingList,classVec

def createVocabList(dataSet):
	vocabSet = set([])
	for document in dataSet:
		vocabSet = vocabSet | set(document) #两个集合的并集
	return list(vocabSet)

def setOfWords2Vec(vocabList,inputSet):#输入语句(inputSet)在单词表(vocabList)中的位置
	returnVec = [0]*len(vocabList)
	for word in inputSet:
		if word in vocabList:
			returnVec[vocabList.index(word)] = 1
		else:
			print "the word: %s is not in my Vocabulary!" % word
	return returnVec

def trainNB0(trainMatrix,trainCategory):#trainMatrix 被setOfWords2Vec 处理成向量化,既出现的单词在单词表的位置+1
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	pAbusive = sum(trainCategory)/float(numTrainDocs) #计算P(1) 的概率,sum(trainCategory)是概率为1的语句和,float(numTrainDocs) 有几个语句
	p0Num = zeros(numWords)#一维数组,都是0,最终算出,非侮辱性语句中,每个单词出现的次数
	p1Num = zeros(numWords)
	p0Denom = 0.0
	p1Denom = 0.0
	for i in range(numTrainDocs): #遍历6个文档
		if trainCategory[i] == 1: #如果文档是 侮辱性的
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	p1Vect = p1Num / p1Denom
	p0Vect = p0Num / p0Denom
	return p0Vect,p1Vect,pAbusive

def trainNB1(trainMatrix,trainCategory):#trainMatrix 被setOfWords2Vec 处理成向量化,既出现的单词在单词表的位置 = 1
	numTrainDocs = len(trainMatrix)
	numWords = len(trainMatrix[0])
	pAbusive = sum(trainCategory)/float(numTrainDocs) #计算P(1) 的概率,sum(trainCategory)是概率为1的语句和,float(numTrainDocs) 有几个语句
	p0Num = ones(numWords)#一维数组,都是1,最终算出,非侮辱性语句中,每个单词出现的次数
	p1Num = ones(numWords)
	p0Denom = 2.0
	p1Denom = 2.0
	for i in range(numTrainDocs): #遍历6个文档
		if trainCategory[i] == 1: #如果文档是 侮辱性的
			p1Num += trainMatrix[i]
			p1Denom += sum(trainMatrix[i])
		else:
			p0Num += trainMatrix[i]
			p0Denom += sum(trainMatrix[i])
	p1Vect = log(p1Num / p1Denom)
	p0Vect = log(p0Num / p0Denom)
	return p0Vect,p1Vect,pAbusive

def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
	p1 = sum(vec2Classify * p1Vec) + log(pClass1)
	# 前面是如果单词出现过(向量是1)则统计其概率,最后相加,后面再加上类别出现的概率,就是朴素贝叶斯的概率
	p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
	if p1 > p0:
		return 1;
	else:
		return 0;













