import importlib
import os
import sys

from constants import REQUIREMENTS_FILE

def main():

    from translations import Translator, TRANSLATION
    translator = Translator()

    with open(REQUIREMENTS_FILE) as f:
        required_imports = list(map(str.strip, f.readlines()))

    for required_import in required_imports:
        try:
            importlib.import_module(required_import)

        except ModuleNotFoundError as import_error:
            if "'winreg'" in str(import_error) and sys.platform != 'windows':
                pass
            else:
                print(import_error)
                print(translator.translations[TRANSLATION.MISSING_PACKAGES_NOTIFICATION])
                install_requirements_choice = input(translator.translations[TRANSLATION.MISSING_PACKAGES_PROMPT])
                if install_requirements_choice.lower().startswith("y"):
                    os.system("pip3 install --upgrade pip")
                    os.system(f"pip3 install -r {REQUIREMENTS_FILE}")
                else:
                    exit(126)

    from logger import Logger
    exception_logger = Logger()

    try:
        from gui import MainGui
        MainGui().run()
    except Exception as mainException:
        exception_logger.error(mainException)
        from gui.popup import show_popup
        show_popup(translator.translations[TRANSLATION.ERROR_TITLE], translator.translations[TRANSLATION.ERROR_OCCURRED])

if __name__ == "__main__":
    main()
