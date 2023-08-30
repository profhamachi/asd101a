import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Sx4FuoR0r0dK5fFDkSS1V9nh4GIbcEJq"

while True:
    orig = input("Starting Location (q to quit): ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination (q to quit): ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("===================================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:    " + (json_data["route"]["formattedTime"]))
        print("Kilometers:       " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("===================================================")