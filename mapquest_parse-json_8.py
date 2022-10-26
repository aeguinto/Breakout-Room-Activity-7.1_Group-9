import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "0QgtuM8NpXYEfqFLVKEhquosu1CgrjgA"

while True:
   orig = input("Starting Location: ")
   if orig == "quit" or orig == "q":
        break

   dest = input("Destination: ")
   if orig == "quit" or orig == "q":
        break

   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Miles:           " + str(json_data["route"]["distance"]))
        print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("=============================================")
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================")
        print("Price Fare:" + str(((json_data["route"]["fuelUsed"])*0.264)+((json_data["route"]["distance"])*0.621)+72))