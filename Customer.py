from Restaurant import Restaurant
from Review import Review
class Customer:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.restaurants = []
        self.reviews = []

    def given_name(self):
        return self.fname
    
    def set_given_name(self, new_given_name):
        self.fname = new_given_name

    def family_name(self):
        return self.lname
    
    def set_family_name(self, new_family_name):
        self.lname = new_family_name
    
    def full_name(self):
        return self.fname + " " + self.lname
    
    def add_restaurants(self, new_restaurant):
        self.restaurants.append(new_restaurant)

    def num_reviews(self):
        return len(self.reviews)
        pass


customer = Customer("Ken", "Walibora")
print(customer.full_name())

print(customer.get_restaurants())
