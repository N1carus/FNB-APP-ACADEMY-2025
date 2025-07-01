#loops

#for loop

#fruits = ["apple", "banana", "cherry"]

#for fruit in fruits:
#    print(fruit)
    
    
#numbers = [1, 2, 3, 5, 7]

#for number in numbers:
#    print(number)
    
    
#while loop

#using a while loop to count from 1 - 5
#count = 1

#while count <= 5:
#    print(count)
#    count += 1

#More on loops

#fruits = ["apple", "banana", "cherry", "date"]

#for fruit in fruits:
#    if fruit == "cherry":
#        break #exits loop once cherry is found
#    print(fruit)
    
#print()

#for fruit in fruits:
#    if fruit == "cherry":
#        continue #Skips cherry and moves to date or next iteration
#    print(fruit)
    
#print()

#for fruit in fruits:
#    if fruit == "cherry":
#        pass #placeholder, no action is needed for cherry
#    print(fruit)

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break 