"""
This module contains functions for translating text
 between English and French using MyMemoryTranslator.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates the given English text to French using MyMemoryTranslator.

    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates the given French text to English using MyMemoryTranslator.

    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text

