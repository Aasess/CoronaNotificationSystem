#importing necessary libraries

import json
from plyer import notification
from datascraper import datascarpper
import time

#defing function for notification
def notifier(Countryname,message):
    notification.notify(
        title = Countryname,
        message = message,
        app_icon = "D:\\Nepalicoronanotificationsystem\\corona.ico",
        timeout = 3
    )

#continuously running
while(True):
    #load the saved json file
    with open('country.json') as f:
        data = json.load(f)

    #call the datascrapper() function to check the new updates
    result_newcase = datascarpper()
    dict_temp = {} #empty dict to storing new cases,new deaths,new recovered

    for key,value in result_newcase.items():
        dict_temp[key]={"new case": int(result_newcase[key]["Confirmed"]) - int(data[key]["Confirmed"]),
                        "new death": int(result_newcase[key]["Death"]) - int(data[key]["Death"]),
                        "new recovered": int(result_newcase[key]["Recovered"]) - int(data[key]["Recovered"]) }

    #logic for handling new case and updating old json file
    for item in dict_temp.items():
        if(item[1]['new case'] > 0 or item[1]['new death'] > 0 or item[1]['new recovered'] > 0):
            message = f"New Case:{item[1]['new case']} \nNew Death:{item[1]['new death']} \nNew Recovered:{item[1]['new recovered']}"
            with open('country.json','w') as f:
                json.dump(result_newcase,f,indent=2)

            #calling the notification function
            notifier(f"Covid -19 detail:\n{item[0]}",message)
            time.sleep(3.2)



