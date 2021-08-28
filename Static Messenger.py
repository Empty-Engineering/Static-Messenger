from MESSENGER import *
import os
def EULA():
    userAgreement = input("Would you like to write an encrypted message? ");
    return (userAgreement.lower() == 'yes' or userAgreement.lower() == 'y');
def main():
    if EULA():
        #do something
        return 0;
if __name__ == '__main__':
    main();