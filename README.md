# Shape Area Calculator

The Shape Area Calculator is a Python program that allows you to calculate the areas of different shapes based on user inputs. It calculates the areas of triangles, squares, and rectangles using the provided height and base values.

## How to Use

1. Run the program in a Python environment.
2. You will be prompted to enter the height and base for the shape.
3. Once you provide the input, the program will calculate the areas of the triangle, square, and rectangle using the given values.
4. The calculated values, along with the input height and base, will be stored in a list.
5. After each calculation, you will be asked if you want to calculate again. Enter 'y' to continue calculating or 'n' to stop.
6. Once you choose to stop, the program will display the results, showing the calculations for each entered shape.

## Program Structure

The program is implemented as a class called `ShapeAreaCalculator`. It has the following methods:

### 1. `__init__(self)`

This method initializes the `ShapeAreaCalculator` object. It initializes an empty list `data` to store the entered data and calculations, and a counter `counter` to track the number of inputs.

### 2. `get_inputs(self)`

This method prompts the user to enter the height and base of the shape. It returns the entered values as a tuple.

### 3. `calculate_areas(self)`

This method performs the main logic of the program. It repeatedly calls `get_inputs()` to get the height and base values, calculates the areas of the triangle, square, and rectangle using the given values, and stores the data and calculations in a dictionary. The dictionary is then appended to the `data` list. The method also provides an option to continue or stop the calculation based on user input.

### 4. `display_results(self)`

This method displays the results of the calculations. It iterates over the `data` list and prints the calculations for each shape, including the height, base, and areas of the triangle, square, and rectangle.

## Example Usage

```python
calculator = ShapeAreaCalculator()
calculator.calculate_areas()
calculator.display_results()
```

This example creates a `ShapeAreaCalculator` object, performs the area calculations, and displays the results.

## Note

- The program assumes that the user will provide valid integer inputs for the height and base.
