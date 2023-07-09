# translator.py

"""
This module provides translation functions between English and French.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English text to French.
    """
    # Write the code here
    translator = MyMemoryTranslator(source='english india', target='french')
    translation = translator.translate(english_text)
    return translation


def french_to_english(french_text):
    """
    Translate French text to English.
    """
    # Write the code here
    translator = MyMemoryTranslator(source='french', target='english india')
    translation = translator.translate(french_text)
    return translation
