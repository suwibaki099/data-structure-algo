import sys
import os
import re
from PIL import Image, ImageFilter


def converter(image_directory, converted_directory):
    pattern = re.compile(r'/$')  # pattern to verify the last letter if it has '/'

    if not pattern.search(image_directory):  # if image does not have '/'
        print(f'does not have \'/\' in {image_directory}. Example.({image_directory}/)')
        return None

    if pattern.search(converted_directory):  # verify if the converted_directory value has '/'
        x = len(converted_directory) - 1  # to remove '/'
        directory = converted_directory
        current_directory = os.getcwd()
        path = os.path.join(current_directory, directory)
        files = os.listdir(image_directory)  # check the files inside the directory

        while True:
            if os.path.exists(path):
                for file_name in files:
                    f, e = os.path.splitext(file_name)  # f stands for fileName and e stands for Extension
                    new_img = f + '.png'
                    with Image.open(image_directory + file_name) as img:
                        filtered = img.convert('RGB')
                        filtered.save(path+new_img, 'png')
                        print('Images Processing Done!')
                break
            else:
                # file does not exit and create will a new directory
                print(f'Folder Created name: {converted_directory[:x]}')
                os.mkdir(path)
                continue
    else:
        print(f'does not have \'/\' in {converted_directory}. Example.({converted_directory}/)')


if __name__ == '__main__':
    folder1 = sys.argv[1]
    folder2 = sys.argv[2]

    converter(folder1, folder2)


"""
Backlogs:
        image_directory - check if image_directory has pictures.
"""
