import requests
import json

##ressources ---> file:///C:/Users/ilyas/OneDrive/Desktop/allSkullzRelated/science/Tableau-periodique-imprimable.pdf

url = "http://127.0.0.1:5000/atome/88" ##<int:numprotons>

dt = {
    'name' : "Radium",
    'val_e': 2,
    'e_negativity': 0.90,
    'Masse_Molaire': 226.0,
    'config_e_quick': "[Rn] 7(s2)",
    'config_e_full': "1(s2) 2(s2) 2(p6) 3(s2) 3(p6) 4(s2) 3(d10) 4(s2) 4(p6) 5(s2) 4(d10) 5(p6) 6(s2) 4(f14) 5(d10) 6(p6) 7(s2)",
    'charges': "(+2)"
}


resp = requests.put(url, data = dt)
print(resp.status_code)


##
##delete 57,58,59 update
##need to change the carone full config and also quick config
##revoir vanadium config
###revoir le bay Or
###revoir mercure
#### revoir le bay du zinc
##revoir le Palladium