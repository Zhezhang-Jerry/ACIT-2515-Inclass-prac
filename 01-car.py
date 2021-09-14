"""
Complete the file with your own code below. Replace this comment with your name and student number.
"""

class Car:
    """
    This class represents a car. Complete it as required.
    """
    def __init__(self, make, model, electric=False, mileage=0): # Complete and add
        self.make = make
        self.model = model
        self.electric = electric
        self._mileage = float(mileage)

        self.is_driving = False

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        value = float(value)
        if value < 0:
            raise ValueError

        self._mileage = value

    def drive(self):
        self.is_driving = True

    def stop(self, distance_driven=0):
        distance_driven = float(distance_driven)

        if distance_driven < 0:
            raise ValueError

        self.is_driving = False
        self._mileage = self._mileage + distance_driven

    def get_description(self):
        return f'{self.make}, {self.model}, {self._mileage}kms'

def test_code_1():
    """
    Code that helps test part 1 of the lab
    """
    chevrolet = Car("Chevrolet", "Suburban")
    print("Checking the 'get_description' method...")
    description = chevrolet.get_description()
    print(description)

    print("Checking the 'mileage' property...")
    assert chevrolet._mileage == 0

    toyota = Car("Toyota", "Prius", mileage="100000", electric=True)
    print("Checking the 'electric' attribute")
    assert toyota.electric is True
    assert toyota._mileage == 100000

def test_code_2():
    """
    Code that helps test part 2 of the lab
    """
    chevrolet = Car("Chevrolet", "Suburban")

    print("Setting car to drive...")
    chevrolet.drive()
    assert chevrolet.is_driving is True

    print("Stopping car...")
    chevrolet.stop()
    assert chevrolet._mileage == 0
    chevrolet.drive()
    chevrolet.stop(distance_driven="10000")
    assert chevrolet._mileage == 10000

def test_code_3():
    """
    Code that helps test part 3 of the lab
    """
    chevrolet = Car("Chevrolet", "Suburban")
    chevrolet.drive()
    chevrolet.stop("10000")
    assert chevrolet.mileage == 10000

    chevrolet.mileage = 1000
    chevrolet.drive()
    chevrolet.stop(1000)
    print(chevrolet._mileage)
    assert chevrolet.mileage == 2000


if __name__ == "__main__":
    # You can also write your own code below to test your code
    test_code_1()
    test_code_2()
    test_code_3()



    # car = Car("Toyata", "Corolla", mileage=35000)
    # print(car.get_description())

    # car.drive()
    # print(car.is_driving)

    # car.stop()
    # print(car.get_description())

    # car.drive()
    # car.stop("5425324234235")
    # print(car.get_description())