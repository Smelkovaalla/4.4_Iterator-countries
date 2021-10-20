import json
from pprint import pprint

class Country_iterator:
    def __init__(self, file_json):
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
    for i in Country_iterator('countries.json'):
        pprint(f'Город {i} - https://en.wikipedia.org/wiki/{i}')



