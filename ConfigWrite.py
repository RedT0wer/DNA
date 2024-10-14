import json

class Color:
    base_color_text = "",
    find_color_text = "",
    difference_color_text = "",
    stop_color_text = ""

def FilledColor():
    dictionary = eval(open("Configuration.json","r").readline())["custom"]

    Color.base_color_text = dictionary["base_color_text"]
    Color.find_color_text = dictionary["find_color_text"]
    Color.difference_color_text = dictionary["difference_color_text"]
    Color.stop_color_text = dictionary["stop_color_text"]


def GetFontSize():
    fil = open("Configuration.json","r")
    dictionary = eval(fil.readline())["custom"]
    fil.close()
    return dictionary["font_size"]

def SetFontSize(new_font_size):
    fil = open("Configuration.json","r")
    dictionary = eval(fil.readline())["custom"]
    fil.close()

    dictionary["font_size"] = new_font_size

    fil = open("Configuration.json","w")
    fil.write(json.dumps(dictionary))
    fil.close()


def GetPath():
    fil = open("Configuration.json","r")
    dictionary = eval(fil.readline())["custom"]
    fil.close()
    return dictionary["path_folder_cache"]

def SetPath(new_path_folder_cache):
    fil = open("Configuration.json","r")
    dictionary = eval(fil.readline())["custom"]
    fil.close()

    dictionary["path_folder_cache"] = new_path_folder_cache

    fil = open("Configuration.json","w")
    fil.write(json.dumps(dictionary))
    fil.close()


def ReturnDefault():
    fil = open("Configuration.json","r")
    dictionary = eval(fil.readline())
    fil.close()

    dictionary["custom"] = dictionary["default"]

    fil = open("Configuration.json","w")
    fil.write(json.dumps(dictionary))
    fil.close()