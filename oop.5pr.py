from dataclasses import dataclass

N = 5  



@dataclass
class Car:
    surname: str  
    brand: str    
    color: str    



cars = []
print("Введіть дані про власників (прізвище, марка, колір):")
for i in range(N):
    print(f"Власник {i + 1}")
    surname = input("  Прізвище = ").strip()
    brand = input("  Марка    = ").strip()
    color = input("  Колір    = ").strip()
    cars.append(Car(surname, brand, color))


with open("CAR.txt", "w", encoding="utf-8") as f:
    for c in cars:
        f.write(f"{c.surname};{c.brand};{c.color}\n")


read_cars = []
with open("CAR.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            surname, brand, color = line.split(";")
            read_cars.append(Car(surname, brand, color))


print("\nВласники автомобілів Audi сірого кольору:")
found = 0
for c in read_cars:
    if c.brand.lower() == "audi" and c.color.lower() in ("сірий", "grey", "gray"):
        print(c.surname, c.brand, c.color)
        found += 1

if found == 0:
    print("Таких власників не знайдено.")
