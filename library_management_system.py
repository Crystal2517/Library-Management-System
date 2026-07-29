import os
import csv
print("Library Management system")

def load_books(): # function to load all the previously added and saved books
    books = []
    if os.path.getsize("books.csv") == 0: # checks if nothing is in the csv file if true return empty list
        return books
    with open("books.csv", "r", newline="") as file: # opens csv file in read mode
        reader = csv.reader(file)
        next (reader) # skips header 
        for row in reader: # goes through every row
            if not row: # skips any empty row 
                continue
            books.append({"Title": row[0],
                          "Author": row[1],
                          "available": (row[2]) == "True"
                        }) # turns each row into the format above and adds to book list
    return (books) # returns list of books that were previously saved in the csv file

books = load_books()


while True:
    print("""
    1. Add book
    2. View books
    3. Borrow book
    4. Return book
    5. Search book
    6. Exit""")

    option = int(input("Choose an option: "))

    if option ==1:
        amount_to_add = int(input("Enter how many books you would like to add: "))
        for book in range(amount_to_add): # loop to allow for multiple book entries
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            available = True
            books.append({"Title": title,
                          "Author": author,
                          "available": True
                          }) # stores books as a dictionary as a list

            file_empty = os.path.getsize("books.csv") == 0 # checks if book CSV file is empty
            with open ("books.csv", "a", newline="") as file:
                writer = csv.writer(file) 
                if file_empty: # If empty it writes the header first
                    writer.writerow(["Title" , "Authour" , "Availability"]) 
                writer.writerow([title, author, True]) # adds book to file

    if option ==2:
        if not books: # checks if books is empty
            print("No books found")
        for index,book in enumerate(books, start=1): # enumerates starting from 1
            if book["available"] == True:
                status = "Available"
            elif book["available"] == False:
                status = "Borrowed"
            print(f"{index}. {book['Title']} - {book["Author"]} - {status}")

    if option == 3:
        if not books:
            print("no books found")
        else:
            borrow_title = input("Enter the name of the book to borrow: ")
            borrow_author = input("Enter the Authors name of the book to borrow: ")
            for book in books:
                if borrow_title == book["Title"] and borrow_author == book["Author"]: # finds book
                    book["available"] = False
                    print(f"{book['Title']} has been borrowed.") # if found changes availability to borrowed
                    break
            else:
                print("book not found")

    if option == 4:
        if not books:
            print("No books found.")
        else:
            return_title = input("Enter the name of the book to return: ")
            return_author = input("Enter the Authors name of the book you are returning: ")
            for book in books: 
                if return_title == book["Title"] and return_author == book["Author"]: # searches through file to find matching book
                    book["available"] = True
                    print(f"{book['Title']} has been returned")
                    break # stops once found
            else:
                print("Book not found")

    if option == 5:
        if not books:
            print("No books found")
        else:
            search_title = input("Enter the name of the book: ") 
            search_author = input("Enter the Authors name of the book: ")
            for book in books:
                if search_title == book["Title"] and search_author ==book["Author"]: # searches for matching book in file
                    if book["available"] == True:
                       status = "Available"
                    elif book["available"] == False:
                        status = "Borrowed"
                    print(f"{book['Title']} - {book["Author"]} - {status}.") # prints the book that was searched for
                    break # stops once found
            else:
               if search_title!= book["Title"]:
                   print("No book found") # handles invalid inputs

    if option == 6:
        print("Thank you for using library management system!")
        break

else:
    print("Invalid option please pick between 1-6")



            







