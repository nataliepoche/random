# Base class
class Store:
    # Both are class attributes, shared among all Store and Grocery objects
    sales = 0
    costs = 0

    # Constructor for the base class
    def __init__(self, store_id, location):
        self.sales = 0
        self.costs = 0
        self.store_id = store_id
        self.location = location
        self.inventory = []

    # Instance method to fill inventory with junk
    def fill_inventory(self):
        for _ in range(10):
            self.inventory.append("junk")

    def get_sales(self):
        return self.sales

    def get_costs(self):
        return self.costs

    # cls refers to the class (i.e. Store), whereas store refers to a particular instance
    @classmethod
    def make_sale(cls, store, sale):
        store.sales += sale
        cls.sales += sale

    # Notice the static method does not access any instance attributes, i.e. no self variables
    @staticmethod
    def calculate_profit(sales, costs):
        return sales - costs

    # Define what to be printed when we print the instance directly
    def __str__(self):
        return f"Store #{self.store_id} is located in {self.location}. Its profit is {self.sales - self.costs}."

    # Define how we want to compare two instances with == operator
    def __eq__(self, other):
        return self.store_id == other.store_id


# Derived class
class Grocery(Store):
    # Constructor for the derived class
    def __init__(self, store_id, location):
        # Essentially just calling the base constructor
        super().__init__(store_id, location)

    # Override the base method for fill_inventory
    def fill_inventory(self):
        self.inventory = ["fruits", "veggies", "snacks", "drinks", "meat"]

    # Hmm, what about the class variable for costs?
    def food_expired(self):
        self.costs += 25


def main():
    pass


if __name__ == "__main__":
    main()