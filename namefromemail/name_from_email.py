# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

import re
email = "elek.viz@exam.com"
#email = str(input("Give me an email address (e.g. elek.viz@exam.com) "))

def name_from_email(email):
    first_name = ""
    last_name = ""
    match = re.search('([\w.-]+)\.([\w.-]+)', email)
    if match:
        print(match.group(1))
        print(match.group(2))

    # for element in email != "\.":
    #     first_name += element
    #     for character in email != "@":
    #         last_name += character
    # return(last_name, first_name)

print(name_from_email("elek.viz@exam.com"))

