def convert(cm):
    formula = int(cm) / 100
    return formula

num1 = int(input("Please enter a length in cm to change to m: "))

print(convert(num1))

def convert2(meter):
    formula = int(meter) * 3.28084
    return formula

num2 = int(input("Please enter a length in m to change to ft: "))
print(convert2(num2))