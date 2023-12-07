class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def information(self):
        return (self.title, self.author, self.pages)

# Creating an instance of Book
book_1 = Book('Oliver Twist', 'Charles Dickens', '2000 pages')



    #creating a serived class "EBook" that inherits from the Book class
Ebook=Book('Things fall apart', 'Chinua Achebe' '300pages')
print(Ebook)
    
   
 #additional attribute "format" to the Ebook class.  display information for an instance of the Ebook class
    
    
    
    
    
 #(iii) function that returns only the title and its author
def returns_only_title_and_author()
        return ({'title'}, {'author'})
returns_only_title_and_author()
    
    
    #(iv) Class