choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().upper()

if choice == "C":
    c = float(input("Enter the celsius value: "))
    f = (9/5 * c) + 32
    print(f"{c}\u00B0C = {f}\u00B0F")
elif choice == "F":
    f = float(input("Enter the fahrenheit value: "))
    c = (f - 32) * 5/9
    print(f"{f}\u00B0F = {c}\u00B0C") 

else:
    ("Invalid choice")
