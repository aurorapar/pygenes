import importlib
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

REQUIREMENTS_FILE = os.path.join(dir_path, '..', 'requirements.txt')

def main():
    try:
        from translations import Translator, TRANSLATION
        translator = Translator()

        with open(REQUIREMENTS_FILE) as f:
            required_imports = list(map(str.strip, f.readlines()))
        print(required_imports)
        for required_import in required_imports:
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
