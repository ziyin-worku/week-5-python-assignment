# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"


# Child Class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # calling parent constructor
        self.storage = storage  # in GB
        self.__battery = battery  # private attribute (encapsulation)
    
    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f"Battery charged to {self.__battery}%"
    
    def use(self, hours):
        self.__battery = max(0, self.__battery - (hours * 10))
        return f"Battery left: {self.__battery}%"
    
    def device_info(self):  # polymorphism (override parent method)
        return f"{self.brand} {self.model} - {self.storage}GB Storage, {self.__battery}% Battery"


# Example usage
phone1 = Smartphone("Apple", "iPhone 14", 256, 80)
phone2 = Smartphone("Samsung", "Galaxy S23", 512, 50)

print(phone1.device_info())
print(phone1.use(3))
print(phone1.charge(15))

print(phone2.device_info())
