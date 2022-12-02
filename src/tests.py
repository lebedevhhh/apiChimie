import requests
import json
# atome = AtomeModel(
#             id = num_protons,
#             name = args['name'],
#             val_e = args['val_e'],
#             e_negativity = args["e_negativity"],
#             Masse_Molaire = args['Masse_Molaire'],
#             config_e_quick = args["config_e_quick"],
#             config_e_full = args["config_e_full"],
#             charges = args["charges"]
# )

url = "http://127.0.0.1:5000/atome/11" #<int:numprotons>

dt = {
    'name' :"Sodium",
    'val_e': 1,
    'e_negativity': 0.93,
    'Masse_Molaire': 22.99,
    'config_e_quick': "[Ne] 3(s1)",
    'config_e_full': "",
    'charges': "(0)"
}


resp = requests.put(url, data = dt)
print(resp.status_code)

##
##need to change the carone full config and also quick config
##