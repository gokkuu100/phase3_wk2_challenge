class Restaurant:
    def __init__(self,name):
        self.name = name
        self.reviews = []
        self.customers = []

    def get_name(self):
        return self.name
    
    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews
    
    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customers(self):
        return self.customers
    
    def average_star_rating(self):
        pass

rest1 = Restaurant("Kingfisher")
rest1.add_review(8)
rest1.add_review(10)
rest1.add_review(8)

rest1.add_customer("Fabz")
rest1.add_customer("Gokue")

print(rest1.get_reviews())
print(rest1.get_customers())