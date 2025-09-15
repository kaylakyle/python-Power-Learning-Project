# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"
    

# Child Class (Inheritance + Encapsulation example)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # inherit from Device
        self.__storage = storage         # encapsulated (private attribute)
        self.battery = battery

    def get_storage(self):
        return self.__storage            # controlled access
    
    def charge(self):
        print(f"{self.device_info()} is charging ")

    def use(self, hours):
        self.battery -= hours * 10
        print(f"{self.device_info()} battery left: {self.battery}%")

# --- Testing the class ---
phone1 = Smartphone("Samsung", "S22", "128GB", 100)
phone1.charge()
phone1.use(3)
print("Storage:", phone1.get_storage())
