from configparser import ConfigParser

def config_qumrandse(filename='database.ini', section='qumrandse'):
    """
    Establish the configuration to the Critical Editions of Second Temple Texts database
    :return: database connection
    """
    #create a parser
    parser = ConfigParser()

    #read config file
    parser.read(filename)
    
    #get section for database
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {} not found in the {} file'.format(section, filename))
    return db
        
def config_qwb(filename='database.ini', section='QWB'):
    """
    Establish the configuration to the Critical Editions of Second Temple Texts database
    :return: database connection
    """
    #create a parser
    parser = ConfigParser()

    #read config file
    parser.read(filename)

    #get section for database
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

def config_wivu(filename='database.ini', section='WIVU'):
    """
    Establish the configuration to the Critical Editions of Second Temple Texts database
    :return: database connection
    """
    #create a parser
    parser = ConfigParser()

    #read config file
    parser.read(filename)

    #get section for database
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

def img_docs(filename='paths.ini', section='PATHS'):
    """
    Serve the PATH to the img docs directory
    """
    parser = ConfigParser()

    parser.read(filename)

    docs = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            docs[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return docs['path_to_img_db']

def img(filename='paths.ini', section='PATHS'):
    """
    Serve the PATH to the img directory
    """
    parser = ConfigParser()

    parser.read(filename)

    img = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            img[param[0]] = param[1]
    else:
        raise Exception('Section {} not found in the {1} file'.format(section, filename))
    return img['path_to_img']

def nli_url(filename='urls.ini', section='URLS'):
    """
    The config file for URLS contains sites of interest to my research
    """
    parser = ConfigParser()

    parser.read(filename)

    urls = {}
    if parser.has_section(section):
        links = parser.items(section)
        for link in links:
            urls[link[0]] = link[1]
    else:
        raise Exception('Section does not exist in {1} list'.format(section, filename))
    return urls['nli']