

import json


def load(lang):
    return json.load(open(f"./lang/id.json", "r"))
    return json.load(open(f"./lang/en.json", "r"))
