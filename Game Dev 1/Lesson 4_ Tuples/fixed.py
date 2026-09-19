# name1= input("What is the name of your group?: ")
# size1= int(input("How many people are in your group? :"))
# date1= input("What was the date of your competition?: ")
# type1= input("What type of medal did you get?:")
# venue1= input("Where was your competetion hosted?: ")
# group1= (name1, size1, date1, venue1, type1)

# name2= input("What is the name of your group?: ")
# size2= int(input("How many people are in your group? :"))
# date2= input("What was the date of your competition?: ")
# type2= input("What type of medal did you get?:")
# venue2= input("Where was your competetion hosted?: ")
# group2= (name2, size2, date2, venue2, type2)

# name3= input("What is the name of your group?: ")
# size3= int(input("How many people are in your group? :"))
# date3= input("What was the date of your competition?: ")
# type3= input("What type of medal did you get?:")
# venue3= input("Where was your competetion hosted?: ")
# group3= (name3, size3, date3, venue3, type3)

# name4= input("What is the name of your group?: ")
# size4= int(input("How many people are in your group? :"))
# date4= input("What was the date of your competition?: ")
# type4= input("What type of medal did you get?:")
# venue4= input("Where was your competetion hosted?: ")
# group4= (name4, size4, date4, venue4 ,type4)

# name5= input("What is the name of your group?: ")
# size5= int(input("How many people are in your group? :"))
# date5= input("What was the date of your competition?: ")
# type5= input("What type of medal did you get?:")
# venue5= input("Where was your competetion hosted?: ")
# group5= (name5, size5, date5, venue5 ,type5)

# print(group1)
# print(group2)
# print(group3)
# print(group4)
# print(group5)
baba= []
for i in range (5):
    name= input("What is the name of your group?: ")
    size= int(input("How many people are in your group? :"))
    date= input("What was the date of your competition?: ")
    kind= input("What type of medal did you get?:")
    venue= input("Where was your competetion hosted?: ")
    group= (name, size, date, kind, venue)
    baba.append (group)

for i in range(len(baba)):
    print(baba[i])
    i+=1
print(baba)
