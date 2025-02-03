age = int(input('Please enter your age: '))
category = input('Please enter "senior" or "student" if applicable. Leave blank otherwise: ')

if category == "student": print("25 €" if age < 30 else "50 €")
elif category == "senior": print("30 €")
else: print("25 €" if age < 18 else "50 €")
