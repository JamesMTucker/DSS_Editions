# -*- encoding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import os, re
import csv
import builtwith
import requests

def get_source(scroll):
    """
    Return source for Leon Levy Page
    """

    scroll = scroll + '-1'

    browser = webdriver.Chrome()
    browser.get("https://www.deadseascrolls.org.il/explore-the-archive/manuscript/" + scroll)
    print("Opening Google Chrome at " + scroll + " to download ... ")
    time.sleep(5)

    #Assign page source var
    html = browser.page_source

    ##Get Soup of HTML to calculate page loads
    soup = BeautifulSoup(html, 'lxml')

    #Get sh-result-header.h2 to divide results by total (as of 10-04-2019)
    refresh_times = soup.find("div", class_='sh-result-header')
    
    ## Adjust wait time dependent on internet speed
    count = refresh_times.h1.text.strip()
    times = re.findall(r'\d+', count)

    ## Clean Numbers to Get times to refresh
    if int(times[1]) < 24:
        times[1] = 24
    
    refresh = int(times[1]) / int(times[0])
    x2load = str(refresh)
    print("Chrome will refresh " + x2load + " time(s).")

    if refresh == 1:
        pass
    else:
        load_more_link = browser.find_element_by_id("loadmore")
        count = 12
        for i in range(0, int(refresh)):
            try:
                load_more_link.click()
                time.sleep(5)
                count = int(count) + 12
                print("Refreshing html…")
            except Exception:
                pass
    browser.implicitly_wait(7)
    html_source = browser.page_source
    browser.close()
    
    with open("img/ll_source/" + scroll + ".html", 'w') as htm:
        htm.write(html_source)
        htm.close()
    return html_source

def parse_source(html):
    """
    Parse source and return PAMs in list
    """
    PAMS = []
    comp_data = {}
    frag_data = {}

    soup = BeautifulSoup(html, 'lxml')

    ## Element :: Get The Title of the Composition
    title = soup.find('div', {"id": "sidebar-header"})
    ed_humre = title.h1.text.replace('\n', '').strip()
    comp_data['ed_humre'] = ed_humre

    sigla_html = title.find("span", class_="ellipsis")
    sigla = sigla_html.text.strip()
    spl = re.compile(u'\u2013\u2009').split(sigla)
    ed_sig = spl[0].strip()
    ed_abbr = spl[1].strip()
    comp_data['ed_abbr'] = ed_abbr

    # Segregate List Items
    list_descrip = soup.find("dd")
    remainderCon = soup.find_all("dd", class_='link')

    # CHILD SITE: Get site location and discard column name (cf. l 20)
    classes = list_descrip.find_all("dt") #Assume that this tuple and the next match.
    siteHeader = classes[0].text.strip()
    # ste = remainderCon[0].text.replace('Qumran, ', '').strip()         #COMPLETE

    # CHILD Manuscript Type 1: Get manuscript type (assume this is IAA designation)
    mssHeader = classes[1].text.strip()
    iaa_lit = remainderCon[1].text.strip()
    comp_data['iaa_lit'] = iaa_lit

    # CHILD Composition Type 2: Get composition type (assume this is DJD/2nd Lit)
    compHeader = classes[2].text.strip()
    iaa_comp = remainderCon[2].text.strip()
    comp_data['iaa_comp'] = iaa_comp

    # CHILD Langauge 3
    langHeader = classes[3].text.strip()
    lang = remainderCon[3].text.strip()
    comp_data['lang'] = lang

    # CHILD Script 6
    scrHeader = classes[4].text.strip()
    scr_type = remainderCon[4].text.strip()
    comp_data['scr_type'] = scr_type

    # CHILD Period 5
    perHeader = classes[5].text.strip()
    pal_date = remainderCon[5].text.strip()
    comp_data['pal_date'] = pal_date

    # CHILD Material
    matHeader = classes[6].text.strip()
    mater = remainderCon[6].text.strip()
    comp_data['mater'] = mater

    ## Maagerim Transcription Link
    maag_container = soup.find_all("dd", class_='link')
    try:
        maag_html = maag_container[7]
        maag_link = maag_html.find('a')['href']
        comp_data['maag'] = maag_link
    except Exception:
            maag_html = "Null"
            comp_data['maag'] = None

    # Publication details (as list)
    publications = soup.find("div", {"id": "publications"})
    pubs = publications.find_all("li")

    results = soup.find("div", {"id": "results-container"})
    images = results.find_all("div", class_="result-item")
    
    for index, image in enumerate(images):
        frag_data['id'] = index
        frag_data['href'] = image.find('a')['href']

        thumb = image.find('div', class_="ms-image-thumb").attrs
        thumb_re = re.compile(r'((http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9%_:?\+.~#&//=]*))')
        thumb_http = thumb_re.search(thumb['style'])
        frag_data['thumb'] = thumb_http.group(1)

        image_info = image.find('div', class_="img-image-info")
        image_elems = image_info.find_all('div')
        frag_data['b_num'] = image_elems[0].text.strip()
        pam_re = re.compile(r'PAM ([M|I][0-9-.]+)')
        pam_num = pam_re.search(image_elems[2].text.strip())
        if pam_num is None:
            frag_data['PAM'] = "Null"
        else:
            frag_data['PAM'] = pam_num.group(1)
            PAMS.append(frag_data['PAM'])
    return PAMS

def fetch_iaa(q_sig):
    """
    Grab source page for Q_Siglum and Parse PAM Images
    """
    scroll_source = get_source(q_sig)
    return parse_source(scroll_source)
    