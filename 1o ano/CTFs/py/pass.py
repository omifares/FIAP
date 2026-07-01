import re

def isSpecial(char):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(char) == None:
        return False
    return True

with open("passwd_1", "r") as passwords:
    for password in passwords.readlines():
        third_char = open("pass_flag", "a+")
        
        char = password[2]
        if isSpecial(char) or char.isupper() or char.isnumeric():
            third_char.write(char)
        
    third_char.close()