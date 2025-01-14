class publisher:
    def __init__(self,name):
        self.name=name
    def display():
        pass
class book(publisher):
    def __init__(self,name,title):
        super().__init__(name)
        self.title=title
    def display():
        pass
class python(book):
    def __init__(self,name,title,author):
        super().__init__(name,title)
        self.author=author
    def display(self):
        print("book details")
        print("name : ",self.name)
        print("title : ",self.title)
        print("author : ",self.author)

name=input("name")
title=input("title")
author=input("author")
b=python(name,title,author)
b.display()