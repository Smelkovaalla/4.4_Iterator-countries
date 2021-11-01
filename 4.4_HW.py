import os
import json
from pprint import pprint
import hashlib


class Country_Iterator:
    def __init__(self, json_file):
        with open(file_json, 'r') as file:
            self.my_json = json.load(file)
        self.start = -1
        self.end = len(self.my_json)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.my_json[self.start]['name']['common']


if __name__ == '__main__':
    def generate(path):
        with open(path) as file:
            for line in file:
                yield line.upper()

    url = "https://en.wikipedia.org/wiki/"
    file_json = os.path.join(os.getcwd(), "countries.json")
    for name_country in Country_Iterator(file_json):
        name_fix = url + name_country.replace(" ", "_")
        pprint(f'Город {name_country} - {name_fix}')
        hash_object = hashlib.md5(b'{name_fix}')
        print(hash_object.hexdigest())
    for enemy in generate(file_json):
        print(enemy.split())
