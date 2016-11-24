import numpy as np
import random
import math
def read_file(file_1):
    matrix = []
    dataMatrix = []
    classLabels = []
    for line in file_1:
        matrix.append(line.strip().split(','))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp = float(matrix[i][j])
            matrix[i][j] = temp
        dataMatrix.append(matrix[i][0:len(matrix[0])-1])
        classLabels.append([matrix[i][len(matrix[0])-1]])
    return np.mat(dataMatrix),np.mat(classLabels)
def beyesi(matrix_1,label,weight):
    list_all=[]
    dict_all={}
    c = matrix_1.shape
    if weight==[]:
        weight=[1/(c[0]-1) for i in range(c[0]-1)]
    for i in range(c[1]):
        list_all.append(dict())
    for i in range(1,c[0]):
        for j in range(c[1]):
            if matrix_1[i,j] in list_all[j].keys():
                list_all[j][matrix_1[i,j]]+=weight[i-1]
            else:
                list_all[j][matrix_1[i,j]]=weight[i-1]
            if label[i,0] in dict_all.keys():
               if matrix_1[i,j] in dict_all[label[i,0]].keys():
                   dict_all[label[i,0]][matrix_1[i,j]]+=weight[i-1]
               else:
                   dict_all[label[i,0]][matrix_1[i, j]]=weight[i-1]
            else:
                dict_all[label[i,0]]={matrix_1[i,j]:weight[i-1]}
    return list_all,dict_all
def error_rate(matrix_d,label,list_all,dict_all):
    c=matrix_d.shape
    count=0
    for i in range(1,c[0]):
        key_result=0
        result=0
        for key in dict_all.keys():
            d=1
            for j in range(c[1]):
                d*=dict_all[key][matrix_d[i,j]]/list_all[j][matrix_d[i,j]]
            if d>result:
                result=d
                key_result=key
        if key_result !=label[i]:
            count+=1
    print(count)
    return count/(c[0]-1)
def bosting(matrix_d,label,list_all,dict_all,t):
    c= matrix_d.shape
    weight=[1/(c[0]-1) for i in range(c[0]-1)]
    # idx_all=[x+1 for x in range(c[0])]
    # random.sample(idx_all)
    # d=int[c[0]/10]
    for n in range(t):
        m = error_rate(matrix_d, label, list_all, dict_all)
        print(m)
        a =math.log((1-m)/m)/2
        # if a==0 or a>=0.5:
        #     break
        for i in range(1, c[0]):
            weight[i-1]*=math.exp(a)
            key_result = 0
            result = 0
            for key in dict_all.keys():
                d = 1
                for j in range(c[1]):
                    d *= dict_all[key][matrix_d[i, j]] / list_all[j][matrix_d[i, j]]
                if d > result:
                    result = d
                    key_result = key
            if key_result == label[i]:
                weight[i-1]*=math.exp(-a)
        for j in range(c[0]-1):
             weight[j]=weight[j]/sum(weight)
        list_all,dict_all=beyesi(matrix_d,label,weight)
    return list_all,dict_all
if __name__=='__main__':
    file_x=open('breast-cancer-assignment5.txt','r')
    matrix_all,label=read_file(file_x)
    weight=[]
    list_all,dict_all=beyesi(matrix_all,label,weight)
    b = error_rate(matrix_all, label, list_all, dict_all)
    print(b)
    list_all_1,dict_all_1=bosting(matrix_all,label,list_all,dict_all,10)
    a = error_rate(matrix_all, label, list_all_1, dict_all_1)
    print(a)#贝叶斯的错误率


