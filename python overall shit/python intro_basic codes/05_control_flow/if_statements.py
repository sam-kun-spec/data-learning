''' if statements  = used to test a specific condition for decision making
    if() , elif() , else()
'''

age  = int(input("How old are you? "))
has_ticket = False
ticket_price = 50

if age >= 65:
    print("You are a senior citizen")
    print("the ticket for a senior citizen is", ticket_price * 0.72,"$")

elif age >= 18:
    print("You are a adult")
    print("the ticket for an adult is", ticket_price,"$")

elif age < 0:
    print("Invalid age")

elif age == 0:
    print("u juzt born")

else:
    print("You are a child")
    print("the ticket for a child is", ticket_price * 0.5,"$")



if not has_ticket:
    print("You can enter the concert")
else:
    print("You cannot enter the concert , pls buy a ticket")


# ijidkng
# jddfik  kjnsd
# jxn