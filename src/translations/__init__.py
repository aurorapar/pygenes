import platform
import locale
import importlib
import sys

from enum import auto, Enum

if 'kivy' in sys.modules:
    from gui.popup import show_popup


class TRANSLATION(Enum):
    TITLE = auto()
    MISSING_TRANSLATION = auto()
    MISSING_TRANSLATION_TITLE = auto()
    MISSING_PACKAGES_NOTIFICATION = auto()
    MISSING_PACKAGES_PROMPT = auto()
    # MISSING_PACKAGES_RERUN_NOTIFICATION = auto()
    FILE_MENU_BUTTON = auto()
    FILE_NEW = auto()
    FILE_OPEN = auto()
    FILE_SAVE = auto()
    FILE_CLOSE = auto()
    HELP_MENU_BUTTON = auto()
    ABOUT = auto()
    ABOUT_SECTION = auto()
    ERROR_TITLE = auto()
    ERROR_OCCURRED = auto()
    NEW_FAMILY_LINE = auto()
    NO_SAVE_DATA = auto()
    ENTER_FILE_NAME = auto()
    CANCEL = auto()

class Translator:

    def __init__(self):
        self.translations = self.get_user_language_translations()
        import translations.en_US as english_translations
        english_translations = english_translations.definitions

        required_definitions = [definition.name for definition in TRANSLATION]
        missing_definitions = [x for x in required_definitions if x not in self.translations.keys()]
        if len(missing_definitions):

            if 'MISSING_TRANSLATION_TITLE' in self.translations.keys():
                error_title = self.translations['MISSING_TRANSLATION_TITLE']
            else:
                error_title = english_translations ['MISSING_TRANSLATION_TITLE']

            if 'MISSING_TRANSLATION' in self.translations.keys():
                error_message = self.translations['MISSING_TRANSLATION']
            else:
                error_message = english_translations['MISSING_TRANSLATION']

            error_message = error_message.format(', '.join(missing_definitions))

            raise RuntimeError(error_message)

        # this is so we can do the following:
        '''
            translator = Translator()
            translator.get_translation(TRANSLATION.TITLE) 
        '''
        additions = {}
        for translated_item in self.translations.keys():
            for translation in TRANSLATION:
                if translation.name == translated_item:
                    additions[translation] = self.translations[translated_item]
        for k,v in additions.items():
            self.translations[k] = v

    def get_user_language_translations(self):
        user_language = locale.getlocale()[0]
        try:
            user_language_module = importlib.import_module('translations.' + user_language)
            return user_language_module.definitions
        except ImportError as importError:
            print(importError)
            from translations import en_US

            error_message = f"Apologies, there is no translation for {user_language}.\n"
            error_message += "\nDefaulting to [b]en_US[/b] as the author is only fluent in this language.\n"
            error_message += "\nYou can help translate by visiting: http://github.com/aurpar/pygenes"
            error_title = "Translation Error"

            if 'kivy' in sys.modules:
                show_popup(error_title, error_message)

            return en_US.definitions


