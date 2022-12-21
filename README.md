Ce projet est open source ; le code est disponible pour tout le monde.
Il suffit de host ce project sur le cloud (aws, heroku, google cloud...)


#GET

## PYTHON
```
import requests

params = "<id:numéro de proton de l'atome voulu>"
url = "<whatever the host url>" + id
resp = requests.get(url)
print(resp.content)
```

**Cette commande retourne les élements suivants :

-Numéro de protons
-L'électronégativité
-Nombre d'électrons de valence
-La masse Molaire
-Les charges
-le nom de l'atome
-La configuration électronique abrégée et celle qui complète
-Les charges

##Javascript

```
let params = "<id:numéro de proton de l'atome voulu>" 

url = "<hosturl>"
fetch(url+params)
  .then((response) => response.json())
  .then((data) => console.log(data));
```