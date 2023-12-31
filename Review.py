class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def get_rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

    @classmethod
    def get_customers(cls):
        return list(set([review.customer for review in cls.all_reviews]))

review1 = Review("Fabz", "Kingfisher", 5)
review2 = Review("Biggie", "McFry", 8)

print(review1.get_customers())  