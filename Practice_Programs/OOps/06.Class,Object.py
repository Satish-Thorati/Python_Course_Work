#6. Movie Rating Check
'''Problem: Create a Movie class with method to check if movie is suitable for kids.
Answer:'''

class Movie:
     def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating
     def is_family_friendly(self):
        return self.rating < 13

# Use case
m1 = Movie("Finding Nemo", "Animation", 8)
print("Family Friendly:", m1.is_family_friendly())