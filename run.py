# since our code is in r, and it is still not finished yet, this file is just for the submission of MA5
import pandas as pd
import numpy as np
import sys

def inputData(d):
    try:
        data=pd.read_csv('test/testdata/'+d).drop(['Unnamed: 0'],axis=1)
        return data
    except:
        print('failed in data reading')


if __name__ == "__main__":
    print(inputData(sys.argv[1]))