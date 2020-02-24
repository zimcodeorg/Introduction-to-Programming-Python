###Solution 1: Good enough but not perfect

def validate(email):
    '''
    Validates an email addreess by checking that it contains only 1 @ sign
    and that there is at least one period '.' after the @ sign
    email -> str
    returns bool
    '''
    #First check that there is only one '@' symbol
    if email.count('@') > 0 and email.count('@'):
        #Find the position of the '@' symbol
        symbol_index = email.index('@')
        #Make sure there is a username before the @ symbol
        if symbol_index > 0:
            if '.' in email[symbol_index:] and email[symbol_index+1] != '.' and email[-1] != '.' :
                #Use slicing to check if there is a '.' after the @ symbol
                #Then check that it is not directly after the '@' symbol
                #Then check that the '.' is not at the end of the email
                return True
    #If any of the tests are False, return False
    return False