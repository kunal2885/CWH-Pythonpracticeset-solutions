# letter = '''  Dear <|Name|>, You are selected! <|Date|> ''' 

name = input('hey user enter your name')
date = input('enter the date of selection')
formatted_letter = f"Dear {name}, You are selected {date}"
formatted_letter2 =  "Dear {}, You are selected! {}".format(name,date)
print(formatted_letter)
print(formatted_letter2)