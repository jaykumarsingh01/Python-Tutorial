# import requests
# response = requests.get("https://www.pw.live")
# print(response.text)

# import requests
# response = requests.get("https://www.pw.live")
# print(response.status_code)  # Check if the request is successful (200)

import requests  # Ensure you have imported the module

response = requests.get("https://www.google.com")  # Use 'requests' (not 'request')
print(response.text)  # Print the response content

