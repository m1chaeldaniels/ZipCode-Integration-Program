import requests
#from pprint import pp

#API key needed
api_key="##"

country_code='US'

#setting up error handling by creating a status code variable equal to the correct code number for a valid zipcode

while True:
    
    
    zip_code= str(input("Please enter a zipcode: "))
    myURL= f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"
    results=requests.get(myURL)
    code=results.status_code
    if code==200:
          print ("\n")
          break
    else:
          print (f"The zipcode '{zip_code}' seems to be invalid")    
    


myJSON = results.json()
lat = (myJSON['lat'])
lon = (myJSON['lon'])
city = (myJSON['name'])




def get_zip(zip_code):
    if zip_code in myURL:
        print(city)
        print(lat)
        print(lon)
        
        return(city, lat, lon)
    
weatherURL=f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}&units=imperial"
results2=requests.get(weatherURL)
myJSON2=results2.json()

temperatures = myJSON2['main']
myTemp = temperatures['temp']
weather = myJSON2['weather'][0]
weatherDESC = weather['description']
templow = temperatures['temp_min']
temphigh = temperatures['temp_max']

#pp(myJSON2)

def get_weather(zip_code):
    
    if zip_code in weatherURL:
        print(weatherDESC)
        print(templow)
        print(temphigh)
    
    return (weatherDESC, templow, temphigh)



#MOve url to function

#creating statements to print out output

print(f"the city name for zipcode : '{zip_code}' is {city}")
print(f"the latitude for zipcode: '{zip_code}' is {lat}")
print(f"the longitude for zipcode: '{zip_code}' is {lon}")
print(f"The current weather is {weatherDESC}")
print(f"The current temperature is {myTemp}")
print(f"Today's low is {templow} with a high of {temphigh}")