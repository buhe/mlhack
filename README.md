mlhack
======

##k邻近
其实就是计算矩阵的距离，比较简单，不需要初始化数据就能预测，而且准确度貌似很高，但其实还是需要一部分已知数据进行测试，而且指标的选择看起来非常重要，会严重影响准确度。
----
##决策树
要找到关键点，需要计算数据集的熵，然后根据熵来决定哪些特性是主要的，则放到决策树的头部，就是先决策。
----
##朴素贝叶斯
###条件概率
	P(gray|bucketB) = P(gray and bucketB) / P(bucketB)
	条件概率,B桶中的灰球 = 灰球在所有桶中的概率 除以 球在B桶中的概率
	1 / 3 = (1/7) / (3/7)

