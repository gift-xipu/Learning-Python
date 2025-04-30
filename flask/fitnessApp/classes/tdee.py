class TDEEClass:
    def __init__(self, bmr, activity_level):
        self.bmr = bmr
        self.activity_level

    def calculate(self):
        activity_factors = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'very': 1.725,
            'super': 1.9
        }
        factor = activity_factors.get(self.activity_level)
        if factor is None:
            raise ValueError("Invalid activity level.")
        return self.bmr * factor

