
class Restaurant:
    def open(self):
        Restaurant.is_open = True
        print("The restaurant is now open!")
        
    def __init__(storage, t, num_of_staff):
        storage.tables = t
        storage.staff = num_of_staff
        storage.is_open = False




madrid_location = Restaurant(15, 6)

print(dir(madrid_location))
# Restaurant.__init__(madrid_location, 15, 6)




london_location = Restaurant(40, 18)

madrid_location.open()
london_location.open()




