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

url = "http://127.0.0.1:5000/atome/71" ##<int:numprotons>

dt = {
    'name' : "Lutétium",
    'val_e': 3,
    'e_negativity': 1.27,
    'Masse_Molaire': 175.0,
    'config_e_quick': "[Xe] 6(s2) 4(f14) 5(d1)",
    'config_e_full': "1(s2) 2(s2) 2(p6) 3(s2) 3(p6) 4(s2) 3(d10) 4(s2) 4(p6) 5(s2) 4(d10) 5(p6) 6(s2) 4(f14) 5(d1)",
    'charges': "(+3)"
}


resp = requests.put(url, data = dt)
print(resp.status_code)
print(resp.content)

##
##delete 57,58,59 update
##need to change the carone full config and also quick config
##revoir vanadium config
#### revoir le bay du zinc
##revoir le Palladium