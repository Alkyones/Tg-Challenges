import re

#utils
def checkIfDictAndSetDefaults(data):
    if type(data) == dict:
        data.setdefault('username', '')
        data.setdefault('password', '')
        data.setdefault('email', '') 
    else:
        return False

def checkEmail(email):
    #difficult expression used for production purposes
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+') #for more information check regular expressions
    
    if regex.fullmatch(email):
        return True, email
    
    return False, email

def checkPassword(password, username):
    if len(password) > 21 or username in password:
        return False, password, "Password is too long / contains username"
    
    #with regex to check if it has any uppercase, number and special character
    # regex = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).*$')

    # if regex.match(password):
    #     return True, password
    # return False, password, "Password doesn't contain special character/ number/ Uppercase letter"
    
    upperCase = any(ele.isupper() for ele in password)
    number= any(ele.isdigit() for ele in password)
    specialCharacter = any(not ele.isalnum() for ele in password)
    
    #check if all requirements are satisfied
    isValid = all([upperCase, number, specialCharacter])
    
    if isValid:
        return True, password
    return False, password, "Password doesn't contain special character/ number/ Uppercase letter"
    

def checkUsername(username):
    if len(username) > 15:
        return False, username, "Username is too long"
    
    # Check if the string starts with a letter and doesn't have any special characters except for underscores
    # regex = re.compile(r'^[A-Za-z][A-Za-z0-9_]*$')
    # if regex.match(username):
    #     return True, username
    
    if not username[0].isalpha():
        return False, username, "Username can not start with a number or special characters"
    
    for letter in username:
        if not letter.isalnum() and letter != '_':
            return False, username, "Username can not contain any special characters other than underscores"
        
    return True, username
            

def checkCredentials(credentials):
    isDataValid = checkIfDictAndSetDefaults(credentials)
    if isDataValid == False:
        return False
        
    username = credentials['username']
    password = credentials['password']
    email = credentials['email']
   
    
    if not any([username, password, email]):
        return False
    
    validUsername = checkUsername(username)[0]
    validPassword = checkPassword(password, username)[0]
    validEmail = checkEmail(email)[0]

    if not all([validUsername, validPassword, validEmail]):
        return False

    return True

if __name__ == '__main__':
    creds = {
        "username": "HelloUser_1",
        "password": "P@ssw0rd",
        "email": "test@gmail.com"
    }
    result = checkCredentials(creds)
    print(result)
    
