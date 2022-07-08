#name = input('waht is your name? ')
#color = input('your favourite color? ')
#print('Hi ' + name)
#print(name + "'s favourite color is " + color)

#name = 'john'
#end ='smith' 
#msg = f' {name} [{end}] is a coder' 
#print(msg)

#name = 'python for beginners'
#x = name.split()
#print(x)


#house_price = 1000000
#good_credit = False
#if good_credit:
#    price = (int(house_price - (house_price * 10/100)))
#    print('your full payment price is : $' + (str(price)))
#    print('your down payment price is : $' + (str(0.1* house_price)))
#else:
#    price = (int( house_price - (house_price * 20/100)))
#    print('your full payment price is : $' + (str(price)))
#    print('your down payment price is : $' + (str(0.2* house_price)))

#while True:
#    weight = int(input('Weight : '))
#    unit = input("pounds (p) or kilogram (k) ? ")
#    if unit.upper() == 'P' :
#        in_pounds = weight*0.45
#        print(f' your weight in kilos {in_pounds}')
#    elif unit.upper() == 'K':
#        in_kilo = weight/0.45
#        print(f' your weight in pounds {in_kilo}')
#

#secret_nm = 9
#i = 0
#while i < 3:
#    guess_num = int(input("Guess: "))
#    i +=1
#    if guess_num == secret_nm:
#         print("you win")
#         break
#else:
##    print("you fail")
#
#command = ""
#started = False
#while True:
#    command = input("> ").lower()
#    if command== "start":
#        if started:
#            print("car is already started")
#        else:
#            started = True
#            print("car started...")
#    elif command == "stop":
#        if not started:
#            print("car is already stopped!")
#        else :
#            started = False    
#            print("stop the engine...")            
#    elif command == "help":
#        print("......")
#    elif command == "quit":
#        break
#    else :
#        print("i don't understand")
#        
#

#total = 0
#prices = [10, 20, 30]
#for price in prices:
#        total += (price)
#        #print(total)
#print(f'total price is : {total}')



#nested loops
#for x in range(4):
#        for y in range(3):
#                print(f'( {x} , {y})')


#numbers = [5, 2, 5, 2, 2, 2]
#for xcount in numbers:
#        show =''
#        for count in range(xcount):
#                show += 'x'
#        print(show)


#x=[1,2,3,4,5,6,7,8,9]
#print(max(x))

#numbers = [5,7,3,1,9,8]
#max = numbers[0]
#for number in numbers:
#        if number > max:
#                max = number
#print(max)                        

#numbers = [
#        [1,2,3],
#        [4,5,6],
#        [7,8,9]
#]
#numbers [0] [2] = 10
#print(numbers[0] [2])
#for row in numbers:
#        for item in row:
#                print(item)


#class Point:
#
#        def __init__(self, x ,y ) -> None:
#                self.x = x
#                self.y = y
#        def move(self):
#                print('move')
#
#        def draw(self):
#                print('draw')
#

#point1= Point()
#point1.draw()
#point1.move()
#point1.x=10
#point1.y=20
#print(point1.x)
#print(point1.y)


#point = Point(10, 20)
#point.x = 111
#print(point.x)






#from unicodedata import name
#
#
#class Person:
#        def __init__(self, name) -> None:
#                self.name = name
#        def talk(self):
#                print(f"Hy i am {self.name}!") 
#                print("How are you")
#
#
#person = Person("john smith") 
##print(person.name)
#person.talk()
#
#person = Person("bob smith")
#person.talk()

#total = 0
#prices = [10, 20, 30, 49]
#for price in prices:
#        total += (price)
#        #print(total)
#print(f'total price is : {total}')


#name = input('what is your name? ')
#color = input('your favourite color? ')
#print('Hi ' + name)
#print(name + "'s favourite color is " + color)

#name = 'python for beginners'
#x = name.split()
#print(x)

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)        
