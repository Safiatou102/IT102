"""
This is a simple script that connects to the AbuseIPDB API to check if an IP address is potentially malicious. It requires an API key to run, which you can obtain from https://www.abuseipdb.com/. The script sends a request to the API with the specified IP address and prints out the results, including the abuse confidence score. If the score is above a certain threshold, it will warn the user about a potentially malicious IP address.
"""

from ast import main
from urllib import response
from webbrowser import get


API_KEY = "a1b2c3d4e5f6g7h8i9j0..."
ip_address = "8.8.8.8"

url = "https://api.abuseipdb.com/api/v2/check"


headers = {
    "Key ":API_KEY, 
    "Accept":"application/json"}

params = {
    "ipAddress": ip_address, "maxAgeInDays": 90}

response = get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()["data"]

    print("IP Address:", data["ipAddress"])
    print("Country:", data["countryCode"])
    print("Abuse Confidence score:", data["abuseConfidentceScore"])

    if data["abuseConfidenceScore"] > 50:
        print("WARNING: Potentially malicious IP address detected!")
    else:
        print("IP appears safe.")
else:
    print("Error:", response.status_code)

    if __name__ == "__main__":
        main()