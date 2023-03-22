
class House():
    counter = 0
    def __init__(self, address, area, price) -> None:
        self.address = address
        self.area = area
        self.price = price
        House.counter += 1

        House.quality = 'low' # class variable
        self.quality = 'medium' # instance variable
        quality = 'high' # local variable (not accessible except within this exact method)

    def present(self):
        print('The house at', self.address, 'has an area of', self.area, 'and costs', self.price)

soho_house = House('12 Lexington St, Soho', 130, 540000)
soho_house.present()
print(House.counter)

print(House.quality)
print(soho_house.quality)

# it is possible to provide a default value for 'self' param, but python ignores it
# this is odd, but I feel like it follows the python philosophy - there is a proper way, but you can easily hack around it
