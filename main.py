#!/usr/bin/env python3

from fastapi import FastAPI
import requests

def main():
  base_url = 'https://pokeapi.co/api/v2/'
  add_url = 'pokemon/'
  id = '2'

  response = requests.get(base_url + add_url + id)
  response = response.json()
  #画像
  print(response['sprites']['front_default'])
  #高さ
  print(response['height'])
  #重さ
  print(response['weight'])
  result = get_pokemon_data_japanese(response['name'])
  if isinstance(result, tuple):
    japanese_name, description = result
      #日本語名
    print(japanese_name)
      #説明
    print(description)

def get_pokemon_data_japanese(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()

      #Japanese name
      japanese_name = None
      for name in data['names']:
        if name['language']['name'] == 'ja-Hrkt':
          japanese_name = name['name']
          break
      #Description
      japanese_description = None
      for entry in data['flavor_text_entries']:
        if entry['language']['name'] == 'ja-Hrkt':
          japanese_description = entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
          break
  
      if japanese_name and japanese_description:
        return japanese_name, japanese_description

if __name__ == '__main__':
  main()

"""
app = FastAPI()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
  if q:
    return {"item_id": item_id, "q": q}
  return {"item_id": item_id}
"""
