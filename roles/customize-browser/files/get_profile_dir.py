import os
import configparser

def get_profile_dir(profile_name):
    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~/.mozilla/firefox/profiles.ini'))
    
    for section in config.sections():
        if config.has_option(section, 'Name') and config.get(section, 'Name') == profile_name:
            return config.get(section, 'Path')
    return None

if __name__ == "__main__":
    import sys
    profile_name = sys.argv[1]
    profile_dir = get_profile_dir(profile_name)
    if profile_dir:
        print(profile_dir)
    else:
        sys.exit(1)
