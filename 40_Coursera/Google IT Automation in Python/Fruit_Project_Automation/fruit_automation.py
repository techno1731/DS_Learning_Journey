#!/usr/bin/env python3

import os
import locale
import sys
import emails
import reports
import modimages
import webupload



def main():

    # Modify Images
    path = '/home/student-03-6de87c8d82cf/supplier-data/images'
    Images_Original = 'images'
    Images_Modified = 'images_modified'
    size = 600, 400  # Required size
    archivos = modimages.obtener_imagen(path)
    for archivo in archivos:
        modimages.modificar_imagen(archivo, Images_Original, Images_Modified, size)

    # POST Images to DJANGO REST
    keys = ['name','weight','description','image_name']  #Keys of data
    path_images = '/home/student-03-6de87c8d82cf/supplier-data/images_modified/'
    path_text = '/home/student-03-6de87c8d82cf/supplier-data/descriptions/'
    files_im = modimages.obtener_imagen(path_images)
    files_dict = webupload.get_files(path_text, keys)
    #url = r'http://localhost/upload/'
    url = r'http://[linux-instance-external-IP]/fruits'
    webupload.up_image(url, files_im)
    webupload.post_text()



#In case of JSON files.

    # Load the data and format it
    # filename = r'file'
    #data = load_data(filename)
    #data_f = format_data(data)
    #data_p = process_data(data_f)

# Example of table
    # table_data = [
    # ['Name', 'Amount', 'Value'],
    # ['elderberries', 10, 0.45]]

    #Generate PDF
    reports.generate("/tmp/report.pdf", "A complete inventory of my fruit", "This is all my fruit.",
                     table_data)
    # Send Email
    sender = "sender@example.com"
    reciever = "reciever@example.com"
    subject = "List of fruits"
    body = "Hi\n\nI'm sending an attachment with all my fruit."

    message = emails.generate(sender, reciever, subject, body, "/tmp/report.pdf")
    emails.send(message)



