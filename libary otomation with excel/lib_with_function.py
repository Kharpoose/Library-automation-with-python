from openpyxl import Workbook, load_workbook


wb = Workbook()
ws = wb.active
ws.title = "Library"


ws.append(['Books Name', 'date of borrowing the book',
          'date of return of the book', 'the person who rented the book'])


def Library():
    aaa = True
    while aaa == True:
        book_name = input("input name a book: ")
        timein = input("the date the book was checked out: ")
        timeout = input("input the return date: ")
        name = input("Who is taking the book? ")

        ws.append([book_name, timein, timeout, name])

        b = str(input("print exit if you want to exit otherwise print anything"))

        if b == "exit":
            aaa = False
        wb.save('libraryNew.xlsx')


Library()
