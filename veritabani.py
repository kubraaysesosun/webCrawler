import sqlite3

con=sqlite3.connect("idefix.db")
cursor=con.cursor()

def veri_ekle(book_name,book_link,book_author,book_price):
    cursor.execute("Insert into Idefix VALUES(?,?,?,?)", (book_name,book_link,book_author,book_price))
    con.commit()
def bkmkitap_veri_ekle(book_name,book_link,book_author,book_price):
    cursor.execute("Insert into bkmKitap VALUES(?,?,?,?)", (book_name,book_link,book_author,book_price))
    con.commit()

def read_data_link():
    cursor.execute("Select book_link From Idefix")
    liste=cursor.fetchall()
    return liste
def read_data_name():
    cursor.execute("Select book_name From Idefix")
    liste=cursor.fetchall()
    return liste
def read_data_author():
    cursor.execute("Select book_author From Idefix")
    liste=cursor.fetchall()
    return liste
def read_data_price():
    cursor.execute("Select book_price From Idefix")
    liste=cursor.fetchall()
    return liste
def bkmkitap_read_data_link():
    cursor.execute("Select book_link From bkmKitap")
    liste=cursor.fetchall()
    return liste
def bkmkitap_read_data_name():
    cursor.execute("Select book_name From bkmKitap")
    liste=cursor.fetchall()
    return liste
def bkmkitap_read_data_author():
    cursor.execute("Select book_author From bkmKitap")
    liste=cursor.fetchall()
    return liste
def bkmkitap_read_data_price():
    cursor.execute("Select book_price From bkmKitap")
    liste=cursor.fetchall()
    return liste
#if __name__ == '__main__':
 #   read_data()