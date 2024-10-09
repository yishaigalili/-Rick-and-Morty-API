import requests
import csv
from flask import Flask, jsonify
import logging
from typing import List, Dict, Any

app = Flask(__name__)

class Character:
    def __init__(self, name: str, location: str, image: str):
        self.name = name
        self.location = location
        self.image = image

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "location": self.location,
            "image": self.image
        }

def get_characters() -> List[Character]:
    characters = []
    page = 1
    while True:
        response = requests.get(f"https://rickandmortyapi.com/api/character/?page={page}")
        if response.status_code != 200:
            break
        
        data = response.json()
        for char in data['results']:
            if (char['species'] == 'Human' and 
                char['status'] == 'Alive' and 
                char['origin']['name'] == 'Earth (C-137)'):
                
                character = Character(
                    name=char['name'],
                    location=char['location']['name'],
                    image=char['image']
                )
                characters.append(character)
        
        if data['info']['next'] is None:
            break
        page += 1
    
    return characters

def write_to_csv(characters: List[Character], filename: str = 'characters.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Location', 'Image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for char in characters:
            writer.writerow({
                'Name': char.name,
                'Location': char.location,
                'Image': char.image
            })

@app.route('/characters', methods=['GET'])
def get_characters_endpoint():
    characters = get_characters()
    return jsonify([char.to_dict() for char in characters])

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    characters = get_characters()
    write_to_csv(characters)
    app.run(host='0.0.0.0', port=5000)