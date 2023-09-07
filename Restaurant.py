class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []
        self.customers = set() 

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def add_review(self, rating):
        self.reviews.append(rating)

    def get_customers(self):
        return list(self.customers)

    def add_customer(self, customer):
        self.customers.add(customer)

    def average_star_rating(self):
        if not self.reviews:
            return 0  
        total_rating = sum(self.reviews)
        return total_rating / len(self.reviews)

rest1 = Restaurant("Kingfisher")
rest1.add_review(8)
rest1.add_review(10)
rest1.add_review(8)

rest1.add_customer("Fabz")
rest1.add_customer("Goku")

print(rest1.customers)
print(rest1.reviews)
print(rest1.average_star_rating())  
