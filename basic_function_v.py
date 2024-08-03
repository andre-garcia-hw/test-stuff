import requests
def get_basic():
    try:
        url=f"https://pokeapi.co/api/v2/pokemon/1"
        response=requests.get(url)
        data=response.json()
        print(f"The name of the pokemon is: {data['name']}")
        print(f"The height is: {data['weight']}")
        print(f"The weight is: {data['height']}")
        print(f"The base exp is: {data['base_experience']}")
    except requests.exceptions.HTTPError as e1:
        print(f"The was an HTTP Error: {e1}") 
    except requests.exceptions.ConnectionError as e2:
        print(f"The was an Connection Error {e2}") 
    except requests.exceptions.Timeout as e3:
        print(f"The was a Timeout Error {e3}") 
    except Exception as e4:
        print(f"The other errors {e4}") 