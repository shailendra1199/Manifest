time = 24
name_units ="hours"

def days_to_units(num_of_days):
    return f"{num_of_days} is converted into {num_of_days * time} {name_units}"

def validate_and_execute():
    try:
        user_input_no_int = int(num_of_days_element)

        if user_input_no_int > 0:
            Calculated_value =days_to_units(user_input_no_int)
            print(Calculated_value)
        elif user_input_no_int == 0 :
            print("0 is Enter ,Enter value greater than 0")
        elif user_input_no_int < 0:
            print("You Enter a negitive no .ENTER VALID NO ")


    except ValueError :
        print("Your input is not valid number.")

        

User_input=""
while User_input != "exit":
    User_input =input("Enter Number(CONVERTED INTO DAYS TO UNITS(HOURS)")
    list_of_days = User_input.split(",")
    for num_of_days_element in set(list_of_days):
        list(list_of_days)
        validate_and_execute()

    


