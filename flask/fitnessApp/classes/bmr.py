class BMRClass:
    def __init__(self, gender, age, weight, height):
        self.gender = gender
        self.age = age
        self.weight = weight 
        self.height = height

    def calculate(self):
        if self.gender.lower() == "male":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        elif self.gender.lower() == "female":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        else:
            raise ValueError("Gender must be male or female")
        return bmr




