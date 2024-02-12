# PASSWORD VALIDATOR TEMPLATE: aqutub_passwordvalidate.py

def validate(password):
    """ Analyzes an input password to determine if it is "Secure", "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid". 
    """

    badSymb = list(" @#")
    goodSymb = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
    if len(password) < 8:
        return "Invalid"
    if any(char in badSymb for char in password):
        return "Invalid"
    if not any(char.isupper() for char in password):
        return "Insecure"
    if not any(char.islower() for char in password):
        return "Insecure"
    if not any(char.isdigit() for char in password):
        return "Insecure"
    if not any(char in goodSymb for char in password):
        return "Insecure"
    else:
        return "Secure"
    
    

def generate(n):
    """ Generates a password of length n which is guaranteed to be Secure according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n. 
    """
    
    if n < 8:
        return "Invalid length"
    import random
    import string
    upAlphabets = (list(string.ascii_uppercase))
    loAlphabets = (list(string.ascii_lowercase))
    numbs = list(string.digits)
    specChar = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
    all = upAlphabets + loAlphabets + numbs + specChar
    password = []
    password += random.choice(upAlphabets)
    password += random.choice(loAlphabets)
    password += random.choice(numbs)
    password += random.choice(specChar)
    for i in range(n-4):
        password += random.choice(all)
    return (''.join(password))
    


    


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.
    pass

