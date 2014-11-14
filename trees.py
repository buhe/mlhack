from math import log

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