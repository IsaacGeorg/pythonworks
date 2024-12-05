
class Movie:
    def set_movie(self,title,rating,run_time,director,genre):
        self.title=title
        self.rating=rating
        self.run_time=run_time
        self.director=director
        self.genre=genre

    def display_movie(self):
        print(self.title,self.rating,self.run_time,self.genre)

movie1=Movie()
movie2=Movie()
movie1.set_movie("ARM",4.6,"2Hrs 30 Minutes","Venugopal","Thriller")
movie2.set_movie("KGF",4.8,"2Hrs 45 Minutes","Hombale","Action")
movie1.display_movie()
movie2.display_movie()



class Cake:
    def __init__(self,title,price):
        self.title=title
        self.price=price
    
    def display(self):
        print(self.title,self.price)

cakeinstance1=Cake("Blueberry",1200)
cakeinstance1.display()
cakeinstance2=Cake("Hazelnut",1200)
cakeinstance2.display()
cakeinstance3=Cake("Mango Cake",1000)
cakeinstance3.display()


# initializing attributes (instance variables)
# constructor

# initializing instance variables ==> Constuctor

#  __init__

# when object is created, constructor will automatically call the object
