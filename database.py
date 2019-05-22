import sqlite3
import seo


url=[]
tags=[]
density=[]
url,tags,density=seo.getData()




#DATABASE

conn=sqlite3.connect("MyData1.db")

try:            #Creates and inserts into table
    conn.execute('''create table tags (url text not null, keywords text not null, frequency int not null);''')
    for x in range(0,len(url)):
        conn.execute('''insert into tags (url,keywords,frequency) values (?,?,?)''',(url[x],tags[x],density[x]));
        conn.commit()
        
except:
    pass


finally:        #Getting data from seo.py for further use in search.py
    
    cursor=conn.execute("select url,keywords,frequency from tags")

    page=[]
    key=[]
    dense=[]
    
    for row in cursor:
        page.append(row[0])
        key.append(row[1])
        dense.append(row[2])


'''======================================================================='''

#For referencing in search.py

def getPages():
    return page

def getKeys():
    return key

def getDense():
    return dense


