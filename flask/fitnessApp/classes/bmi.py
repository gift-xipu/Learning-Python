class BMIClass:
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height

    def calculate(self):
        return self.weight /(self.height**2)

