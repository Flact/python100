

# def format_name(f_name, l_name):
#     return f"{f_name} {l_name}".title()

def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        # return
        return "Type first name and last name"
    return f"{f_name} {l_name}".title()

# print(format_name("AnGeLa", "yU"))

print(format_name(input("What is your first name? "), input("What is your last name? "))) # Look this, take two arguments print seperatly