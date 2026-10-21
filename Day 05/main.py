name = input("შეიყვანე სახელი")
surname = input("შეიყვანე გვარი")
age = input("შეიყვანე ასაკი")
print(f"hello, my name is {name} {surname} and my age is {age}")


price1 = float(input("პირველი პროდუქტის ფასი: "))
price2 = float(input("მეორე პროდუქტის ფასი: "))
price3 = float(input("მესამე პროდუქტის ფასი: "))
total = price1 + price2 + price3
print(total)



age = int(input("შეიყვანე ასაკი"))
years = int(input("შეიყვანე წლების რაოდენობა"))
future_age = age + years
print(f"In {years} years you will be {future_age} years old")


distance = float(input("გავლილი მანძილი (კმ)"))
time = float(input("დახარჯული დრო (საათი)"))
speed = distance / time
print(f"საშუალო სიჩქარე: {speed} კმ/სთ")


distance = float(input("გასავლელი მანძილი"))
fuel = (distance * 8 ) / 100
print(f"დასჭირდება {fuel} საწვავი")


distance = float(input("გასავლელი მანძილი"))
consumption = float(input("საწვავის ხარჯი ყოველ 100 კმ-ზე (ლიტრი) "))
fuel_price = float(input("ერთი ლიტრი საწვავის ფასი"))
fuel_amount = (distance * consumption) / 100
cost = fuel_amount * fuel_price
print(f"დახარჯული საწვავი: {fuel_amount} ლიტრი")
print(f"დახარჯული თანხა: {cost}₾")
