def convert2(meter):
    formula = int(meter) * 3.28084
    round(formula, 2)
    return formula

num2 = int(input("Please enter a length in m to change to ft: "))
print(convert2(num2))