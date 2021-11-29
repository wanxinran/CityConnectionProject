import os.path
import numpy as np

def getFileData():
        graphFile = open('small_test.txt', "r")
        lines = graphFile.readlines()
        edgeID = []
        startID = []
        endID = []
        length = []
        for x in lines:
            edgeID.append(x.split(' ')[0])
            startID.append(x.split(' ')[1])
            endID.append(x.split(' ')[2])
            length.append(x.split(' ')[3])
        graphFile.close()
        return edgeID, startID, endID, length

if __name__ == '__main__':
    file_data = getFileData()
    print file_data
