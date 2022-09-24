
#empty list to store names and phone numbers.
names = []
phone_numbers = []

num = int(input("Enter no of contact you want to save: "))
for i in range(num):
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    #adding the input from user to the already created empty list
    names.append(name)
    phone_numbers.append(phone_number)
print("\nName\t\t\tPhone Number")
for i in range(num):
    print("{}\t\t\t{}".format(names[i],phone_numbers[i]))

#Searching for a contact in the list
search_term = input("\nEnter search term: ")
print("search Result: ")
if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    
    print("Name: {}, Phone Number: {}". format(search_term, phone_number))
else:
    print("Note Found")
