# SELECT QUERY Project
# We will take an input string
# Remove whitespace
# Convert it to a list
# Make functions to separate the list into headers (columns) and data values (rows)
# Make the header and data lists iterable

input_csv = """name,year_start,year_end,position,height,weight,birth_date,college\nAlaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24, 1968',Duke University\nZaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7, 1946',Iowa State University\nKareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16, 1947','University of California, Los Angeles'
Mahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9, 1969',Louisiana State University\n"""

stripped_input = input_csv.strip() #removed white spaces from input string
print(stripped_input)
print(len(stripped_input))

all_rows = stripped_input.split("\n") # convert entire string into a list
print(all_rows) # test
print(len(all_rows)) # test

def headers(): # make a list containing only headers aka columns
    
    headers = all_rows[0].split(",") # split rows at each comma within the first element to make list of headers
    print(headers)
    print(len(headers))
    return headers
headers()

def values(): # return list of values aka data rows
    i = 1
    values_list = []
    while i < len(all_rows):
        values_list += all_rows[i].split("\n")
        i += 1
    print(values_list)
    print(len(values_list))
values()

name,year_start,year_end,position,height,weight,birth_date,college
Alaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24, 1968',Duke University
Zaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7, 1946',Iowa State University
Kareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16, 1947','University of California, Los Angeles'
Mahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9, 1969',Louisiana State University
391
['name,year_start,year_end,position,height,weight,birth_date,college', "Alaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24, 1968',Duke University", "Zaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7, 1946',Iowa State University", "Kareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16, 1947','University of California, Los Angeles'", "Mahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9, 1969',Louisiana State University"]
5
['name', 'year_start', 'year_end', 'position', 'height', 'weight', 'birth_date', 'college']
8
["Alaa Abdelnaby,1991,1995,F-C,6-10,240,'June 24, 1968',Duke University", "Zaid Abdul-Aziz,1969,1978,C-F,6-9,235,'April 7, 1946',Iowa State University", "Kareem Abdul-Jabbar,1970,1989,C,7-2,225,'April 16, 1947','University of California, Los Angeles'", "Mahmoud Abdul-Rauf,1991,2001,G,6-1,162,'March 9, 1969',Louisiana State University"]
4
