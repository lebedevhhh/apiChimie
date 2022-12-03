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

url = "http://127.0.0.1:5000/atome/28" #<int:numprotons>

dt = {
    'name' :"Cobalt",
    'val_e': 9,
    'e_negativity': 1.88,
    'Masse_Molaire': 55.85,
    'config_e_quick': "[Ar] 4(s2) 3(d7)",
    'config_e_full': "1(s2) 2(s2) 2(p6) 3(s2) 3(p6) 4(s2) 3(d7)",
    'charges': "(+2, +3)"
}


resp = requests.put(url, data = dt)
print(resp.status_code)

##
##need to change the carone full config and also quick config
##revoir vanadium config
#### rendu Nickel