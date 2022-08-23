import json
from pathlib import Path
import subprocess

beginning_warning = """Welcome! It appears this is the first time you are running Steam Deck Tweaks.

This is a program designed to aid in the process of installing some popular
tweaks and programs onto your Steam Deck. These include a VNC server for
controlling your Steam Deck from your PC, Helping with the install of
EmuDeck, and a few other things that I made thrown in.

### IMPORTANT ###
This program modifies files in the root of the Steam Deck that were not
designed to be modified. These are all within the bound of a regular Linux
operating system, however the Steam Deck is specialized, and installing some
of these could cause system instability or possibly corrupt the operating
system. I am not responsible for any damage that you may cause to your
Steam Deck opearting system by using my program. If you do find yourself
with a broken/bricked Steam Deck, Valve has instructions on how to restore
a factory image and get yourself back up and running here:

https://help.steampowered.com/en/faqs/view/1B71-EDF2-EB6D-2BB3"""


class Menu:
    class Item:
        def __init__(self, text, action):
            self.text = 0

    def __init__(self):
        self.items = 0


def first_time_setup():
    print('#----------------------------# Steam Deck Tweaks #----------------------------#\n')
    print(beginning_warning)
    confirmation = input('Do you accept the risks of using Steam Deck Tweaks and wish to continue? [Y/N]: ').lower()
    while confirmation != 'y':
        if confirmation == 'n':
            print('Exiting...')
            exit(1)
        else:
            print('Please input a "Y" or an "N".')
            confirmation = input('Do you wish to continue? [Y/N]: ').lower()


def main():
    print('#----------------------------# Steam Deck Tweaks #----------------------------#\n')
    script_path = Path(__file__).absolute()
    home_dir = str(Path.home())
    config_path = home_dir + '/.config/steamdeck-tweaks.json'
    config_data = {
        'read_only': 'enabled'
    }
    try:
        readonly_status = subprocess.check_output('sudo steamdeck-readonly status', shell=True, stderr=subprocess.STDOUT).wait()
    except subprocess.CalledProcessError as e:
        readonly_status = str(e.output)

    if readonly_status == 'b\'enabled\\n\'':
        read_only = True
    elif readonly_status == 'b\'disabled\\n\'':
        read_only = False
    else:
        read_only = None

    try:
        with open(config_path, 'r') as file:
            config_data = json.load(file)
    except FileNotFoundError:
        first_time_setup()
        with open(config_path, 'w') as outfile:
            outfile.write(json.dumps(config_data))

    if config_data['read_only'] == 'enabled':
        pass
