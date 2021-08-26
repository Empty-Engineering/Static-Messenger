import os
import platform
import pkg_resources
def GET_DEPENDENCIES() -> None:
    required = {'requests'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed
    if missing:
        os.system("python3 -m pip install "+str(required))
def DOWNLOAD_GPG() -> None:
    import requests
    if (platform.system().lower() == 'windows'):
        file_url = 'https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.3.1.tar.bz2'
        file_object = requests.get(file_url)
        with open('gnupg-2.3.1.tar.bz2', 'wb') as local_file:
            local_file.write(file_object.content)
    elif (platform.system().lower() == 'darwin' or platform.system().lower() == 'linux'):
        file_url = 'https://releases.gpgtools.org/GPG_Suite-2021.1_105.dmg'
        file_object = requests.get(file_url)
        with open('GPG_Suite-2021.1_105.dmg', 'wb') as local_file:
            local_file.write(file_object.content)
def INSTALL_GPG() -> None:
    osName = platform.system()
    if (osName.lower() == 'windows'):
        os.system('7z gnupg-2.3.1.tar.bz2')
        os.system('cd ')
    if (osName.lower() == 'darwin' or osName.lower() == 'linux'):
        os.system('open GPG_Suite-2021.1_105.dmg')

