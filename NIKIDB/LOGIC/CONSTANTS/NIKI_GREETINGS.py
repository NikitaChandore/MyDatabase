import shutil

from NIKIDB import Log
from .NIKI_COLORS import colors


def NIKI_HEADER():
    try:
        columns = shutil.get_terminal_size().columns
        print(colors.fg.lightgreen, colors.bold, "<< WELCOME TO NIKIDB >>".center(columns), colors.reset)
        print(colors.bold, "Designed and Developed by : NIKITA CHANDORE".center(columns), colors.reset)
        print(colors.bold, "PROJECT GUIDE : NITIN PATIL SIR\n".center(columns))
        Log.info("-" * 40)
        Log.info("\t\tWelcome to NIKIDB")
        Log.info("-" * 40)
    except Exception:
        Log.warning("Exception occured whille setting up Header.")


def NIKI_FOOTER():
    try:
        columns = shutil.get_terminal_size().columns
        print(colors.fg.darkgrey, "...Thank you for using NIKIDB...\n".center(columns))
        Log.info("-" * 40)
        Log.info("\t\tThank you for using NIKIDB")
        Log.info("-" * 40)
    except Exception:
        Log.warning("Exception occured while setting up footer.")
