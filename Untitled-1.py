class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # Move to the beginning of the file
        lines = self.file.readlines()
        for line in lines:
            book_info = line.strip().split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        lines = self.file.readlines()
        self.file.seek(0)
        updated_lines = [line for line in lines if not line.startswith(title)]
        self.file.truncate(0)
        self.file.writelines(updated_lines)
        print(f"Book '{title}' removed successfully.")


lib = Library()

def print_menu():
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")

while True:
    print_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    else:
        print("Invalid choice. Please choose again.")
