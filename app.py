#!/usr/bin/env python
from datetime import datetime
from os import makedirs, getcwd
import requests
import re
import pickle

LOG_FILE = '-'.join([
    '/'.join([getcwd(), 'logs', 'log']),
    datetime.now().strftime("%Y%m%d")
]) + '.txt'
STATE_FILE = '/'.join([getcwd(), 'databases', 'cncs-shadowserver-to-disk']) + '.state'
DOWNLOAD_FOLDER = "./shadowserver"
MATCH = '(https:\/\/dl.shadowserver.org\/[^"]+)'
SS_URL = "https://dl.shadowserver.org/reports/index.php"

def download_element(session, url):
    try:
        RESPONSE = session.get(url)
        if RESPONSE.status_code == 200:
            FILENAME = re.findall("filename=(.+)", RESPONSE.headers['content-disposition'])[0]
            try:
                makedirs('/'.join([DOWNLOAD_FOLDER, FILENAME[11:-4]]))
            except FileExistsError:
                pass
            DEST_FILE = '/'.join([DOWNLOAD_FOLDER, FILENAME[11:-4], FILENAME])
            with open(DEST_FILE, 'wb') as outputfile:
                outputfile.write(RESPONSE.content)
            with open(LOG_FILE, 'a', encoding='utf-8') as l:
                l.write(
                    ' '.join([
                        datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3],
                        '+00:00',
                        '[INF]',
                        'Saving',
                        FILENAME,
                        'In',
                        DOWNLOAD_FOLDER,
                        '\n'
                    ])
                )
            l.close()
            return True
        else:
            raise ValueError('Response status is not 200')
    except:
        return False

def shadowserver_to_disk():
    try:
        with open(STATE_FILE, 'rb') as state:
            ALREADY_PROCESSED = pickle.load(state)
    except:
        ALREADY_PROCESSED = []
    AUTH_DETAILS = {
        'user': "",
        'password': "",
        'login':'Login'
    }
    with open(LOG_FILE, 'a', encoding='utf-8') as l:
        l.write(
            ' '.join([
                datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3],
                '+00:00',
                '[INF]',
                'Connecting To',
                SS_URL,
                '\n'
            ])
        )
    l.close()
    SESSION = requests.Session()
    RESPONSE = SESSION.post(SS_URL, data=AUTH_DETAILS)
    HTML_CONTENT = RESPONSE.content.decode('utf-8')
    for download_me in re.finditer(MATCH, HTML_CONTENT, re.MULTILINE):
        URL = download_me.group(1)
        if URL not in ALREADY_PROCESSED:
            download_element(SESSION, URL)
            ALREADY_PROCESSED.append(URL)
    with open(STATE_FILE, 'wb') as state:
        pickle.dump(ALREADY_PROCESSED, state)
    state.close()

if __name__ == "__main__":
    shadowserver_to_disk()
