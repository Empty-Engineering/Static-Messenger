from INSTALL_GPG import *
import os
GET_DEPENDENCIES()
DOWNLOAD_GPG()
INSTALL_GPG()
def main() -> None:
    os.system('gpg --generate-full-key')
if (__name__ == '__main__'):
    main()