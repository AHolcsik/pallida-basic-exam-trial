# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

email = "elek.viz@exam.com"
#email = str(input("Give me an email address (e.g. elek.viz@exam.com) "))

def name_from_email(email):
    first_name = ""
    last_name = ""
    if element in email != ".":
        first_name += element
        if character in email != "@":
            last_name += character
    return(last_name, first_name)

print(name_from_email("elek.viz@exam.com"))

