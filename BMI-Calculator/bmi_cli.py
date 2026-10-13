
def calculate_bmi():
    while True:
        try:
            weight = float(input("Enter weight in kg: "))
            height = float(input("Enter height in meters: "))

            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be greater than zero.")
                continue

            bmi = round(weight / (height ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"

            print("\n--- BMI RESULT ---")
            print(f"BMI: {bmi}")
            print(f"Category: {category}")
            break

        except ValueError:
            print("Error: Please enter numeric values only.")


while True:
    calculate_bmi()

    again = input("\nCalculate again? (y/n): ").strip().lower()

    if again != "y":
        print("Thank you for using BMI Calculator!")
        break