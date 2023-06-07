class ShapeAreaCalculator:
    def __init__(self):
        self.data = []  # List to store the entered data and calculations
        self.counter = 1  # Counter to track the number of inputs

    def get_inputs(self):
        height = int(input("Enter height: "))
        base = int(input("Enter base: "))
        return height, base

    def calculate_areas(self):
        while True:
            height, base = self.get_inputs()

            # Calculate the areas using the given height and base
            triangle_area = height * base // 2
            square_area = height * base
            rectangle_area = height * base * 2

            # Store the data and calculations in a dictionary
            calculations = {
                "Height": height,
                "Base": base,
                "Triangle Area": triangle_area,
                "Square Area": square_area,
                "Rectangle Area": rectangle_area
            }

            # Append the dictionary to the data list
            self.data.append(calculations)

            # Prompt the user if they want to calculate again
            choice = input("Do you want to calculate again? (y/n): ")
            if choice.lower() == "n":
                break

            # Increment the counter
            self.counter += 1

    def display_results(self):
        print("===========================================")
        print("Results:")
        for i, calculations in enumerate(self.data, start=1):
            print(f"Calculations for Area {i}")
            print("-------------------------------------------")
            for key, value in calculations.items():
                print(f"{key}: {value}")
            print("-------------------------------------------")
        print("===========================================")


# Usage example:
calculator = ShapeAreaCalculator()
calculator.calculate_areas()
calculator.display_results()
