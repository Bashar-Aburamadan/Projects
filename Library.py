
from  datetime import timedelta,date
from time import sleep
import random
import  sys

users = []
librarians = []
books = []
borrowed_order = []

class Client:
    def __init__(self , full_name ,age , id_no , phone_number ):
        self.__id = random.randint(1,1000)
        self.__full_name = full_name
        self.__age = age
        self.__id_no = id_no
        self.__phone_number = phone_number

    def get_id(self):
        return self.__id

    def set_full_name(self , name):
        self.__full_name = name
    def set_age(self , age):
        self.__age = age
    def get_id_no(self ):
        return self.__id_no
    def set_phone_number(self , phone_number):
        self.__phone_number = phone_number

    def info(self):
        print({
            'Id : ' : self.__id,
            'Full name : ' : self.__full_name,
            'Age : ' : self.__age,
            'id_no : ' : self.__id_no,
            'Phone number : ' : self.__phone_number
        })
class Librarian(Client):
    def __init__(self, full_name ,age , id_no , phone_number , salary = 0.0):
        super().__init__( full_name ,age , id_no , phone_number)
        self.__salary = salary

    def get_salary(self):
        return self.salary

    def info(self):
        return {
            'id' : self.__id,
            "full_name" : self.__full_name,
            "age" : self.__age,
            'id_no': self.__id_no,
            "phone_number" :self.__phone_number,
            'Salary': self.__salary
        }
class Book:
    def __init__(self , title , description , author ):
        self.__id = random.randint(1,1000)
        self.__title = title
        self.__description = description
        self.__author = author
        self.__status = 'Not ordered'

    def get_id(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_description(self):
        return self.__description
    def get_author(self):
        return self.__author
    def get_status(self ):
        return self.__status

    def display(self):
        return {
            'Book Id : ' : self.__id,
            'Title : '  : self.__title,
            'Description : ' : self.__description,
            'Author : ' : self.__author,
            'State : ' : self.__status
        }
class Borrowing_order:
    def __init__(self , book_id , cliend_id , status):
        self.__start_data = date.today()
        self.__end_data = date.today() + timedelta(days=int(input('your days : ')))
        self.__book_id = book_id
        self.__cliend_id = cliend_id
        self.__status = status

    def get_start_data(self):
        return self.__start_data
    def get_end_data(self):
        return self.__end_data
    def get_book_id(self):
        return self.__book_id
    def get_cliend_id(self ):
        return self.__cliend_id
    def get_status(self ):
        return self.__status
    def display(self):
        return {
            'Book ID : ' : self.__book_id,
            "Client ID" : self.__cliend_id,
            "Status now " : self.__status,
            'Start day ': self.__start_data,
            "End day" :self.__end_data
        }



def add_client():
    print('************************')
    users.append(Client(str(input("Your name : ")),int(input('Your age : ')),str(input('Your ID number : ')),int(input('Your phone number : '))))
    print('--------------------------')

def add_librarians():
    print('************************')
    for i in range(int(input("How many Librarian : "))):
        librarians.append(Librarian(str(input("His name : ")),int(input('His age : ')),str(input('His ID number : ')),int(input('His phone number : ')) , int(input('His Salary : '))))
        print('------------------------')

def borrow_books():
    print('*****************************')
    for j in books:
        print(j.display())
    bk = int ( input('-------> Select your book : '))
    for i in range (len(books)):
        if bk == ( books[i].get_id() ):
            print('its here : ' , bk)
            borrowed_order.append(Borrowing_order(bk , int(input('Enter your ID : ')) ,'Ordered' ))
            if len(users) == 0 :
                msg = "------------------\n Please Add client to order !"
                print(sys.exit(msg))
            else:
                del books[i]

                print('*************************************\n' , 'Your order : ')
                for i in range(20):
                    print(".", end="")
                    sleep(0.1)
                print("\n")

            for info in borrowed_order:

                print(info.display())


            break

    print('**************************************')
    print("*******************")
    for j in books:
        print("----Books currently available---")
        print(j.display())

def return_book():
    rb = int ( input('-------> Select your book : '))
    for i in range (len(borrowed_order)):
        if rb == ( borrowed_order[i].get_book_id() ):
            books.append(borrowed_order[i])
books.append(Book('In Search of Lost Time','Swanns Way, the first part of A la recherche de temps perdu','Marcel Proust'  ))
books.append(Book('Ulysses ','Ulysses chronicles the passage of Leopold Bloom through Dublin during an ordinary day','James Joyce'  ))
books.append(Book('Don Quixote','Alonso Quixano, a retired country gentleman in his fifties','Miguel de Cervantes'  ))
books.append(Book('The Great Gatsby','The novel chronicles an era that Fitzgerald himself dubbed the ','F. Scott Fitzgerald'  ))
books.append(Book('Moby Dick','First published in 1851, Melvilles masterpiece is, in Elizabeth Hardwicks words','Herman Melville'  ))
books.append(Book('War and Peace','Epic in scale, War and Peace delineates in graphic detail events leading up to Napoleons invasion of Russia','Leo Tolstoy'  ))


while True:
    print("\n")
    print("Program is running")
    for i in range(25):
        print(".", end="")
        sleep(0.1)
    print("\n")
    try:
        print("--------------------------- Welcome to the Alaa Library ----------------------------------")
        choice = int(input("1.Add Client\n2.Add Librarian\n3.Borrow book\n4.Return Book\n5.Exit\nWhat do you want to do? :"))
        if choice == 1 :
            add_client()
        if  choice == 2 :
            add_librarians()
        if choice == 3 :
            borrow_books()
        if choice == 4 :
            return_book()
        if choice == 5 :
            print("Signing out")
            for i in range(30):
                print(".", end="")
                sleep(0.2)
            msg="\n Good-bye"
            print(sys.exit(msg))
        else:
            msg = "\n The number entered is not in the list\n Please run the program again. \n"
            print(sys.exit(msg))
    except ValueError:
        print("\nOops!  The entry is incorrect. Please Try again...\n")


