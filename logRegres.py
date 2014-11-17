#encoding=utf-8
from numpy import *
def loadDataSet():
	dataMat = []
	labelMat = []
	fr = open('testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat

def sigmoid(inX):
	return 1.0/(1+exp(-inX))

def gradAscent(dataMatIn,classLabels):#梯度上升算法
	dataMatrix = mat(dataMatIn)#数组矩阵化
	labelMat = mat(classLabels).transpose()#矩阵化后，行向量转为列向量
	m,n = shape(dataMatrix)# 100 行,3 列
	alpha = 0.001
	maxCycles = 500
	weights = ones((n,1))
	for k in range(maxCycles):
		h = sigmoid(dataMatrix * weights) #结果是个列向量
		error = (labelMat - h) #真实 减去 实际，算出差值
		weights = weights + alpha * dataMatrix.transpose() * error
	return weights
