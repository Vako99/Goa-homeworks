#1-რა არის ინფუთი
# input() არის ფუნქცია რომელიც მომხმარებელს აძლევს საშუალებას კლავიატურიდან შეიყვანოს ინფორმაცია პროგრამაში. input ყოველთვის აბრუნებს ტექსტს


#2-რა არის თაიფქასთინგი
#type casting ნიშნავს ერთი ტიპის მონაცემის მეორე ტიპად გადაქცევას.int("5") ტექსტ 5 ს გადააქცევს მთელ რიცხვად 5-ად

#3-მონაცემთა ტიპები
#int მთელი რიცხვი            მაგ 5, -12, 2024
# float ათწილადი რიცხვი         მაგ 3.14, -0.5, 10.0
# str ტექსტი (სტრიქონი)       მაგ "გამარჯობა", 'Python', "123"
# bool ლოგიკური მნიშვნელობა    მაგ True, False


#4-შედარებები
#> მეტია
#< ნაკლებია
#== ტოლია
#>= მეტია ან ტოლია
#<= ნაკლებია ან ტოლია
#!=  არ არის ტოლი 




#5-მათემატიკური მაგალითები
Num1 = int(input("Enter first number"))
Num2 = int(input("enter second number"))
print(Num1, "==", Num2, "->", Num1 == Num2)
print(Num1, "!=", Num2, "->", Num1 != Num2)
print(Num1, ">", Num2, "->", Num1 > Num2)
print(Num1, "<", Num2, "->", Num1 < Num2)
print(Num1, ">=", Num2, "->", Num1 >= Num2)
print(Num1, "<=", Num2, "->", Num1 <= Num2)


#-6ასაკი
age= int(input("enter ur age"))
print("ასაკი 18 ან მეტია:", age >= 18)

#7-გამოთვლა მანქანა
speed = float(input("speed "))
distance = float(input("distance "))
time = float(input("time "))

needed_time = distance / speed
print(needed_time <= time)



#8-ეყოფა თუ არა
p1 = float(input("ფასი 1: "))
p2 = float(input("ფასი 2: "))
p3 = float(input("ფასი 3: "))
money = float(input("თანხა: "))

print(money >= p1 + p2 + p3)



#9-მეხსიერება
Storage = float(input("Gb; "))
Space = float(input("Free space; "))
print("მეხსიერება საკმარისია;", Storage <= Space)




