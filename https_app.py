import json
import v20
import colorama
import requests
# from pip._vendor import requests

# print the message
# print("Why won't this line of code print")

# # print the message
# print('This line fails too!')

# # print the message
# print ("I think I know how to fix this one")

# # print the name entered by the user
colorama.init()
print(colorama.Fore.LIGHTCYAN_EX) 
#name =input('Please tell me your name: ')
#fprint(colorama.Fore.LIGHTMAGENTA_EX) 

#print(colorama.Fore.LIGHTGREEN_EX+name)




API_KEY=''

  # Request headers
headers = { 
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': API_KEY
}

 # Request parameters
parameters_str ={
    'visualFeatures': 'Faces,Description',
    'language': 'en'
}
#Categories ,Tags, Description ,Faces , ImageType 

print(colorama.Fore.LIGHTMAGENTA_EX+'Getting Data ...') 
#image
image_path ="C:/test/1.jpg"
image_data=''
try:
    image_data = open(image_path, "rb").read()

except Exception as e:
    print(e.__str__())


service_address ='https://pcomputervision.cognitiveservices.azure.com/'

address = service_address+'/vision/v1.0/analyze'

print(colorama.Fore.GREEN+'Sending Data ...') 
print(colorama.Fore.YELLOW+'>>>') 

response = requests.post(address,headers=headers,params=parameters_str,data=image_data )


# Display the JSON results returned
results = response.json()

print(json.dumps(results))
