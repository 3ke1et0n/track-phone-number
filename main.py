#pip install folium
#pip install phonenumbers
#pip install opencage

import folium
from numpy import number
import phonenumbers
import opencage


print('''
  _____  _                        _   _                 _               
 |  __ \| |                      | \ | |               | |              
 | |__) | |__   ___  _ __   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 |  ___/| '_ \ / _ \| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |    | | | | (_) | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 |_|    |_| |_|\___/|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                        
                                                                        

                                      instagram:@ram4nzz                          
                                                                                                           
      ''')

from phonenumbers import geocoder
number = input("enter your number: ")



pepnumber = phonenumbers.parse(number)



Location = geocoder.description_for_number(pepnumber, "en")
print(Location)


from phonenumbers import carrier

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = '#get key in the opencage geolocation'

geocoder = OpenCageGeocode(key)
query = str(Location)
results = geocoder.geocode(query)
#print(result)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(Location=[lat,lng])
folium.Marker([lat,lng], popup=Location).add_to(myMap)

myMap.save("myLocation.html")

