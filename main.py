#Library to import Date
import datetime

#Function to search book name in book list
def is_book_present(b,b_list):
    book_found = False
    ind = 0

    #Loop to check the entered book name is present and if yes then returns the book details
    for one_book in b_list:
        ls = one_book.split(",")
        if ls[1]==b:
            book_found = True
            break
        ind=ind+1
    return book_found, ind

#Function to search student in student list
def is_student_present(e, st_list):
    stud_found = False
    ind = 0

    #Loop to check whether entered Enrollment number is present and if yes then returns the student details
    for one_stud in st_list:
        ls = one_stud.split(",")
        if ls[0]==e:
            stud_found = True
            break
        ind = ind + 1
    return stud_found, ind

#Function to enter date of issue and return of the book
def getdate():
    a = datetime.date.today()
    dt = str(a.day)+"/"+str(a.month)+"/"+str(a.year)
    return dt


#Function to issue book
def issue_book():
    stud_enr = input("Enter Student Enrollment Number:")
    b_no = input("Enter Book Number to be Issued:")
    cur_dt = getdate()

#Writing data to file in append mode
    fobj = open("all_issued_books.txt","a")
    fobj.write(stud_enr + ","+ b_no + "," + cur_dt +  ",NA\n" )
    fobj.close()
    print("Book Issued...")
    input()     #to add a pause

#Function to return book
def return_book():
    fobj = open("all_issued_books.txt","r")
    b_dt = fobj.readlines()
    fobj.close()

    curr_date = getdate()   #current date as date of return of book
    bnum = input("Enter Book Number to return:")
    ind=0
    #Loop to iterate over the length of book return date list
    while ind<len(b_dt):
        one_book = b_dt[ind]
        ls = one_book.split(",")
        if ls[1]==bnum and ls[3]=="NA\n":
            book_found = True
            ls[3]= curr_date + "\n"
            new_str = ",".join(ls)
            b_dt[ind]=new_str
            break
        ind = ind + 1

    if book_found==False:
        print("Invalid Book Number, No such book is issued...")
    else:
        fobj = open("all_issued_books.txt","w")
        fobj.writelines(b_dt)
        fobj.close()
        print("Book Returned..")
    input()

#Function to check not returned books
def not_ret_books():
    fobj = open("all_issued_books.txt","r")
    issued_list = fobj.readlines()
    fobj.close()

    #Loop to check the returned date as 'NA' and print its details
    for one_book in issued_list:
        ls = one_book.split(",")
        if ls[3]=="NA\n":
            print(ls[0], ls[1], ls[2], sep="\t\t\t")
    input()

#Function to print book details/history
def book_history():
    fobj = open("all_issued_books.txt", "r")
    issued_list = fobj.readlines()
    fobj.close()

    #Loop to check which student has currently issued this book
    bnum = input("Enter Book Number, to print History:")
    for one_book in issued_list:
        ls = one_book.split(',')
        if ls[1] == bnum:
            print(ls[0], ls[2], ls[3], sep="\t\t", end="")
    input()

#Function to check student details/history
def student_history():
    fobj = open("all_issued_books.txt","r")
    issued_list = fobj.readlines()
    fobj.close()

    #Loop to check what books were borrowed by the student
    enr = input("Enter  Enrollment Number of Student, to print History:")
    for one_book in issued_list:
        ls = one_book.split(",")
        if ls[0]==enr:
            print(ls[1], ls[2], ls[3], sep="\t\t", end="")
    input()

#Function to seacrh student details
def search_stud():
    enr = input("Enter Enrollment Number of Student to search:")
    fobj = open("all_stud.txt","r")
    st_list = fobj.readlines()
    fobj.close()

    found, ind = is_student_present(enr, st_list)

    if found==False:
        print("Invalid Enrollment Number...")
    else:
        ls = st_list[ind].split(",")
        print("Enrollment Number:",ls[0])
        print("Student Name:",ls[1])
        print("Student Email:",ls[2])
        print("Student Mobile Number:",ls[3])
        print("Student Class:",ls[4])
    input()

#Function to search book details
def search_book():
    bnm = input("Enter Book Name:")
    fobj  = open("all_book.txt","r")
    b_list = fobj.readlines()
    fobj.close()

    found, ind = is_book_present(bnm, b_list)

    if found==False:
        print("Invalid Book Name...")
    else:
        ls = b_list[ind].split(",")
        print("Book Number:",ls[0])
        print("Book Name:",ls[1])
        print("Book Author:",ls[2])
    input()

#Function to add a new book
def add_book():
    b_no = input("Enter Book Number:")
    b_title = input("Enter Book Title:")
    b_author = input("Enter Book Author:")
    b_pub = input("Enter Book Publication:")

    fobj = open("all_book.txt","a")
    fobj.write(b_no + ","+ b_title + ","+ b_author + ","+ b_pub+ "\n")
    fobj.close()
    print("Book Added Successfully...")
    input()

#Function to add new student
def add_stud():
    st_enr = input("Enter Student Enrollment Number:")
    st_nm = input("Enter Student Name:")
    st_mail = input("Enter Student E-Mail:")
    st_mob = input("Enter Student Mobile Number:")
    st_class = input("Enter Student Class:")

    fobj = open("all_stud.txt","a")
    fobj.write(st_enr+","+st_nm+","+st_mail+","+st_mob+","+st_class+"\n")
    fobj.close()
    print("New Student Added Successfully...")
    input()


#main program
while True:
    print("Select from below Options:")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Book History")
    print("4 - Student History")
    print("5 - Search Student")
    print("6 - Search Book")
    print("7 - Add New Book")
    print("8 - Add New Student")
    print("9 - Show not returned Books")
    print("10 - Exit")

    ch = int(input("Enter your choice:"))

    if ch==1:
        issue_book()
    elif ch==2:
        return_book()
    elif ch==3:
        book_history()
    elif ch==4:
        student_history()
    elif ch==5:
        search_stud()
    elif ch==6:
        search_book()
    elif ch==7:
        add_book()
    elif ch==8:
        add_stud()
    elif ch==9:
        books_not_returned()
    else:
        print("Thank You...")
        exit()
        fobj.close()




