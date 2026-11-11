#aხსენით ტქვენი ენით if else
#if else არის როგორც გზა ჯვარედინი,პროგრამა ამოწმებს მოცემულ პირობას ანუ if ს და თუ პირობა სწორია ანუ true მაშინ სრულდება ჩაწერილი პირველი კოდი ხოლო თუ პირობა მცდარია ანუ false პროგრამა გადადის ავტომატურად else ბლოკზე და ასრულებს მოქმედებას რომელიც ჩაწერილია else ბლოკში



#შემოიყვანეთ ორი რიცხვი
num = int(input("enter first number: "))
if num % 2 == 0:
    print("number is even") 
else:
    print("number is odd")


#ფასდაკლება
price = int(input("enter price: "))
if price > 100:
    print("შენ მიოღე 10 პროცენტიანი კუპონი")
else:
    print("შენ ვერ მიიღე კუპონი")


#ტემპერატურა
temperature = int(input("enter temperature: "))
if temperature > 25:
    print("Its hot outside")
else:
    print("its cold outside")



#ორი რიცხვის შემოყვანა
num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
if num1 > num2:
    print("first number is bigger than second number")
else:
    print("second number is bigger than first number")
