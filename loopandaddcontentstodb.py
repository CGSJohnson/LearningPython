#import library that contains date/time functions
import datetime

#import library used to help construct connection string
import urllib

#import library to establish sql connection
from sqlalchemy import create_engine

#import library to access files/directories
from pathlib import Path

#import library to get/manipulate data
import pandas as pd

#establish db connectivity
server = 'JOHNSONLAPTOP\JOHNSONS'
database = 'PlayingAround'
params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=" + server + ";DATABASE=" + database + ";trusted_connection=yes")

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

#get folder to iterate
#had to escape \ character by adding another
paths = Path('C:\\Users\\Johnsons\\AppData\\Local\\Temp\\PythonDataSets')

#define list to hold all data
listoffilesandcontents = []

#iterate folder and read contents of files in the folder
for file in paths.iterdir() :
    # because path is object not string
    file_in_str = str(file)
    
    # open file and read contents into a data frame
    filesandcontents = pd.read_csv(file_in_str)

    # add filename and date/time columns to dataframe
    filesandcontents["FileName"] = file_in_str
    filesandcontents["FileUploadDTTM"] = datetime.datetime.now()
    #print(filesandcontents)
    listoffilesandcontents.append(filesandcontents)
    #print(listoffilesandcontents)

#construct final data frame for insert into db
allfilesandcontents = pd.concat(listoffilesandcontents, axis=0, ignore_index=True)  

#insert data frame into sql db
allfilesandcontents.to_sql("FilesInDirectory", con = engine, if_exists = 'append', chunksize = 1000, method='multi', index=False)