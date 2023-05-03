from configparser import ConfigParser


def parse_token(filename="config.ini", section="token"):
    "Считываем конфигурацию"
    parser = ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            if param[0] == "token":
                token = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file'.format(section, filename))
    return token


def parse_folder(filename="config.ini", section="folder"):
    "Считываем конфигурацию"
    parser = ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            if param[0] == "folder":
                folder = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file'.format(section, filename))
    return folder
