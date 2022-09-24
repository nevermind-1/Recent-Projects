usernames = {
    'anthony':'32355',
    'james':'88766',
    'Hampo':'90909'
}

user = input('Please enter username: ')

#let's check for it in our database

if user in usernames:
    #get the password  of the user in question
    pword = usernames.get(user)

    #Let's get password 
    password = input('please enter your password: ')
    if password == pword:
        print("Thank you!")
    else:
        print("You enterd an incorrect password. Please try again!")
