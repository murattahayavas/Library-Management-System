class Library:
    def __init__(self):
        self.file=open("books.txt","a+")
    
    def list_books(self):
        self.file.seek(0)
        the_books=self.file.read().splitlines()
        if not the_books:
            print("There is no book in the library.")
        else:
            for book in the_books:
                content=book.split(",")
                print("Book Name:",content[0])
                print("Author:",content[1])
                print("Release Date:",content[2])
                print("Pages:",content[3])
                print()            
            
    def add_book(self):
        name=input("Book Name: ")
        author=input("Author: ")
        release_date=input("Release Date: ")
        page_numbers=input("Pages: ")
        package=f"{name},{author},{release_date},{page_numbers}\n"
        self.file.write(package)
        print("The book succesfully added to library.")

    def remove_book(self,name):
        self.file.seek(0)
        content=self.file.readlines()
        new_library=[]
        tmp=False

        for book in content:
            if name.lower() not in book.lower():
                new_library.append(book)
            else: tmp=True

        if tmp:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(new_library)
            print("The book succesfully removed.")
        else: print("There is no book as this name.")

lib=Library()

while True:

    print("***MENU***")
    print("1)List Books")
    print("2)Add Book")
    print("3)Remove Book")
    print("4)Exit")

    choice=int(input("Your Choice:"))

    if choice==1:
        lib.list_books()
    elif choice==2:
        lib.add_book()
    elif choice==3:
        title=input("Enter the name of book you want to remove from library: ")
        lib.remove_book(title)
    elif choice==4:
        break
    else: print("Unvalid choice.\nPlease try again.")


