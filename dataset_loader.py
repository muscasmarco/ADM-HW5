import pandas as pd

class DatasetLoader:

    def __init__(self, name, dataset_folder=''):

        self.name = name

        if self.name == 'coordinates':
            self.dataset_path = dataset_folder+'USA-road-'+self.name+'.CAL.co'
            self.cols = ['type','node-id', 'latitude','longitude']

        elif self.name == 'distance' or self.name == 'time-distance':
            self.dataset_path = dataset_folder+'USA-road-'+self.name+'.CAL.gr'
            self.cols = ['type','node-id-1', 'node-id-2', name]	


        self.dataset = pd.read_csv(self.dataset_path, sep=' ', header=None)
        self.dataset.columns = self.cols

    def get_dataset(self):
        return self.dataset


if __name__ == '__main__':
    dl = DatasetLoader('time-distance', './dataset/')
    ds = dl.dataset
