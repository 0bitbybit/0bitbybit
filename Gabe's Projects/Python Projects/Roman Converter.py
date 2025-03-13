#This program returns/displays the Roman Numeral value when you enter an arabic numeral value.
#Currently it's setup for in-program input instead of CLI user input.   

# define dictionaries for each value
thou = {"1": "M", "2": "MM","3": "MMM"}
hundo = {"1":"C", "2":"CC", "3":"CCC", "4":"CL", "5":"D", "6":"DC", "7":"DCC", "8":"DCCC", "9":"CM"}
tens = {"1":"X", "2":"XX", "3":"XXX", "4":"XL", "5":"L", "6":"LX", "7":"LXX", "8":"LXXX", "9":"XC"}
ones = {"1":"I", "2":"II", "3":"III","4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}

#functions for each vaule, starting with the ones place

def hundo_f(an, rn_list):
    
    for x in hundo: 
      if x in an[0]:   
        rn_list.append(hundo[x])
    for x in tens:
      if x in an[1]:   
        rn_list.append(tens[x])
    for x in ones:
      if x in an[2]:   
        rn_list.append(ones[x])
        
def thou_f(an, rn_list): # define functions for each place value
    for x in thou: 
        if x in an[0]:   
            rn_list.append(thou[x])
    for x in hundo:
        if x in an[1]:   
          rn_list.append(hundo[x])
    for x in tens:
        if x in an[2]:   
          rn_list.append(tens[x])
    for x in ones:
        if x in an[3]:   
          rn_list.append(ones[x])

            
def tens_f(an, rn_list):
    for x in tens:
        if x in an[0]:   
            rn_list.append(tens[x])
    for x in ones:
        if x in an[1]:   
            rn_list.append(ones[x])
            
def ones_f(an, L):
    for x in ones: 
        if x in an[0]:   
            L.append(ones[x])

def my_roman_numerals_converter(an):

    rn_list = []

    an = str(an) 

# criteria to run each function is based on AN order of magnitude i.e. thousands, tens

    if len(an) == 4:  
        thou_f(an, rn_list)

    if len(an) == 3:
        hundo_f(an, rn_list)
        
    if len(an) == 2:
        tens_f(an, rn_list)
        
    if len(an) == 1:
        ones_f(an, rn_list)
        
        
    rn_list = "".join(rn_list)

    return(rn_list)

print(my_roman_numerals_converter(14))
print(my_roman_numerals_converter(79))
