class Book:
    def __init__(self,title, author, publication_year, genre, num_pages):
        self.title = title
        self.author = author
        self.publication_year=publication_year
        self.genre = genre
        self.num_pages = num_pages

    def read(self, pages):
        self.pages = pages
        num_pages = self.num_pages - pages
        print("Number of Pages remains to read: ", num_pages)

    def change_genre(self, new_genre):
        new_genre == self.genre
        print("Genre Updated: ",new_genre)

    def get_age(self):
        current_year=2019
        # self.current_year = current_year
        age =(current_year) - (self.publication_year)
        print(f"Age of the Book is {age} Years ")


bk = Book("Vision-2020", "Chetan Bhagat", 2015, "Genre1", 200)
bk.read(130)
bk.change_genre("newGenre")
bk.get_age()







