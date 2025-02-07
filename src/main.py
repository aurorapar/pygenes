import os
import logging

from gui import MainGui


def main():
    try:
        MainGui().run()

    except ModuleNotFoundError:
        print("You did not have a required package installed.")
        install_requirements_choice = input("Install required packages? y/n: ")
        if install_requirements_choice.lower().startswith("y"):
            input("After installation, rerun the program. Press enter to begin requirement installation.")
            os.system("pip3 install --upgrade pip")
            os.system("pip3 install -r requirements.txt")
        else:
            exit(126)
    except Exception as mainException:
        raise mainException


if __name__ == "__main__":
    main()
