#Back end part
import sqlite3

def connect():   #db connection
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integere, isbn integer)")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):    #allows you to insert new entries.
    conn=sqlite3.connect("books.db") #need top 2 db connection lines to create new connection
    cur=conn.cursor() #need a cursor object to navigate through the db
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn)) #NULL takes the 4 parameters as place holders and aligns it with user input.
    conn.commit()  #                               adds in this order ^^^^
    conn.close() #commit changes and close connection


def view():   #this allows you to view all the data
    conn=sqlite3.connect("books.db") 
    cur=conn.cursor()
    cur.execute("SELECT * FROM book") #selects all the data from the database
    rows=cur.fetchall() #stores all the selected data in rows variable. fetches all rows returned from query
    conn.close() 
    return rows

def Search(title="",author="",year="",isbn=""): #pass empty strings so you can search for each parameter individually instead of needing to enter all 4.
    conn=sqlite3.connect("books.db") 
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()                              #place holders for user input in those boxes. pass the tuple of parameters as the 2nd arugment.
    conn.close() 
    return rows


def delete(id): #select one record and delete. need to grab the list selection from list box as a tuple. that tuple has a unique id. refer to the id, go to db table, and delete the row with that id
    conn=sqlite3.connect("books.db") 
    cur=conn.cursor() 
    cur.execute("DELETE FROM book WHERE id=?",(id,)) #id place holder is = to id parameter
    conn.commit()                                
    conn.close() 
#from tuple get id with index of 0 and passes to delete function

def update(id,title,author,year,isbn):  #select row, values of row displays, change cell in entry and press update. get list from list box and refer to id and get new values.
    #      ^^^^ update tables with this new value where id is equal to this
    conn=sqlite3.connect("books.db") 
    cur=conn.cursor() 
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id)) #update ? where id equals to tuple
    conn.commit()                                
    conn.close()


connect()