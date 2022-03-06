import json
from enum import Enum, auto

CONFIG_FILE_NAME = "/home/pi/Pimoroni/unicornhathd/examples/traffic-light/light-config.json"

GIF_COLOR = "gif_color"


def color_from_string(value):
    for color in Color:
        if color.name == value:
            return color
    # if we are here, there was an error
    raise ValueError(f"{value} is no valid Color")


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    UKRAINIAN = auto()
    CLASSIC = auto()


class LightConfig:
    def __init__(self, config_data):
        self.gif_color = color_from_string(config_data[GIF_COLOR])

    def to_dict(self):
        return {GIF_COLOR: self.gif_color}


def read_config(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data


def write_config(filename, config_data):
    with open(filename, "w") as config_file:
        json.dump(config_data, config_file)


def set_next_mode():
    color = None
    while color is None:
        print("Available modes\n"
              "Red -> r\n"
              "Green -> g\n"
              "Blue -> b\n"
              "Ukrainian -> u\n"
              "Classic -> c\n")
        key = input("choose wisely...")

        if key == "r":
            color = Color.RED
        elif key == "g":
            color = Color.GREEN
        elif key == "b":
            color = Color.BLUE
        elif key == "u":
            color = Color.UKRAINIAN
        elif key == "c":
            color = Color.CLASSIC
        else:
            print(f"{key} is not a valid code")

    print(f"chose {color}")
    write_config(CONFIG_FILE_NAME, {GIF_COLOR: color.name})


color_file_map = {
    Color.RED: "red_pimoroni.png",
    Color.BLUE: "blue_pimoroni.png",
    Color.GREEN: "green_pimoroni.png",
    Color.UKRAINIAN: "ukranian_pimoroni.png",
    Color.CLASSIC: "pimoroni.png"
}


def to_gif_name(color):
    return color_file_map[color]


if __name__ == "__main__":
    while True:
        set_next_mode()
