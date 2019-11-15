import argparse
from PIL import Image
import os

if __name__ == "__main__":

    # parse input arguments
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "input_folder",
        type=str
    )
    argparser.add_argument(
        "target_folder",
        type=str
    )
    arguments = argparser.parse_args()

    print(arguments)

    if not os.path.exists(arguments.target_folder):
        os.mkdir(arguments.target_folder)

    for file in os.listdir(arguments.input_folder):
        clean_filename = os.path.splitext(file)[0]
        img = Image.open(f"{arguments.input_folder}/{file}")
        img.save(f"{arguments.target_folder}/{clean_filename}.png", "png")
