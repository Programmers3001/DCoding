import json

with open(r'dcodingmodel.json', encoding='utf-8') as file:
    model = json.load(file)
model_reversed = {value: key for key, value in model.items()}
def encode(string):
    new_string = ""
    for i in range(len(string)):
        try:
            char = string[i].replace(string[i], model[string[i]])
            #print(char)
        except Exception as e:
            #print(e)
            char = string[i]
        new_string+=char
    return new_string
def decode(string):
    new_string = ""
    for i in range(len(string)):
        try:
            char = string[i].replace(string[i], model_reversed[string[i]])
        except Exception as e:
            char = string[i]
        new_string+=char
    return new_string
if __name__ == "__main__":
    print(encode("David je super cool!"))
    a = encode("David je super cool!")
    print(decode(a))