def urlify(string):
    result = ''
    for i in string:
        result = result + i.replace(" ", "%20")
    return result


print(urlify("Mr John Smith"))
