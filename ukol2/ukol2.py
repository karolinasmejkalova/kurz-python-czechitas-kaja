# ičo = 22834958
# část jedna
import json
import requests

ico = input("ICO:\n")

response = requests.get(
    f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")

data = response.text
json_data = json.loads(data)

if not "obchodniJmeno" in json_data:
    print("Neplatne ICO")
else:
    print(json_data["obchodniJmeno"])
    print(json_data["sidlo"]["textovaAdresa"])

#část dvě
name = input("Nazev subjektu:")

response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat",
                         headers={"accept": "application/json", "Content-Type": "application/json", }, data='{"obchodniJmeno" : "' + name + '"}')

data = json.loads(response.text)

if not "pocetCelkem" in data:
    print("ERROR")
else:
    print("Nalezeno subjektu:", data["pocetCelkem"])

    for i in data["ekonomickeSubjekty"]:
        print(i["obchodniJmeno"])
