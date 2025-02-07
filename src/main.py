import os
import traceback
from datetime import datetime

date_format = '%Y-%m-%d_%H-%M-%S'

current_date = datetime.now().strftime(date_format)
dir_path = os.path.dirname(os.path.realpath(__file__))

def main():
    try:
        from translations import Translator, TRANSLATION
        translator = Translator()

        from kivy.logger import Logger as Logger
        from kivy.config import Config
        Config.set('kivy', 'log_name', f'pygenes_{current_date}.log')
        Config.set('kivy', 'log_dir', os.path.join(dir_path, '..', 'logs'))
        Config.set('kivy', 'log_level', 'error')

    except ModuleNotFoundError:
        print(translator.translations[TRANSLATION.MISSING_PACKAGES_NOTIFICATION])
        install_requirements_choice = input(translator.translations[TRANSLATION.MISSING_PACKAGES_PROMPT])
        if install_requirements_choice.lower().startswith("y"):
            input(translator.translations[TRANSLATION.MISSING_PACKAGES_RERUN_NOTIFICATION])
            os.system("pip3 install --upgrade pip")
            os.system("pip3 install -r requirements.txt")
        else:
            exit(126)

    try:
        from gui import MainGui
        MainGui().run()
    except Exception as mainException:
        now = datetime.now().strftime(date_format)
        stack_trace = traceback.format_exc()
        log_message = f"{current_date} Error occurred\n{stack_trace}"
        Logger.error(log_message)
        exit(1)


if __name__ == "__main__":
    main()
