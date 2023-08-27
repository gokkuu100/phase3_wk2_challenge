class Review:
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def get_customer(self):
       return self.customer
    
    def get_restaurant(self):
       return self.restaurant

    def get_rating(self):
        return self.rating

    def all(self):
     allReview = [self.customer, self.restaurant, self.rating]
     return allReview
    
review1 = Review("Fabz", "Kingfisher", 5)
review2 = Review("Biggie", "McFry", 8)

print(review1.get_rating())
print(review1.all())