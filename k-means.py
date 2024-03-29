from numpy import *


#加载数据
def loadDataSet():
    dataMat = []
    fr = open("testSet.txt")
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        # fltLine = map(float, curLine)
        dataMat.append([float(curLine[0]),float(curLine[1])])
    return dataMat
#[[1.658985, 4.285136], [-3.453687, 3.424321], [4.838138, -1.151539], [-5.379713, -3.362104], [0.972564, 2.924086], [-3.567919, 1.531611], [0.450614, -3.302219], [-3.487105, -1.724432], [2.668759, 1.594842], [-3.156485, 3.191137], [3.165506, -3.999838], [-2.786837, -3.099354], [4.208187, 2.984927], [-2.123337, 2.943366], [0.704199, -0.479481], [-0.39237, -3.963704], [2.831667, 1.574018], [-0.790153, 3.343144], [2.943496, -3.357075], [-3.195883, -2.283926], [2.336445, 2.875106], [-1.786345, 2.554248], [2.190101, -1.90602], [-3.403367, -2.778288], [1.778124, 3.880832], [-1.688346, 2.230267], [2.592976, -2.054368], [-4.007257, -3.207066], [2.257734, 3.387564], [-2.679011, 0.785119], [0.939512, -4.023563], [-3.674424, -2.261084], [2.046259, 2.735279], [-3.18947, 1.780269], [4.372646, -0.822248], [-2.579316, -3.497576], [1.889034, 5.1904], [-0.798747, 2.185588], [2.83652, -2.658556], [-3.837877, -3.253815], [2.096701, 3.886007], [-2.709034, 2.923887], [3.367037, -3.184789], [-2.121479, -4.232586], [2.329546, 3.179764], [-3.284816, 3.273099], [3.091414, -3.815232], [-3.762093, -2.432191], [3.542056, 2.778832], [-1.736822, 4.241041], [2.127073, -2.98368], [-4.323818, -3.938116], [3.792121, 5.135768], [-4.786473, 3.358547], [2.624081, -3.260715], [-4.009299, -2.978115], [2.493525, 1.96371], [-2.513661, 2.642162], [1.864375, -3.176309], [-3.171184, -3.572452], [2.89422, 2.489128], [-2.562539, 2.884438], [3.491078, -3.947487], [-2.565729, -2.012114], [3.332948, 3.983102], [-1.616805, 3.573188], [2.280615, -2.559444], [-2.651229, -3.103198], [2.321395, 3.154987], [-1.685703, 2.939697], [3.031012, -3.620252], [-4.599622, -2.185829], [4.196223, 1.126677], [-2.133863, 3.093686], [4.668892, -2.562705], [-2.793241, -2.149706], [2.884105, 3.043438], [-2.967647, 2.848696], [4.479332, -1.764772], [-4.905566, -2.91107]]



# print(loadDataSet())

dataSet = mat(loadDataSet())                    #这里mat不能丢失,丢失就会报错
#这里的dataSet是80行2列的一个矩阵

#获取欧式距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))     #这里需要先相减；再算个平方；再求和;再开平方
# >>> x1 = range(6)
# >>> x1
# [0, 1, 2, 3, 4, 5]
# >>> np.power(x1, 3)
# array([  0,   1,   8,  27,  64, 125])


#初始化质心并确定质心范围
def randCent(dataSet, k):
    n = shape(dataSet)[1]                       #这里表示的是列数，这里n = 2
    # print(n)
    centroids = mat(zeros((k, n)))              #k(3)行2列，下面是确定范围，这里对质心做了个初始化(初始化为3行2列的0矩阵)
    for j in range(n):
        minJ = min(dataSet[:, j])                                       #求第j列的最小值，这里有2列，80行
        rangeJ = float(max(dataSet[:, j]) - minJ)                       #偏移量；第j列的最大值和最小值的差值
        centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))        #质心初始化
        # arr1 = random.rand(3, 1)
        # print(arr1)
        # # [[0.28226936]
        # #  [0.74514296]
        # #  [0.94803495]]
        # arr2 = 10 * arr1
        # print(arr2)
        # # [[2.82269362]
        # #  [7.45142963]
        # #  [9.4803495 ]]
        #
        # arr3 = -5 + arr2
        # print(arr3)
        # # [[-2.17730638]
        #  # [ 2.45142963]
        #  # [ 4.4803495 ]]
    return centroids
# print(random.rand(3,2))
# [[0.46957239 0.66290334]
#  [0.75796764 0.31432774]
#  [0.63107047 0.23190033]]




# randCent(dataSet, 3)
# print(randCent(dataSet, 3))


#求出质心
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0]                                           #求出dataSet的行数，这里有80行；这里的m=80
    clusterAssment = mat(zeros((m, 2)))                             #这里得到一个簇并进行初始化这是一个80*2的矩阵里面放的是什么呢,第一列放的是质心的编号(这里为0，1，2三个质心),第二列放的是到某个点(这里一共有80个点)的距离, (通过这种方法可以把80个点分出3个类)
                                                                    # 这里需要说明一下:这三个质心分别计算一下到点A的距离，假设到点A的距离最短的是质心0，那么这个矩阵的这一行这里就写质心0和，质心0到这个点的距离，到下一个点B的距离最短的是质心是2,矩阵这一行就写质心2和质心2到点B的距离，依次类推，一共要写80行，最后可以被分出3大类
    centroids = createCent(dataSet, k)                              #初始化质心,这里k=3,这里调用了randCent函数;这里的centroids是一个3行2列的矩阵
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):                                              #这里需要循环80次
            minDist = inf                                               #这里的Inf表示的是正无穷;-inf表示的是负无穷
            minIndex = -1                                               #
            for j in range(k):                                          #这里k等于3，要循环3次
                distJI = distMeas(centroids[j, :], dataSet[i, :])       #得出欧式距离,这里调用了计算欧式距离的那个函数，这里计算的是[k(这里为3个，故里面一层循环为3)个]质心到到样本点(这里有80个,故外层循环为80)的欧式距离
                if distJI < minDist:                                    #这里的minDist的初始值为无穷大，故这里必然会执行下面的语句
                    minDist = distJI                                    #获取最小距离,就是利用欧式距离来计算的
                    minIndex = j                                        #该最小距离所对应的那个质心的索引,这个分类的原理上面已经说过
            if clusterAssment[i, 0] != minIndex:                        #
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist ** 2           #这里的clusterAssment就是上面所说的80*2矩阵(这里第一列放的是到某个点的距离最小的那个质心的索引(编号)，第二列放的是最短距离的平方)
        # print(clusterAssment)                                         #clusterAssment具体是什么看最下面,有示例
        for cent in range(k):                                           #这里的k为3
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]        #这里的ptsInClust是个矩阵(k就三类),k=0时，里面放的是k为0时候所对应的那一类的点的集合,k为1时，里面放的是k为1类时候所对应的那一类的点的集合；k为2时，里面放的是k为2类的时候点的集合
            centroids[cent, :] = mean(ptsInClust, axis=0)                           #得到某一类(这里有3类)的数据的平均值;其实就是这一类的点的坐标的平均值(可以看做中心点)
            # print(mean([[1,2],[2,2]],axis=0))                                     #这里是把每列的数值都加起来然后再除以个数得到平均值
            # [1.5 2. ]
    return centroids, clusterAssment                                    #这里的返回值centroids指的是三类点的各自中心点位置(就三个点);clusterAssment是一个80*2的矩阵，里面存放了3个质心到80个点的最短距离，同时也将这80个点分成了3类
#这里对dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]进行理解:
# clusterAssment = mat([[0,1],[1,1],[2,1],[0,2],[1,2]])
# print(clusterAssment)
# 这里面的第一列的0,1,2,0,1(第一列表示的是类别(这里有0，1，2这三类))的索引为0，1，2，3，4；
# [[0 1]
#  [1 1]
#  [2 1]
#  [0 2]
#  [1 2]]
# for cent in range(3):
    # print(nonzero(clusterAssment[:,0].A==cent)[0])      #这里的作用是把clusterAssment这个矩阵里面的类别(第一列)的索引提取出来
    # [0 3]                                             #这里的0，3表示的是第0类的索引
    # -----------------------------------
    # [1 4]                                            #这里的1，4表示的是第1类的索引
    # -----------------------------------
    # [2]                                              #这里的2表示的是第2类的索引


centroids,clusterAssment = kMeans(dataSet,3,distMeas=distEclud,createCent=randCent)
print(centroids)
#每一次运行的结果应该不一样
# [[ 2.65077367 -2.79019029]
#  [ 1.98283629  3.1465235 ]
#  [-3.18695357 -0.35938491]]


# clusterAssment:
# [[ 1.         21.64606637]
#  [ 2.         22.15745896]
#  [ 1.          3.86992835]
#  [ 0.          0.        ]
#  [ 1.         18.77390019]
#  [ 2.          8.12144342]
#  [ 0.          0.        ]
#  [ 2.          1.26826624]
#  [ 1.          4.97017662]
#  [ 2.         20.75976007]
#  [ 1.         25.70564255]
#  [ 0.          0.        ]
#  [ 1.          5.01405398]
#  [ 2.         22.43748216]
#  [ 1.         18.09771574]
#  [ 0.          0.        ]
#  [ 1.          4.28426912]
#  [ 2.         33.91848178]
#  [ 1.         20.68638872]
#  [ 0.          0.        ]
#  [ 1.         10.10691637]
#  [ 2.         21.08025955]
#  [ 1.         13.98710656]
#  [ 0.          0.        ]
#  [ 1.         18.27875966]
#  [ 2.         19.30597385]
#  [ 1.         12.91021773]
#  [ 0.          0.        ]
#  [ 1.         12.8692257 ]
#  [ 2.          7.03335285]
#  [ 0.          0.        ]
#  [ 0.          0.        ]
#  [ 1.         11.03906039]
#  [ 2.         10.35280912]
#  [ 1.          2.8249735 ]
#  [ 0.          0.        ]
#  [ 1.         27.37772699]
#  [ 2.         24.74186718]
#  [ 1.         15.74660248]
#  [ 0.          0.        ]
#  [ 1.         16.51406127]
#  [ 2.         19.87339541]
#  [ 1.         17.92209602]
#  [ 0.          0.        ]
#  [ 1.         11.48904472]
#  [ 2.         21.16143465]
#  [ 1.         24.20370931]
#  [ 0.          0.        ]
#  [ 1.          5.33649374]
#  [ 2.         36.76495251]
#  [ 1.         21.33850243]
#  [ 0.          0.        ]
#  [ 1.         19.60855704]
#  [ 2.         20.62824228]
#  [ 1.         21.15232692]
#  [ 0.          0.        ]
#  [ 1.          6.44484144]
#  [ 2.         18.37055176]
#  [ 1.         24.28942062]
#  [ 0.          0.        ]
#  [ 1.          6.27575111]
#  [ 2.         20.08876593]
#  [ 1.         24.27411586]
#  [ 0.          0.        ]
#  [ 1.         12.07094846]
#  [ 2.         30.65066804]
#  [ 1.         17.51224373]
#  [ 0.          0.        ]
#  [ 1.         11.41206308]
#  [ 2.         24.65151437]
#  [ 1.         22.64136159]
#  [ 2.          1.04473345]
#  [ 1.          0.41216091]
#  [ 2.         23.64810477]
#  [ 1.         11.40987029]
#  [ 0.          0.        ]
#  [ 1.          8.47787883]
#  [ 2.         18.41988993]
#  [ 1.          6.72711269]
#  [ 0.          0.        ]]
