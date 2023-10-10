class Coffee:
    def __init__(self, name):
        self._name = name
        self._orders = []
        self._customers = []
    
    @property 
    def coffee_name(self):
        return self._name

    @coffee_name.setter
    def coffee_name(self, name):
        if type(name) == str and len(name) >= 3 and not hasattr(self,"name"):
            self._name = name
        else: 
            raise Exception("coffee name must be a string with 3 or more characters")
        
    def orders(self):
        return self._orders
    
    def customers(self):
        return list(set(self._customers))
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        return sum([order.price for order in self._orders]) / len(self._orders)
    
        total_price = 0

        for order in self._order:
            total_price = total_price + order.price
        
        avg = total_price / len(self._orders)

        return avg
