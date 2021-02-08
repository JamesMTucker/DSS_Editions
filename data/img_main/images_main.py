# -*- coding: utf-8 -*-

import sys
import argparse
from img_sql import fetch_images
from crawler import fetch_iaa
from downloader import pull_down
import pandas as pd
from config import nli_url
import re
import os
import logging
    

def main(args):
    """
    Process request to download images from the iaa
    :size: image size for the iiif nli api request
    :iaa_plate: iaa plate number
    :q_siglum: alternate option to scrape the Leon Levy Website for PAM plates associated with iaa_plate
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("size", help="Designate the image size, e.g., 100 or 50", type=str)
    parser.add_argument("iaa_plate", help="Please specificy a plate number or list of plate numbers")
    parser.add_argument("q_siglum", help="Optional: add a Q siglum to get associated PAMs", nargs='?')
    
    args = parser.parse_args()
    
    iaa_imgs = fetch_images()

    if not os.path.exists('img/P' + str(args.iaa_plate)):
        os.mkdir('img/P' + str(args.iaa_plate))

    # filter df.series on iaa_plate (sometimes unwarranted plates will be found)
    plate_info = iaa_imgs[iaa_imgs.PLATE.str.contains(args.iaa_plate)]

    if plate_info.empty is True:
        print(f'Found no images for {args.iaa_plate}.')
    else:
        for index, row in plate_info.iterrows():
            if re.match('^M|^I', row['file_name']):
                continue
            else:
                if re.match('^P|^' + str(args.iaa_plate) + '-', row['file_name']):
                    print("Downloading {} …".format(row['file_name']))
                    pull_down(row['file_name'], args.iaa_plate, args.size)
                else:
                    continue

    if args.q_siglum is not None:
        pam_images = fetch_iaa(args.q_siglum)
        for img in pam_images:
            pam = img.replace(".", "")
            pam_file = iaa_imgs[iaa_imgs.file_name.str.contains(pam)]
            if pam_file.empty is True:
                print("The PAM plate does not exist on the NLI server")
            else:
                for index, row in pam_file.iterrows():
                    print("Downloading {} …".format(row['file_name']))
                    pull_down(row['file_name'], args.iaa_plate, 100)
    else:
        print("No associated PAM images were downloaded")

if __name__ == '__main__':
    main(sys.argv[1:])