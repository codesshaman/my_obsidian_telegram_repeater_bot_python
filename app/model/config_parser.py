from configparser import ConfigParser


def parse_token(filename="config.ini", section="token"):
    "Считываем конфигурацию"
    parser = ConfigParser()
    parser.read(filename)
    token = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            token[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file'.format(section, filename))
    return token