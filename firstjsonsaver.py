from datascraper import datascarpper
import json


result = datascarpper()

#save as json file
with open('country.json','w') as f:
    json.dump(result,f,indent=2)