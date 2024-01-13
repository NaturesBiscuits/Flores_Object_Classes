import math


class Circle:
    def __init__(self):
        while True:
            try:
                self.radius = float(input("Enter the radius of the circle: "))
                if self.radius > 0:
                    break
                else:
                    print("Invalid radius. Please enter a positive value.")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

    def area(self):
        area = math.pi * self.radius**2
        print(f"The area of the circle is: {area:.2f}")

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print(f"The perimeter of the circle is: {perimeter:.2f}")


circle = Circle()

circle.area()
circle.perimeter()
