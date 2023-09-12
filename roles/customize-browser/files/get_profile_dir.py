import configparser
import sys

def get_profile_dir(profile_name):
    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~/.mozilla/firefox/profiles.ini'))
    
    for section in config.sections():
        if config.has_option(section, 'Name') and config[section]['Name'] == profile_name:
            return config[section]['Path']
    return None

if __name__ == "__main__":
    profile_name = sys.argv[1]
    profile_dir = get_profile_dir(profile_name)
    if profile_dir:
        print(profile_dir)
    else:
        print(f"No directory found for profile: {profile_name}")
