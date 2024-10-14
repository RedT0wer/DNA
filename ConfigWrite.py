import json

class Color:
    base_color_text = "",
    find_color_text = "",
    difference_color_text = "",
    stop_color_text = ""

def FilledColor():
    dictonary = eval(open("Configuration.json","r").readline())

    Color.base_color_text = dictonary["custom"]["base_color_text"]
    Color.find_color_text = dictonary["custom"]["find_color_text"]
    Color.difference_color_text = dictonary["custom"]["difference_color_text"]
    Color.stop_color_text = dictonary["custom"]["stop_color_text"]