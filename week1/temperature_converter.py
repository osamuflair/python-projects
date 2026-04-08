#Temperature Converter

def cel_to_fah(num): #celsius to fahrenheit
    result = round(((num * 9 / 5) + 32), 2)
    print(f"{num}°C = {result}°F\n")

def fah_to_cel(num): #fahrenheit to celsius
    result = round(((num - 32) * 5 / 9), 2)
    print(f"{num}°F = {result}°C\n")

def cel_to_kel(num): #celsius to kelvin
    result = round((num + 273.15), 2)
    print(f"{num}°C = {result}K\n")

def kel_to_cel(num): #kelvin to celsius
    if num < 0:
        print("kelvin can't be negative\n")
    else:
        result = round((num - 273.15), 2)
        print(f"{num}K = {result}°C\n")

def fah_to_kel(num): #fahrenheit to kelvin
    result = round((((num - 32) * 5 / 9) + 273.15), 2)
    print(f"{num}°F = {result}K\n")

def kel_to_fah(num): #kelvin to fahrenheit
    if num < 0:
        print("kelvin can't be negative\n")
    else:
        result = round((((num - 273.15) * 9 / 5) + 32), 2)
        print(f"{num}K = {result}°F\n")

conversions = {
    1: cel_to_fah,
    2: fah_to_cel,
    3: cel_to_kel,
    4: kel_to_cel,
    5: fah_to_kel,
    6: kel_to_fah
}

def main():
    while True:
        print("Temperature Converter")
        print("press 1 to convert from celsius to fahrenheit")
        print("press 2 to convert from fahrenheit to celsius")
        print("press 3 to convert from celsius to kelvin")
        print("press 4 to convert from kelvin to celsius")
        print("press 5 to convert from fahrenheit to kelvin")
        print("press 6 to convert from kelvin to fahrenheit")
        print("Press 0 to end program")
        
        try:
            choice = int(input(" "))
        except ValueError:
            print("Enter a number!!\n")
            continue

        if choice == 0:
            break
        elif choice > 6 or choice < 0:
            print("The Number Must be From 1 to 6!!\n")
            continue

        try:
            num = float(input("Enter number to convert: "))
        except ValueError:
            print("Enter a  valid number!!\n")
            continue

        conversions[choice](num)

main()