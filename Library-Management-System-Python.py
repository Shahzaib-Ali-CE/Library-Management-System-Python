issued_books=[]
books=["History of World","Thief","The Spinner Tale","Algorithms"]
Serial_Number=[12101,12102,12103,12104]
Location=["A1","A2","A3","B1"]

def information():
    book = input("Enter Book Name: ")
    number = int(input("Enter Serial Number: "))
    section = input("Enter Section (Like-B1): ")
    return book, number, section

print("Welcome to Air University Library Management")
print("Enter 1 for View Library Menu")
print("Enter 2 for Exit")
choose = int(input("Please choose an option from given above: "))
while choose==1:
    print("1. Add Books \n2. Remove Books \n3. Search Book \n4. Issue Book \n5. Record")
    option = int(input("Please select option from given above: "))
    if option==1:
        book,number,section = information()
        books.append(book)
        Serial_Number.append(number)
        Location.append(section)
        print("Your Book", book, "has been added successfully")

    elif option==2:
        book_remove = input("Enter Book Name to remove: ")
        for i in books:
            if i == book_remove:
                index1=books.index(i)
                books.pop(index1)
                Serial_Number.pop(index1)
                Location.pop(index1)
                print("Your Book", book_remove, "has been removed successfully")
                break
        else:
            print("Book not found!")

    elif option==3:
        select = input("Enter Book which you want to search: ")
        for i in books:
            if i==select:
                index2=books.index(i)
                print("Book Found")
                print(books[index2])
                print("Serial Number is ", Serial_Number[index2])
                print("It is placed in Section ", Location[index2])
                break
        else:
            print("Book not found!")

    elif option==4:
        name=input("Enter Name of Person: ")
        Reg_Number=int(input("Enter Registration Number: "))
        book_issue=input("Enter Book Name which you want to issue")
        for i in books:
            if i == book_issue:
                index3=books.index(i)
                issued_books.append(i)
                books.pop(index3)
                Serial_Number.pop(index3)
                Location.pop(index3)
                print("Your Book", book_issue, "has been issued to", name, "successfully")
                break
        else:
            print("Book not found!")

    elif option==5:
        print("Available Books: ")
        for x in books:
            print(x)
        print("Issued Books: ")
        for x in issued_books:
            print(x)

    elif option!=5 and option!=4 and option!=3 and option!=2 and option!=1:
        print("Invalid Input!")

    choose = int(input("Enter 1 for Main Menu or Any other key for Exit "))

print("Exiting Library Management System. Have a productive day!")
