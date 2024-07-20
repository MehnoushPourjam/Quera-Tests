n_weight = int(input())
m_high = float(input())

BMI = n_weight/(m_high**2)
print(f"{BMI:.2f}")

if BMI < 18.5:
    print("Underweight")
elif BMI<25:
    print("Normal")
elif BMI<30:
    print("Overweight")
else:
    print("Obese")