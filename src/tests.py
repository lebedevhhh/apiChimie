import requests
import json
import pprint 



PP = pp = pprint.PrettyPrinter(indent=4)

##ressources ---> file:///C:/Users/ilyas/OneDrive/Desktop/allSkullzRelated/science/Tableau-periodique-imprimable.pdf

url = "http://127.0.0.1:5000/atome/" ##<int:numprotons>


# dt = {
#     "config_e_quick": "[Ar] 4(s2) 3(d3)",
# }

resp = requests.get(url)
print(resp.status_code)
content = resp.content.decode("utf-8")
content = json.loads(content)
PP.pprint(content)


# resp = requests.patch(url, data = dt)
# print(resp.status_code)
# print(resp.content)

# resp = requests.put(url, data = dt)
# print(resp.status_code)

#revoir le bay 100-116
#revoir le 94
## revoire 86 a 89
##delete 57,58,59 update
##need to change the carone full config and also quick config