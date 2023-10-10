class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price

        #SSOT
        coffee._orders.append(self)
        coffee._customers.append(customer)
        customer._orders.append(self)
        customer._coffees.append(coffee)

        Order.all.append(self)
    
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        from Customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else: 
            raise Exception("Customer must be an instance of Customer class")
        
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        from Coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else: 
            raise Exception("Coffee must be an instance of Coffee class")
    
    @property 
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        if type(price) == float and 1.0 <= price <= 10.0 and not hasattr(self, "price"):
            self._price = price
        else: 
            raise Exception("Prices must be of type float and Price must be a number between 1.0 and 10.0, inclusive")