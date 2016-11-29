import numpy as np
import random
import math
def read_file(file_1):
    matrix = []
    dataMatrix = []
    classLabels = []
    for line in file_1:
        matrix.append(line.strip().split(','))
    matrix[0]
    for j in range(len(matrix[0])):
        temp =int(matrix[0][j])
        matrix[0][j] = temp
    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            temp = float(matrix[i][j])
            matrix[i][j] = temp
        dataMatrix.append(matrix[i][0:len(matrix[1])-1])
        classLabels.append(matrix[i][len(matrix[1])-1])
    return np.mat(dataMatrix),classLabels,matrix[0]
def beyesi(matrix_1,label,weight):
    dict_all={}
    c = matrix_1.shape
    for ii in set(label[1:c[0]]):
        dict_all[ii] = []
        for j in range(c[1]):
            dict_all[ii].append({})
    if weight==[]:
        weight=[1/(c[0]) for i in range(c[0])]
    print(weight)
    for i in range(c[0]):
        for j in range(c[1]):
            if matrix_1[i,j] in dict_all[label[i]][j].keys():
                dict_all[label[i]][j][matrix_1[i,j]] +=weight[i]
            else:
                dict_all[label[i]][j][matrix_1[i, j]] = weight[i]
    return dict_all
def error_rate(matrix_d,label,dict_all):
    count_dict={}
    for i in dict_all.keys():
        for j in dict_all[i][0].keys():
            if i in count_dict.keys():
                count_dict[i]+=dict_all[i][0][j]
            else:
                count_dict[i]=dict_all[i][0][j]
    c=matrix_d.shape
    count=0
    for i in range(c[0]):
        result = 0
        d=1
        for key in dict_all.keys():
            for j in range(c[1]):
                if matrix_d[i,j] in dict_all[key][j].keys():
                    d*=dict_all[key][j][float(matrix_d[i,j])]/count_dict[key]
                else :
                    d=0
                    break
            d*=count_dict[key]/(c[0])
            if d>=result:
                result=d
                key_result=key
        if key_result !=label[i]:
            count+=1
    return count/(c[0])
def bosting(matrix_d,label,dict_all,t):
    c= matrix_d.shape
    count_dict = {}
    for i in dict_all.keys():
        for j in dict_all[i][0].keys():
            if i in count_dict.keys():
                count_dict[i] += dict_all[i][0][j]
            else:
                count_dict[i] = dict_all[i][0][j]
    weight=[1/(c[0]) for i in range(c[0])]
    m = error_rate(matrix_d, label, dict_all)
    for n in range(t):
        a =math.log((1-m)/m)/2
        for i in range(c[0]):
            weight[i]*=math.exp(a)
            result = 0
            key_result = 0
            for key in dict_all.keys():
                d = 1
                for j in range(c[1]):
                    if matrix_d[i, j] in dict_all[key][j].keys():
                        d *= dict_all[key][j][float(matrix_d[i, j])] / count_dict[key]
                    else:
                        d = 0
                        break
                d *= count_dict[key] / (c[0])
                if d>= result:
                    result = d
                    key_result = key
            if key_result == label[i]:
                weight[i]*=math.exp(-a)
        b=sum(weight)
        for j in range(c[0]):
             weight[j]=weight[j]/b
        dict_all_1=beyesi(matrix_d,label,weight)
        m = error_rate(matrix_d, label, dict_all_1)
    return dict_all
def fenli(matrix_d):
    c=matrix_d.shape
    idx=[i for i in range(c[0])]
    idx.random.sample
    idx_1=np.mat(idx[0:int(c[0]/10)])
    idx_2=np.mat(idx[int(c[0]/10):c[0]])
    return matrix_d[idx_1,:],matrix_d[idx_2,:]

if __name__=='__main__':
    file_x=open('breast-cancer-assignment5.txt','r')
    # file_x=open('hello.txt','r')
    matrix_all,label,typ=read_file(file_x)
    print(label)
    weight=[]
    dict_all=beyesi(matrix_all,label,weight)
    print(dict_all)
    b = error_rate(matrix_all, label, dict_all)
    print(1-b)
    dict_all_1=bosting(matrix_all,label,dict_all,20)
    a = error_rate(matrix_all, label, dict_all_1)
    print(1-a)


