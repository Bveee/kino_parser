import json

from bs4 import BeautifulSoup


def main():
    html = open('kp_test4.html').read()
    soup = BeautifulSoup(html, 'html.parser')

    div = soup.find('div', {"class": "block_left"})
    a = div.find('a', {"name": "producer"})
    act_name = a.find_previous_siblings('div')
    # разобрать кусок
    # aact = actn.find('a', {"name": "actor"})
    # actname = aact.find_previous_siblings('div')
    # print(type(a))
    #
    act = act_name[-4::-1]  # переворачивает список, как на сайте и обрезает режисера 1
    print(act)
    dict_act = dict()
    for index, info_act in enumerate(act):
        name = info_act.find('div', {'class': 'name'})
        role = info_act.find('div', {'class': 'role'}).get_text()
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
    save_as_json(actors, 'file_kp3.json')
