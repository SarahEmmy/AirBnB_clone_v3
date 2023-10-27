#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Creates a tgz archive from the web_static folder
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(timestamp)

        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))

        print("Timestamp:", timestamp)
        print("File Name:", file_name)

        return file_name
    except Exception as e:
        return None

if __name__ == "__main__":
    result = do_pack()
    if result:
        print("Web static packed: {}".format(result))
    else:
        print("Packaging web static failed")
