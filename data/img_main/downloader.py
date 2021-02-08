# -*- coding: utf-8 -*-

import urllib3
import csv
import re
import logging
import datetime
import os
from config import nli_url


def pull_down(f, plate, res):
    """
    Download the iiif image to local machine
    """
    nli = nli_url()
    
    http = urllib3.PoolManager()

    logging.basicConfig(filename='image_downloader.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
    logging.debug('Downloading {} at pct:{}'.format(f, res))
    
    url = str(nli) + str(f) + "/full/pct:" + str(res) + "/0/default.jpg"
    
    img = http.request('GET', url, preload_content=False)
    with open("img/P" + str(plate) + "/" + str(f), 'wb') as out:
        logging.debug('Downloaded {} …'.format(f))
        while True:
            data = img.read(1500)
            if not data:
                break
            
            out.write(data)
        print('{} is saved …'.format(f))