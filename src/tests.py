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

url = "http://127.0.0.1:5000/atome/55" ##<int:numprotons>

dt = {
    'name' :"Cesium",
    'val_e': 1,
    'e_negativity': 0.79,
    'Masse_Molaire': 132.9,
    'config_e_quick': "[Xe] 6(s1)",
    'config_e_full': "1(s2) 2(s2) 2(p6) 3(s2) 3(p6) 4(s2) 3(d10) 4(s2) 4(p6) 5(s2) 4(d10) 5(p6) 6(s1)",
    'charges': "(+1)"
}


resp = requests.put(url, data = dt)
print(resp.status_code)

##
##need to change the carone full config and also quick config
##revoir vanadium config
#### rendu Palladium
#### revoir le bay du zinc
##revoir le Palladium