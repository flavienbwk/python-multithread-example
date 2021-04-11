#!/bin/python3

# Let's say you want to download files associated to each user listed in your SQLite database as following :
#
# ```csv
# user_id,file_url
# 1,https://i.imgur.com/XTOuirC.jpg
# 2,https://i.imgur.com/ddOusrC.jpg
# ...
#
# You can run the following script

import os
import sqlite3
import urllib.request
import concurrent.futures

def download_file(file_url, dst_file):
    if not file_url:
        print(f"Empty file {dst_file}")
        return
    if not os.path.exists(dst_file):
        try:
            print(f"Downloading {dst_file}")
            urllib.request.urlretrieve(file_url, dst_file)
        except Exception as e:
            print(e)
            print(f"Failed to retrieve {dst_file}'s file")
    return

def main():
    connection = sqlite3.connect("my_sqlite.db")
    cursor = connection.cursor()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for row in cursor.execute('SELECT * FROM users;'):
            user_id = row[0]
            file_url = row[1]
            dst_file = f"./files/{str(user_id)}.jpg"
            executor.submit(download_file, file_url, dst_file)
    connection.close()

if __name__ == "__main__":
    main()
