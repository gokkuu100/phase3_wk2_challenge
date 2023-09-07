class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.restaurants = []
        self.reviews = []
        Customer.all_customers.append(self)

    def set_given_name(self, new_given_name):
        self.given_name = new_given_name

    def set_family_name(self, new_family_name):
        self.family_name = new_family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def given_name(cls, customer):
        return customer.given_name

    @classmethod
    def family_name(cls, customer):
        return customer.family_name

    @classmethod
    def all(cls):
        return cls.all_customers

    def add_restaurant(self, new_restaurant):
        self.restaurants.append(new_restaurant)

    def num_reviews(self):
        return len(self.reviews)

customer = Customer("Ken", "Walibora")
print(customer.full_name())

customer.set_given_name("Prince")
customer.set_family_name("Hope")

print(customer.given_name)  
print(customer.family_name) 

all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name())
