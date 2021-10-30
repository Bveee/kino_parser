import json
import requests

from bs4 import BeautifulSoup
from settings import *


def main():
    # with open(html_path, 'r') as f: # из файла
    #     html = f.read()
    html = requests.get(url=url_path, params=headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    div = soup.find('div', {"class": "block_left"})
    a = div.find('a', {"name": "producer"})
    act_name = a.find_previous_siblings('div')
    act_num = int(act_name[0].find('div', {"class": "num"}).get_text()[:-1])
    act = act_name[act_num-1::-1]  # переворачивает список, как на сайте и выбирает актеров

    dict_act = dict()
    for index, info_act in enumerate(act):
        name = info_act.find('div', {'class': 'name'})
        role = info_act.find('div', {'class': 'role'}).get_text()[4:].replace(', в титрах не указана', '')
        rus_name = name.find('a').get_text()
        eng_name = name.find('span').get_text()
        dict_act.update({index+1: {'rus_name': rus_name, 'eng_name': eng_name, 'role': role}})
    return dict_act


def save_as_json(payload: dict, path_to_file: str, add_indentation: bool = False):
    if add_indentation:
        with open(path_to_file, 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=4)
    else:
        with open(path_to_file, 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False)


if __name__ == '__main__':
    actors = main()
    print(actors)
    save_as_json(actors, json_path)
