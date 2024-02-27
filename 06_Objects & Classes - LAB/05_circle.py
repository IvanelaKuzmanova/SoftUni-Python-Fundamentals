class Circle:
    __pi = 3.14
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):          #using object parameters (no need to add them in the brackets if defined in __init__)
        return Circle.__pi * self.diameter     #to use the attribute we need to call the class.attribute; self.diameter means the diameter of the current object

    def calculate_area(self):
        return Circle.__pi * (self.radius ** 2)

    def calculate_area_of_sector(self, angle):         #using object parameters and adding angle parameter
        return (angle/360) * Circle.__pi * (self.radius ** 2)

#--------------------------------------------------------------------------------------------------------------------

current_diameter = float(input())       #input a diameter variable
current_angle = int(input())

circle = Circle(current_diameter)       #creating object with the new variable

print(circle.calculate_circumference(current_diameter))
print(circle.calculate_area(circle.radius))
print(circle.calculate_area_of_sector(current_angle))