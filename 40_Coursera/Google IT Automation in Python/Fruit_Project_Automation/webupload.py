#!/usr/bin/env python3

import os
import requests
import re
import changeImage

def get_files(path, keys, extension=".txt"):

    """ Generates a list of files that contain plain text
    then for each file in the list opens the file read the contens
    splits it by line and then creates a list of dictionaries with the keys"""
    file_names = []
    files_path = []
    files_dict = []
    for archivo in os.scandir(path):
        if archivo.name.endswith(extension):
            files_path.append(os.path.join(path, archivo.name))
            file_names.append(archivo.name)
        else:
            continue
    for i in range(len(file_names)):
        file_names[i]=re.sub(r'.txt',r'.jpeg',file_names[i])
    files = list(zip(files_path, file_names))

# ------ Debug Lines ------
#   print(files)
# ------ Debug Lines ------

    for ruta, archivo in files:
#        with open(ruta, mode='a') as fa:
#            fa.write(archivo)
        with open(ruta, mode='r') as fr:
            text = fr.read().splitlines()
        files_dict.append(dict(zip(keys, text)))

    for index, d in enumerate(files_dict):
        weight = int(files_dict[index]['weight'].split().pop(0))
        files_dict[index]['weight'] = weight

# ------ Debug Lines ------
#   print(files_dict)
# ------ Debug Lines ------

    return files_dict


def post_text(url, files_dict):
    for archivo in files_dict:
        response = requests.post(url, data=archivo)
    return None


def up_image(url, list_images):
    for image in list_images:
        with open(image, 'rb') as im:
            response = requests.post(url, files={'file': im})
    return None


# Example of use and standalone application
def main():
    keys = ["name", "weight", "description", "image_name"]
    path_text = r'/home/studentxxx/supplier-data/descriptions/'
    path_images = r'/home/studentxxx/supplier-data/images_modified/'
    files_dict = get_files(path_text, keys)
    files_im = changeImage.obtener_imagen(path_images, extension='.jpeg')
    url_images = r'http://localhost/upload/'
    url_text=r'http://localhost/fruits/'
    up_image(url_images, files_im)
    #post_text(url_text, files_dict)
    return None


if __name__ == "__main__":
    main()
