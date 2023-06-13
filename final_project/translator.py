from deep_translator import (GoogleTranslator)

def englishToFrench(englishText):
    frenchText = GoogleTranslator(source='en', target='fr').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    englishText = GoogleTranslator(source='fr', target='en').translate(frenchText)
    return englishText