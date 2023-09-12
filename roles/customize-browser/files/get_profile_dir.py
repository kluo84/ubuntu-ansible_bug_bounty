import os
import configparser

def get_profile_dir(profile_name):
    base_path = os.path.expanduser('~/.mozilla/firefox/')
    config = configparser.ConfigParser()
    config.read(os.path.join(base_path, 'profiles.ini'))
    
    for section in config.sections():
        if config.has_option(section, 'Name') and config.get(section, 'Name') == profile_name:
            return os.path.join(base_path, config.get(section, 'Path'))
    return None

if __name__ == "__main__":
    import sys
    profile_name = sys.argv[1]
    profile_dir = get_profile_dir(profile_name)
    if profile_dir:
        print(profile_dir)
    else:
        sys.exit(1)
