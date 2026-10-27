import requests
import json
import sys
artist = input("Enter the artist name: ").strip()
while True:
    try:
        number = int(input("How many Top Tracks you want to find?"))
    except ValueError:
        print("Please enter a number")
    else:
        break

url = 'https://itunes.apple.com/search'

qa = {
    "term": artist,
    "media": "music",
    "entity": "song",
    "limit" : number    
}

response = requests.get(url, params = qa)
data = response.json()
(json.dumps(data, indent=4))

st=set()
count = 1
for song in data['results']:
    title = song.get('trackName')
    if title and title not in st:
        st.add(title)
        print(f"{count}. {title}")
        count += 1