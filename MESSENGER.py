import os
def write_Message(message):
    message_file: object = open("messagecontent", 'r+');
    message_file.write(str(message));
def read_Message():
    message_file: object = open("messagecontent", 'r+');
    message_content = message_file.read(100);
    print(message_content);
