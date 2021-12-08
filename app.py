#!/usr/bin/env python3
from os import makedirs, getcwd, path
import threading
import requests
import re

MATCH = '(https:\/\/dl.shadowserver.org\/[^"]+)'
SS_URL = "https://dl.shadowserver.org/reports/index.php"

def download_element(session, url):
    try:
        RESPONSE = session.get(url)
        if RESPONSE.status_code == 200:
            FILENAME = re.findall("filename=(.+)", RESPONSE.headers['content-disposition'])[0]
            try:
                makedirs('/'.join([getcwd(), "shadowserver", FILENAME[11:-4]]))
            except FileExistsError:
                pass
            DEST_FILE = '/'.join([getcwd(), "shadowserver", FILENAME[11:-4], FILENAME])
            if not path.isfile(DEST_FILE):
                with open(DEST_FILE, 'wb') as outputfile:
                    outputfile.write(RESPONSE.content)
    except:
        pass

if __name__ == "__main__":
    try:
        makedirs('/'.join([getcwd(), "shadowserver"]))
    except FileExistsError:
        pass
    SESSION = requests.Session()
    RESPONSE = SESSION.post(
        SS_URL,
        data={
        'user': "",
        'password': "",
        'login':'Login'
        }
    )
    HTML_CONTENT = RESPONSE.content.decode('utf-8')
    threads = list()
    for download_me in re.finditer(MATCH, HTML_CONTENT, re.MULTILINE):
        URL = download_me.group(1)
        x = threading.Thread(target=download_element, args=(SESSION, URL), daemon=True)
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()
