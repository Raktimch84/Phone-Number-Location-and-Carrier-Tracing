import phonenumbers
from phonenumbers import geocoder,carrier,timezone
number=input("Enter the phone number with country specific digits(example +91) :  ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
geo=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(geo)

