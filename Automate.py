# Author: Ravin D

import pandas as pd

class preprocess_tricks:

    def find_null(self,dataset):
        nulls = []
        for i in dataset:
            if (dataset[i].isna().sum()>0):
                nulls.append(i)
        return nulls

    def remove_null(self, dataset):
        cols = self.find_null(dataset=dataset)
        for i in cols:
            mean = dataset[i].mean()
            dataset.fillna(mean, inplace=True)
        return dataset
        

if __name__ == "__main__":
    dataset = pd.read_csv("archive/CC GENERAL.csv")
    obj = preprocess_tricks()
    obj.find_null(dataset=dataset)
    dataset = obj.remove_null(dataset=dataset)
    print(dataset.head())
    obj.find_null(dataset=dataset)