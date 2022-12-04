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

url = "http://127.0.0.1:5000/atome/46" ##<int:numprotons>

dt = {
    'name' :"Palladium",
    'val_e': 9,
    'e_negativity': 2.20,
    'Masse_Molaire': 102.9,
    'config_e_quick': "[Ar] 4(s2) 3(d10) 4(s2) 4(p6) 5(s1) 4(d8)",
    'config_e_full': "1(s2) 2(s2) 2(p6) 3(s2) 3(p6) 4(s2) 3(d10) 4(s2) 4(p6) 5(s1) 4(d8)",
    'charges': "(+2, +3, +4)"
}


resp = requests.put(url, data = dt)
print(resp.status_code)

##
##need to change the carone full config and also quick config
##revoir vanadium config
#### rendu Palladium
#### revoir le bay du zinc