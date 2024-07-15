#BMI CALCULATOR

h = float(input("Enter height in m: "))
wt = float(input("Enter weight in kgs: "))

bmi = (wt/(h**2))
print("Body Mass Index value is:", f"{bmi:.2f}")

if bmi <= 18.5:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are overweight.")
elif bmi <= 34.9:
    print("You are obese.")
else:
    print("You are clinically highly obese.")
