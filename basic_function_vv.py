import requests

def get_pokemon_data(pokemon_id):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        print(f"The name of the Pokémon is: {data['name']}")
        print(f"The height is: {data['height']}")
        print(f"The weight is: {data['weight']}")
        print(f"The base experience is: {data['base_experience']}")
    except requests.exceptions.HTTPError as e1:
        print(f"There was an HTTP Error: {e1}")
    except requests.exceptions.ConnectionError as e2:
        print(f"There was a Connection Error: {e2}")
    except requests.exceptions.Timeout as e3:
        print(f"There was a Timeout Error: {e3}")
    except Exception as e4:
        print(f"Other errors: {e4}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <pokemon_id>")
    else:
        get_pokemon_data(sys.argv[1])
