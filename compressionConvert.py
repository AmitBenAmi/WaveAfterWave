import json

keys = None

with open('word_to_bytes.json', 'r') as f:
    keys = json.load(f)

def convertWordToBinary(key):
    if key not in keys.keys() or not isinstance(keys[key], int):
        return None
    return keys[key]

def convertTextToBinary(text):
    data = bytearray([])
    for word in text.strip().split(' '):
        conversion = convertWordToBinary(word)
        if conversion is None:
            return None

        data.append(conversion)

    return data