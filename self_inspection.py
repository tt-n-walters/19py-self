
class Restaurant:
    def create_new():
        storage = {}
        storage["tables"] = 10
        storage["staff"] = 6
        storage["is_open"] = False
        return storage
    
    
    def open():
        Restaurant.is_open = True
        print("The restaurant is now open!")



madrid_location = Restaurant.create_new()
london_location = Restaurant.create_new()

print(madrid_location["tables"])


