#!/usr/bin/env python3
import os
import datetime
import reports
import supplier_upload
import emails

def create_report():
    keys = ["name", "weight", "description", "image_name"]
    path = r'/home/student-04-b8ac6ffecd5a/supplier-data/descriptions/'
    files_dict = supplier_upload.get_files(path, keys)
    filename='/tmp/processed.pdf'
    now = datetime.datetime.now()
    title= "Processed Update on "+ now.strftime("%b %d, %Y")
    additional_info = r"<br />\
    name: {}<br />\
    weight: {} lbs<br />\
    <br />\
    name: {}<br />\
    weight: {} lbs<br />\
    <br />\
    name: {}<br />\
    weight: {} lbs<br />\
    <br />\
    name: {}<br />\
    weight: {} lbs<br />\
    <br />\
    name: {}<br />\
    weight: {} lbs<br />\
    <br />\
    name: {}<br />\
    weight: {} lbs<br />\
    <br />\
    name: {}<br />\
    weight: {} lbs<br />\
    <br />\
    name: {}<br />\
    weight: {} lbs<br />\
    <br />\
    name: {}<br />\
    weight: {} lbs<br />\
    <br />\
    name: {}<br />\
    weight: {} lbs<br />\
    <br />".format(
            files_dict[0]['name'],
            files_dict[0]['weight'],
            files_dict[1]['name'],
            files_dict[1]['weight'],
            files_dict[2]['name'],
            files_dict[2]['weight'],
            files_dict[3]['name'],
            files_dict[3]['weight'],
            files_dict[4]['name'],
            files_dict[4]['weight'],
            files_dict[5]['name'],
            files_dict[5]['weight'],
            files_dict[6]['name'],
            files_dict[6]['weight'],
            files_dict[7]['name'],
            files_dict[7]['weight'],
            files_dict[8]['name'],
            files_dict[8]['weight'],
            files_dict[9]['name'],
            files_dict[9]['weight'],
            )
    reports.generate(filename, title, additional_info)
    return None

def enviar_email():
    sender = 'automation@example.com'
    recipient ='student-04-b8ac6ffecd5a@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body ='All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachment_path = '/tmp/processed.pdf'
    message = emails.generate(sender, recipient, subject, body, attachment_path)
    emails.send(message)
    return None

def main():
    print("Creating report: ", end="")
    create_report()
    print('done')
    print("Sending email: ", end="")
    enviar_email()
    print("done")
    return None

if __name__ == "__main__":
    main()
