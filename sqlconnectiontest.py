import pyodbc

#test output
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'JOHNSONLAPTOP\JOHNSONS'
database = 'WOES'
yesreply = 'yes'
cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';Trusted_Connection=' + yesreply)
cursor = cnxn.cursor()

#Sample select query
#cursor.execute("SELECT @@version;") 
cursor.execute("SELECT TOP (1000) GiftTypeID ,GiftTypeTxt,GiftTypeDisplayOrder FROM WOES.dbo.GiftTypes")

for row in cursor :
    print(row)