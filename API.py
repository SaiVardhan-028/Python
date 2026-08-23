#import json
#import sys

import requests

def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            params={"q": artist}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Didn't complete program")
        return

    content = response.json()

    for artwork in content["data"]:
        print(f" * {artwork['title']}")

main()
    
    
#if len(sys.argv) != 2:
#   sys.exit()
# + sys.argv[1])
#print(json.dumps(response.json()))
