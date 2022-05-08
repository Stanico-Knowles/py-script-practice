import datetime


date = datetime.datetime.now()
formatted_date = date.strftime('%A, %B %d, %Y, %I:%M %p')
print(f'The date and time is {formatted_date}')
print('I was written with straight Python!')