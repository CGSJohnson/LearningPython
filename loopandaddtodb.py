#import library that contains date/time functions
import datetime

#import library used to help construct connection string
import urllib

#import library to access files/directories
from pathlib import Path

#import library to establish sql connection
from sqlalchemy import create_engine

#import library to get data
import pandas as pd

#establish db connectivity
server = 'JOHNSONLAPTOP\JOHNSONS'
database = 'PlayingAround'
#driver = "SQL Server Native Client 11.0"
#conn = f'mssql+pyodbc://{server}/{database}?trusted_connection=yes?driver=SQL+Server+Native+Client+11.0'
params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=" + server + ";DATABASE=" + database + ";trusted_connection=yes")

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

#get folder to iterate
#had to escape \ character by adding another
paths = Path('C:\\Sam\\logs\\')

#list to hold file names
filenames = []

#iterate folder
for file in paths.iterdir() :
    # because path is object not string
    file_in_str = str(file)
    # put filenames into a list
    filenames.append(file_in_str)

#put list into a data frame
listoffiles = pd.DataFrame(filenames)

#rename column header
listoffiles.columns=['FileName']

#add date/time column to data frame
listoffiles['FileUploadDTTM'] = datetime.datetime.now()
    
#print dataframe
#print(listoffiles)

#insert data frame into sql db
listoffiles.to_sql("ListOfFilesInDirectory", con = engine, if_exists = 'append', chunksize = 1000, method='multi', index=False)