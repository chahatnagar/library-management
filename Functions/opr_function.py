from vars import db

def add_name():
    global name
    name = input("Enter student's name:     ")
def add_bookcode():
    global book_code
    book_code = input("Enter book code:     ")

def add_user():
    add_name()
    add_bookcode()
    db[book_code] = name
    print("\nBook with code number,",book_code,"successfully issued to",name+".\n")

def del_user():
    add_bookcode()
    if book_code not in db:
        print("Book with code number,",book_code,"is not yet issued.")
    elif book_code in db:
        del db[book_code]
        print("Book with code number,",book_code,"successfully removed from the database.")

def book_status():
    add_bookcode()
    if book_code in db:
        print("Book with the following code number",book_code,"is issued to",db[book_code]+".")
    elif book_code not in db:
        print("Book is not yet issued:)")

def database():
    print("Sn. | ", "Book Code | ", "Issued by | ")
    a = 1
    for i in db:
        print(a,"  |", i,"    |", db[i])
        a+=1
