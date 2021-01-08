#!/usr/bin/env python3

from PIL import Image
import os
import re


def obtener_imagen(path):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(('.png')):
                matches.append(os.path.join(root, filename))
    return matches


def modificar_imagen(archivo):
    size = 128, 128
    im = Image.open(archivo)
    nombre_archivo = re.sub(r'(.*).png', r'\1.jpeg', archivo)
    nombre = re.sub(r'(.*)/Images_Original/(.*)',r'\1/Images_Modified/\2',nombre_archivo)
    print(nombre)
    im = im.convert('RGB')
    im = im.rotate(90)
    im.thumbnail(size)
    im.save(nombre)
    return None


def main():
    path = r'/home/techno1731/Documents/00_DS-Roadmap/40_Coursera/Google IT Automation in Python/Image_Handling/Images_Original'
    archivos = obtener_imagen(path)
    print(archivos)
    for archivo in archivos:
        modificar_imagen(archivo)
    return None


if __name__ == "__main__":
    main()
