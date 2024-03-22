#final output in on prem

import mysql.connector

# Establish connection to MySQL
mydb = mysql.connector.connect(
        host='capstonerds.cb66m60m6g6j.us-west-1.rds.amazonaws.com',
        user='admin',
        password='kavin123',
        database='capdb'
    
)
mycursor = mydb.cursor()

# Define the CREATE TABLE query
create_table_query = '''
    CREATE TABLE IF NOT EXISTS company_table (
        cik INT,
        EntityName VARCHAR(100),
        Taxonomy VARCHAR(100),
        Units VARCHAR(15),
        Standard VARCHAR(100),
        Start DATE,
        End DATE,
        Val VARCHAR(70),
        AccountNumber VARCHAR(20),
        FY YEAR,
        FP VARCHAR(5),
        Form VARCHAR(50),
        Filed DATE,
        Frame VARCHAR(15)
    )
'''

# Execute the CREATE TABLE query
mycursor.execute(create_table_query)

# Commit the changes
mydb.commit()

# Insert data into the table
for index, row in extracted_data.iterrows():
    insert_query = '''
        INSERT INTO company_table (cik, EntityName, Taxonomy, Units, Standard, Start, End, Val, AccountNumber, FY, FP,Form, Filed, Frame)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)
    '''
    # Execute the INSERT INTO query
    mycursor.execute(insert_query, (row['cik'], row['EntityName'], row['Taxonomy'],row['Units'], row['Standard'], row['Start'], row['end'], row['val'], row['accn'], row['fy'], row['fp'],row['form'], row['filed'], row['frame']))

# Commit the changes
mydb.commit()

# Close cursor and database connection
mycursor.close()
mydb.close()
