#activity 1
#count of the occurences of vowels in the string entered by the user
# string1= input("Enter a string ")
# vowels= {'a':0, 
#          'e':0,
#          'i':0,
#          'o':0,
#          'u':0}

# for i in string1:
#     if i in vowels:
#         vowels[i] +=1
# print (vowels)

#activity 2
#count the occurences of each letter in the string entered by the user
# string2= input("Enter a string ")
# letters= {}


# for i in string2.lower():
#     if i.isalpha():
#         if i in letters:
#             letters[i] +=1
#         else:
#             letters [i]= 1
# print (letters)

#activity 3
#find if the number entered by the user in a pangram
int1= input("enter a number ")
numbers= {'0':0,
          '1':0,
          '2':0,
          '3':0,
          '4':0,
          '5':0,
          '6':0,
          '7':0,
          '8':0,
          '9':0}

for i in int1:
    if i in numbers:
        numbers[i] +=1

pangram= True

for i in numbers.values():
    if i == 0:
        pangram= False

if pangram:
    print("It's a pangram")
else:
    print("Number is not a pangram")