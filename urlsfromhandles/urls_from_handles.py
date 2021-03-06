# Create a function that takes a list of GitHub handles as input and returns a
# list of strings that represents
# GitHub url's under Green Fox Academy organization in the following format:
# "https://github.com/greenfox-academy/teststudent"

# example:
# input: ["ghhandle1", "ghhandle2"]
# output: ["https://github.com/greenfox-academy/ghhandle1", "https://github.com/greenfox-academy/ghhandle2"]

names = ["ghhandle1", "ghhandle2"]

def urls_from_handles(names):
    list_of_urls = []
    url = "https://github.com/greenfox-academy/"
    for handle in names:
        list_of_urls += [url + handle]
    return(list_of_urls)

print(urls_from_handles(names))
