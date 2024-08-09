import requests
print(r"""/
                                                                
 _____                                                                               _____ 
( ___ )                                                                             ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  __  __ _                            __ _     ____                            |   | 
 |   | |  \/  (_)_ __   ___  ___ _ __ __ _ / _| |_  / ___|  ___ _ ____   _____ _ __  |   | 
 |   | | |\/| | | '_ \ / _ \/ __| '__/ _` | |_| __| \___ \ / _ \ '__\ \ / / _ \ '__| |   | 
 |   | | |  | | | | | |  __/ (__| | | (_| |  _| |_   ___) |  __/ |   \ V /  __/ |    |   | 
 |   | |_|__|_|_|_| |_|\___|\___|_|  \__,_|_|  \__| |____/ \___|_|    \_/ \___|_|    |   | 
 |   | |  ___(_)_ __   __| | ___ _ __                                                |   | 
 |   | | |_  | | '_ \ / _` |/ _ \ '__|                                               |   | 
 |   | |  _| | | | | | (_| |  __/ |                                                  |   | 
 |   | |_|   |_|_| |_|\__,_|\___|_|                                                  |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                             (_____)

      ---Please Read Readme beforehand---                                           
"""
                )
""" get input value of data offset, country code and api key"""
offset = input('\033[91m'+"Enter data offset: "+ '\033[0m')
country = input('\033[91m'+"Write Country Code (or just press enter if not interested): "+ '\033[0m')
if country != "":
    city = input('\033[91m'+"Write down city you want to search ( or just press enter if not interested): "+ '\033[0m')
else:
    city = ""
url = "https://api.criminalip.io/v1/banner/search?query=Minecraft+port%3A25565+country%3A{}+city%3A{}&offset={}".format(country,city,offset)

"""get api value using requests module"""
payload={}
headers = {"x-api-key" : input('\033[91m'+"Write your CIP API key: "+ '\033[0m')}
response = requests.request("GET", url, headers=headers, data=payload)
response.encoding = "utf-8"
output = response.json()
"""if response is successful return information"""
if response.status_code == 200:
    try:
        datas = output["data"]["result"]
        print('\033[94m'+"--------------------------------------------------"+ '\033[0m')
        print(f"Total numbers of Minecraft servers found: '\033[91m{output["data"]["count"]}\033[0m'")
        for data in datas :
            print('\033[94m'+"AS_Name: "+ '\033[0m'+data.get("as_name"))
            print(f"located City: '\033[91m{data.get("city")}\033[0m'")
            print(data.get("banner"))
            if data.get("score") == "Safe" or data.get("score") =="Low" and data.get("score_out") == "Safe" or data.get("score_out") == "Low":
                print('\033[93m'"This is a safe Minecraft Server"+ '\033[0m')
            else:
                print('\033[91m'+"This is either a suspicious or vulnerable server"+ '\033[0m')
            print('\033[94m'+"----------------------------------------------------"+ '\033[0m')
        
    except KeyError:
        print("Key Error: Invalid API key")
    except TypeError:
        print("Type Error: ")
else:
    print(f"Failed to get Data: {response.status_code}")
