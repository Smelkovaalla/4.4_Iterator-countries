import json
from pprint import pprint
import hashlib

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
  city_list = []
  url = "https://en.wikipedia.org/wiki/"
  for i in Country_iterator('countries.json'):
    namefix = i.replace(" ", "_")
    url_city = url + namefix
    # pprint(f'Город {i} - {url_city}')
    city_list. append(url_city)

            
  def gen():
    for line in city_list:
      yield line.upper()
      
  for item in gen():
    hash_object = hashlib.md5(b'item')
    pprint(hash_object.hexdigest())   
    pprint(item)

