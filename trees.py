#encoding=utf-8
from math import log
import operator

def calcShannonEnt(dataSet):#求熵
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLable = featVec[-1]
		if currentLable not in labelCounts.keys():
			labelCounts[currentLable] = 0
		labelCounts[currentLable] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob * log(prob,2)
	return shannonEnt		

def createDataSet():
	dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	labels = ['no sufacing','flippers']
	return dataSet,labels;

def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:#如果数据集中的特征等于期望值
			reducedFeatVec = featVec[:axis]#他前面的数据
			reducedFeatVec.extend(featVec[axis+1:])#他后面的数据
			retDataSet.append(reducedFeatVec)
	return retDataSet		

def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1	
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0
	bestFeature = -1
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet,i,value)
			prob = len(subDataSet)/float(len(dataSet))#算出这个熵的权重
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature

def majorityCnt(classList):#出现最多的分类名称
	classCount={}
	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

def createTree(dataSet,labels):
	classList = [example[-1] for example in dataSet]#-1是列表中最后一个
	if classList.count(classList[0]) == len(classList):#所有内容相同
		return classList[0]
	if len(dataSet[0]) == 1:#分组用完了所有特性,选个最多的
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
	return myTree	

def classify(inputTree,featLabels,testVec):#testVes [1,0]
	firstStr = inputTree.keys()[0]
	secondDict = inputTree[firstStr]
	featIndex = featLabels.index(firstStr)#找出这个特性是第几个属性
	for key in secondDict.keys():
		if testVec[featIndex] == key:#回答testVes的问题,是否正确,正确就继续
			if type(secondDict[key]).__name__=='dict':#如果不是叶子节点则继续
				classLabel = classify(secondDict[key],featLabels,testVec)
			else:
				classLabel = secondDict[key]
	return classLabel

def storeTree(inputTree,filename):
	import pickle
	fw = open(filename,'w')
	pickle.dump(inputTree,fw)
	fw.close()

def grabTree(filename):
	import pickle
	fr = open(filename)
	return pickle.load(fr)




































