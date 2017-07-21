#!/usr/bin/env python
# coding=utf-8

import numpy as np

class NaiveBayes(object):

    def readData(self,filePath):
        # read data from filePath
        file = open(filePath,'r')
        data = []
        for line in file.readlines():
            line = [int(x) for x in str.split(line,',')]
            data.append(line)
        self.trainData = np.array(data)
        return self.trainData

    def train(self, trainData):
        self.n_class, labels = [], trainData[:,-1]
        # counting the number of samples belonging to class 0 and class 1,respectively
        for x in xrange(2):
            n_class_x = np.count_nonzero(labels == x)
            self.n_class.append(n_class_x)
            
        self.n_class = np.array(self.n_class)

        feature_max_value, n_feature = np.max(trainData[:,:trainData.shape[1]])+1, trainData.shape[1]
        self.n_feature_class = np.zeros((feature_max_value, n_feature, 2))
        # counting then number of samples
        for c in xrange(2):
            for feature in xrange(n_feature):
                for value in xrange(feature_max_value):
                    for i in xrange(trainData.shape[0]):
                        if labels[i] == c and trainData[i,feature] == value:
                            self.n_feature_class[value,feature,c]+=1.0
        return True

    def predict(self, predictData):
        #calculating the probability of class 0 and class 1, respectively
        p0, p1 = self.n_class[0]*1.0/np.sum(self.n_class), self.n_class[1]*1.0/np.sum(self.n_class)
        predictData = np.array([int(x) for x in str.split(predictData,',')])
        for i in xrange(predictData.shape[0]):
            p0 *= self.n_feature_class[predictData[i],i,0]/self.n_class[0]

        for i in xrange(predictData.shape[0]):
            p1 *= self.n_feature_class[predictData[i],i,1]/self.n_class[1]
        return 1 if p1>p0 else 0


if __name__ == '__main__':

    bayes = NaiveBayes()
    trainData = bayes.readData('data.txt')
    print bayes.train(trainData)
    print bayes.predict('2,2,2,1,1')

