
class Restaurant:
    def open(self):
        self.is_open = True
        print(f"The restaurant is now open with {self.tables} tables!")
        
    def __init__(storage, t, num_of_staff):
        storage.tables = t
        storage.staff = num_of_staff
        storage.is_open = False


madrid_location = object.__new__(Restaurant)
Restaurant.__init__(madrid_location, 15, 6)


london_location = Restaurant(40, 18)

madrid_location.open()
london_location.open()

print(madrid_location)




