import phonenumbers
from phonenumbers import geocoder
import folium 
from test import number


Key = "bc382094f2504f6d994932f2b23bef1a"

number = input("Enter a phone number with country code : ")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)


from phonenumbers import carrier 
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode (Key)

query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

map_locaton = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat, lng ], popup =number_location).add_to(map_locaton)
map_locaton.save("mylocation.html")