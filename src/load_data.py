import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column,Integer,String
import glob
import os
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper

Base=declarative_base()
def Load_Data():
    csv_data=pd.read_csv(r'csv/train.csv')
    #Convert dataframe to list and store in same variable
    csv_data=csv_data.values.tolist()
    return csv_data
if __name__ == "__main__":
    # SQL Alchemy setup
    # Create engine that will allow us to communicate with database
    engine = create_engine('sqlite:///training_data_db.sqlite',echo=False)
    # Creating session which is the middle ground to talk to our engine
    Session = sessionmaker(bind=engine)
    s = Session()
    data = Load_Data() 
    print(data)


