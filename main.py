import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
full_dict = resp.json()
Hulk_info = []
CaptainAmerica_info = []
Thanos_info = []
intelligence_dict = {}


def add_info():
    for i in full_dict:
        if i['name'] == 'Hulk':
            Hulk_info.append(i)
        elif i['name'] == 'Captain America':
            CaptainAmerica_info.append(i)
        elif i['name'] == 'Thanos':
            Thanos_info.append(i)


def get_intelligence_dict():
    for i in Hulk_info:
        intelligence_dict['Hulk'] = i['powerstats']['intelligence']
    for i in CaptainAmerica_info:
        intelligence_dict['Captain America'] = i['powerstats']['intelligence']
    for i in Thanos_info:
        intelligence_dict['Thanos'] = i['powerstats']['intelligence']


if __name__ == "__main__":
    add_info()
    get_intelligence_dict()
    print(f"{max(intelligence_dict.keys())} - {max(intelligence_dict.values())}")
