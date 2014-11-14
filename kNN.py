#encoding=utf-8
from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])#参造系
	labels = ['A','A','B','B']#标签
	return group,labels

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]#拿出行数
	diffMat = tile(inX, (dataSetSize,1)) - dataSet#先复制输入矩阵,行复制参造矩阵行数,列为1次,然后矩阵减法
	sqDiffMat = diffMat**2#矩阵平方
	sqDistances = sqDiffMat.sum(axis=1)#矩阵相加
	distancse = sqDistances**0.5#矩阵开方
	sortedDistIndicies = distancse.argsort()#排序,从小到大,结果其实是矩阵索引
	classCount={}
	for i in range(k):#k是找出前几个
		voteIlable = labels[sortedDistIndicies[i]]#拿出第几个label
		classCount[voteIlable] = classCount.get(voteIlable,0) + 1#遍历label ,并+1, 取前k个
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)#根据label的数量排序
	return sortedClassCount[0][0]#返回符合次数最多的label

def autoNorm(dataSet):#归一化
	minVals = dataSet.min(0)#矩阵每列中的最小
	maxVals = dataSet.max(0)#矩阵每列中的最大
	ranges = maxVals - minVals#差值
	normDataSet = dataSet - tile(minValus,(m,1))#矩阵每项减去最小值
	normDataSet = normDataSet / tile(ranges,(m,1))#再除以差值,结果都在0-1区间
	return normDataSet, ranges, minVals
