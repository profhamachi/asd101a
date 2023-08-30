import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "San Diego, CA"
dest = "Los Angeles, CA"
key = "Sx4FuoR0r0dK5fFDkSS1V9nh4GIbcEJq"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)