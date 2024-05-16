import sys

from modules.check_clipboard import check_clipboard
from modules.detectTargetActiveWIndow import getActiveWindowTitle
def main():

    bufWindowTitle = ""

    try:

        while True:

            activeWindowTitle = getActiveWindowTitle()

            if bufWindowTitle != activeWindowTitle:

                check_clipboard(activeWindowTitle)

                bufWindowTitle = activeWindowTitle

    except KeyboardInterrupt:

        sys.exit(0)



if __name__ == '__main__':

    main()