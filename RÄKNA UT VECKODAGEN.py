#Steg 1: Användaren skall skriva in ett årtal mellan 1583 och 9999
year = int(input("Year:"))
while year < 1583 or year > 9999:
    print("Out of range, try inbetween the years 1583-9999")
    year = int(input("Year:"))

#Steg 2: Användaren skall skriva in en månad mellan 1-12
month = int(input("Month:"))
while month < 1 or month > 12:
    print("Out of range, try inbetween month 1-12")
    month = int(input("Month:"))

'''Formel för att göra så att om användaren skriver in månad 1 eller 2
så skall det istället bli månad 13 respektive 14 från föregående år'''
if month == 1 or month == 2:
    month += 12
    year -= 1


#Följande används för att bestämma om det är skottår eller inte
skottår = bool((year + 1) % 4 == 0 and (year + 1) % 100 != 0)
skottår2 = bool((year + 1) % 400 == 0)
skottår3 = bool(skottår or skottår2) 


day = int(input("Day:"))
while True:
    if month == 14 and (day < 1 or day > 29) and skottår3 == True:
        print("Out of allowed range 1-29")
        day = int(input("Day:"))
    elif month == 14 and (day < 1 or day > 28) and skottår3 == False:
        print("Out of allowed range 1 to 28")
        day = int(input("Day:"))
    elif month in [13, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        print("Out of allowed range 1 to 31")
        day = int(input("Day:"))
    elif month in [4, 6, 9, 11] and (day < 1 or day > 30):
        print("Out of allowed range 1 to 30")
        day = int(input("Day:"))

    else:
        #Zeller's Congruens - för att räkna ut vilken veckodag det är
        weekday = ( day + 13*(month+1)//5 + year + year//4
                    - year//100 + year//400 ) % 7

        #Här skall programmet skriva ut vilken dag det är
        if weekday == 0:
            print("It is a Saturday")
            break
        elif weekday == 1:
            print("It is a Sunday")
            break
        elif weekday == 2:
            print("It is a Monday")
            break
        elif weekday == 3:
            print("It is a Tuesday")
            break
        elif weekday == 4:
            print("It is a Wednesday")
            break
        elif weekday == 5:
            print("It is a Thursday")
            break
        elif weekday == 6:
            print("It is a Friday")
            break
