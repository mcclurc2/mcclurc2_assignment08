#main.py

import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')
cursor = conn.cursor()
# Submit a query to the SQL Server instance and store the results in the cursor object
cursor.execute('SELECT * FROM tStoreStatus')
total_fires = 0

for row in cursor:
    print(row)



