import json
import random


async def get_joke(path: str = "app/data/jokes.json") -> str:
    with open(path) as f:
        data = json.load(f)
        jokes = data.get("jokes")
        len_of_joke = len(jokes)
        joke_id = random.randint(0, len_of_joke)
        print(jokes[joke_id])
        return jokes[joke_id]







