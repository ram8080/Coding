def is_unique(string) {
    ''' First of all this solution can be breaken down in to three steps:
    storing ascii values of characters by subtracting from a ascii value in order to store all characters values
    '''
    checker=0
    for i in range(len(string)):
        bit=ord(string[i])-ord('a') 

        if bit>0:
            if (checker & 1<<bit)>0:
                return False
            checker=checker|(1<<bit)
        return True



}

string="CodingIsLove"
print(is_unique(string))