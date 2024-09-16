def get_volume_of_cuboid(length, width, height):
    return length * width * height

#print(get_volume_of_cuboid(6.3,2,5))


def mango(quantity, price):
    grupos = int((quantity/3))
    return ((grupos*3) - grupos) + (quantity - (grupos*3)) * price
print(mango(864, 4105))