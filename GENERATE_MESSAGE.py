from INSTALL_GPG import *
import os
GET_DEPENDENCIES()
DOWNLOAD_GPG()
INSTALL_GPG()
def GENERATE_PGP_TOKEN() -> None:
    os.system('gpg --generate-full-key')
def main() -> int:
    GENERATE_PGP_TOKEN()
    fileName = input('Enter file name.\n')
    os.system('touch %s' % fileName)
if __name__ == "__main__":
    main()