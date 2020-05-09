
class Restaurant:
    def __init__(self, t, num_of_staff):
        self.tables = t
        self.staff = num_of_staff
        self.is_open = False
    

    def open():
        Restaurant.is_open = True
        print("The restaurant is now open!")



madrid_location = Restaurant(15, 6)
london_location = Restaurant(40, 18)

print(madrid_location["tables"])
print(london_location["tables"])


