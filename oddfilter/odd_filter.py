# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

list_o_numbers = [1, 2, 3, 4, 5]
def odd_filter(list_o_numbers):
    odds = []
    for element in list_o_numbers:
        if element % 2 != 0:
            odds += element
    return(odds)


print(odd_filter(list_o_numbers))
