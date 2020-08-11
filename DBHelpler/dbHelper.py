import sqlite3

def getConnection():
    conn=None
    if conn == None: 
        conn = sqlite3.connect('mycontacts.db')    
        return conn
    else:
        return conn
    
def execSQL(sql):
    conn=getConnection()    
    c=conn.cursor()
    c.execute(sql)
    print("Executing SQL: {}".format(sql))
    conn.commit()
    