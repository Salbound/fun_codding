from datetime import date
from datetime import datetime

# date = somente dia é pego
today = date.today()
print("Today's date:", today)

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)



#datetime = pega dia e hora
# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)



#ref: https://www.programiz.com/python-programming/datetime/current-datetime#:~:text=today()%20method%20to%20get,representing%20date%20in%20different%20formats.