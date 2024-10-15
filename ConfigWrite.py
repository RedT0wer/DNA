import json

class Config:
    def __init__(self):
        json_data = open("Configuration.json","r")
        dictionary = json.load(json_data)
        self.__dict__ = dictionary['custom']
        json_data.close()

    def return_default(self):
        json_data = open("Configuration.json","r")
        dictionary = json.load(json_data)
        json_data.close()
        
        dictionary["custom"] = dictionary["default"]

        json_data = open("Configuration.json","w")
        json_data.write(json.dumps(dictionary))
        json_data.close()

    def apply_settings(self):
        json_data = open("Configuration.json","r")
        dictionary = json.load(json_data)
        json_data.close()
        
        dictionary["custom"] = self.__dict__

        json_data = open("Configuration.json","w")
        json_data.write(json.dumps(dictionary))
        json_data.close()
