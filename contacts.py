import sqlite3
import DBHelpler.dbHelper as db
import argparse
from operations import Operations as OPS


def parse_arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument('--ops',help="specify type of operation",default=OPS.FETCH.value)
    parser.add_argument('--name',help="pass the name to be inserted",default='')
    parser.add_argument('--phone',help="pass the phone number",default='')
    args=parser.parse_args()
    d=vars(args)
    return d
    
def fetch_contact_list():
    conn=db.getConnection()    
    c=conn.cursor()
    rows=c.execute("select * from contacts")
    records=rows.fetchall()
    if len(records) > 0:
        for record in records:
            print(record)
    else:
        print('No Data to display')
        
def insert_contact(name,phone):
    sql='INSERT INTO contacts (contactname,phone) VALUES (\'{}\',\'{}\')'.format(name,phone)
    db.execSQL(sql) 

def contacts_operations():
    args=parse_arguments()
    operation=args['ops']
    name=args['name']
    phone=args['phone']
    if operation==OPS.CREATE.value:
        db.execSQL("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY AUTOINCREMENT , contactname text, phone text)")
    elif operation==OPS.FETCH.value:
        fetch_contact_list()
    elif operation==OPS.INSERT.value:
        insert_contact(name,phone)
    else:
        print('operation not found')    
   
if __name__ == "__main__":
    contacts_operations()    