if __name__ == "__main__":
    import csv

    books = '''author,book
    J R R Tolkien,The Hobbit
    Lynne Truss,"Eats, Shoots & Leaves"'''

    with open("books.csv", "w") as fp:
        fp.write(books)
