import pandas as pd

''' Just a class to load the datasets we are using, the point is having 
    more readability. '''

class DatasetLoader:

    def __init__(self, name, dataset_root_path='./dataset/'):

        ''' Just because why not, could be useful if the variable name is not ideal when this class is istantiated. '''
        self.name = name 
        
        if self.name == 'coordinates':
            self.dataset_path = dataset_root_path+'USA-road-'+self.name+'.CAL.co'
            self.cols = ['type','node-id', 'latitude','longitude']

        elif self.name == 'distance' or self.name == 'time-distance':
            self.dataset_path = dataset_root_path+'USA-road-'+self.name+'.CAL.gr'
            ''' Side note, distance and time-distance could have the same name for reusability'''
            self.cols = ['type','node-id-1', 'node-id-2', 'distance']	

        self.dataset = pd.read_csv(self.dataset_path, sep=' ', header=None) # The first row is not a header.
        self.dataset.columns = self.cols # Assigning name to the columns of the newly made dataset

    def get_dataset(self):
        return self.dataset