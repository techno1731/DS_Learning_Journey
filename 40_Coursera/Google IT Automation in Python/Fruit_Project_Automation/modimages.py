#!/usr/bin/env python3

from PIL import Image
import os
import re


def obtener_imagen(path, extension=".tiff"):

    """ Generates a list with all files in directory that matches the desired
    extension"""

    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith((extension)):
                matches.append(os.path.join(root, filename))
    return matches


def modificar_imagen(archivo, Images_Original, Images_Modified,
                     size=0, degrees=0,
                     extension_o=".tiff", extension_d=".jpeg"):

    """ Modifies an Image archivo to tupple size and rotates by degrees
    then changes the extension from extension_o to extension_d and leaves
    the original in directory Images_Original and the Modified in
    directory Images_Modified."""

    im = Image.open(archivo)
    extension = re.sub(r'(.*)' + extension_o, r'\1' + extension_d, archivo)
    nombre = re.sub(r'(.*)/' + Images_Original + r'/(.*)',
                    r'\1/' + Images_Modified + r'/\2',
                    extension)

# ------ Debug Lines START ------
#    print(nombre)
# ------ Debug Lines END ------

    if degrees != 0:
        im = im.rotate(degrees)
    if size != 0:
        im.thumbnail(size)
    im.save(nombre)
    return None

# Example of use and standlone operation


def main():
    path = '/home/studentxxx/supplier-data/images'
    extension_o = '.tiff'  # Extension of the original images default=tiff
    extension_d = '.jpeg'  # Desired extension of the images default=jpeg
    Images_Original = 'CurrentDirectory'  # Image directory name
    Images_Modified = 'DesiredDirectory'  # Directory must exist
    size = 600, 400  # The desired size, for reduction only dafault=0
    degrees = 0  # Desired degrees to rotate the image default=0
    archivos = obtener_imagen(path)

# ------ Debug Lines START ------
    print(archivos)
# ------ Debug Lines END ------

    # Iterate over all files in archivos and modify only extension and size
    for archivo in archivos:
        modificar_imagen(archivo, Images_Original, Images_Modified, size)
    return None


if __name__ == "__main__":
    main()
