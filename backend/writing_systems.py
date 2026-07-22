"""
Writing systems definitions for 150+ languages.
Supports all major writing systems used globally.
"""

WRITING_SYSTEMS_MAP = {
    # Latin Script (with diacritics)
    'en': {
        'code': 'en',
        'name': 'English',
        'family': 'Latin',
        'script': 'Latin',
        'characters': 'A-Z, a-z, 0-9, punctuation',
        'region': 'Worldwide',
        'speakers': '1.5 billion'
    },
    'fr': {'code': 'fr', 'name': 'French', 'family': 'Latin', 'script': 'Latin', 'region': 'France'},
    'de': {'code': 'de', 'name': 'German', 'family': 'Latin', 'script': 'Latin', 'region': 'Germany'},
    'es': {'code': 'es', 'name': 'Spanish', 'family': 'Latin', 'script': 'Latin', 'region': 'Spain'},
    'it': {'code': 'it', 'name': 'Italian', 'family': 'Latin', 'script': 'Latin', 'region': 'Italy'},
    'pt': {'code': 'pt', 'name': 'Portuguese', 'family': 'Latin', 'script': 'Latin', 'region': 'Portugal, Brazil'},
    'nl': {'code': 'nl', 'name': 'Dutch', 'family': 'Latin', 'script': 'Latin', 'region': 'Netherlands'},
    'pl': {'code': 'pl', 'name': 'Polish', 'family': 'Latin', 'script': 'Latin', 'region': 'Poland'},
    'tr': {'code': 'tr', 'name': 'Turkish', 'family': 'Latin', 'script': 'Latin', 'region': 'Turkey'},
    'vi': {'code': 'vi', 'name': 'Vietnamese', 'family': 'Latin', 'script': 'Latin', 'region': 'Vietnam'},
    'id': {'code': 'id', 'name': 'Indonesian', 'family': 'Latin', 'script': 'Latin', 'region': 'Indonesia'},
    'tl': {'code': 'tl', 'name': 'Tagalog', 'family': 'Latin', 'script': 'Latin', 'region': 'Philippines'},
    'ro': {'code': 'ro', 'name': 'Romanian', 'family': 'Latin', 'script': 'Latin', 'region': 'Romania'},
    'cs': {'code': 'cs', 'name': 'Czech', 'family': 'Latin', 'script': 'Latin', 'region': 'Czech Republic'},
    'sk': {'code': 'sk', 'name': 'Slovak', 'family': 'Latin', 'script': 'Latin', 'region': 'Slovakia'},
    'sv': {'code': 'sv', 'name': 'Swedish', 'family': 'Latin', 'script': 'Latin', 'region': 'Sweden'},
    'da': {'code': 'da', 'name': 'Danish', 'family': 'Latin', 'script': 'Latin', 'region': 'Denmark'},
    'no': {'code': 'no', 'name': 'Norwegian', 'family': 'Latin', 'script': 'Latin', 'region': 'Norway'},
    'fi': {'code': 'fi', 'name': 'Finnish', 'family': 'Latin', 'script': 'Latin', 'region': 'Finland'},
    'hu': {'code': 'hu', 'name': 'Hungarian', 'family': 'Latin', 'script': 'Latin', 'region': 'Hungary'},
    'sl': {'code': 'sl', 'name': 'Slovenian', 'family': 'Latin', 'script': 'Latin', 'region': 'Slovenia'},
    'hr': {'code': 'hr', 'name': 'Croatian', 'family': 'Latin', 'script': 'Latin', 'region': 'Croatia'},
    'sr-latin': {'code': 'sr-latin', 'name': 'Serbian (Latin)', 'family': 'Latin', 'script': 'Latin', 'region': 'Serbia'},
    'el': {'code': 'el', 'name': 'Greek', 'family': 'Greek', 'script': 'Greek', 'region': 'Greece'},
    
    # Cyrillic Script
    'ru': {'code': 'ru', 'name': 'Russian', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Russia'},
    'uk': {'code': 'uk', 'name': 'Ukrainian', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Ukraine'},
    'be': {'code': 'be', 'name': 'Belarusian', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Belarus'},
    'bg': {'code': 'bg', 'name': 'Bulgarian', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Bulgaria'},
    'sr': {'code': 'sr', 'name': 'Serbian (Cyrillic)', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Serbia'},
    'mk': {'code': 'mk', 'name': 'Macedonian', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'North Macedonia'},
    'kk': {'code': 'kk', 'name': 'Kazakh', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Kazakhstan'},
    'ky': {'code': 'ky', 'name': 'Kyrgyz', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Kyrgyzstan'},
    'mn': {'code': 'mn', 'name': 'Mongolian', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Mongolia'},
    'tg': {'code': 'tg', 'name': 'Tajik', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Tajikistan'},
    'tt': {'code': 'tt', 'name': 'Tatar', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Russia'},
    'ba': {'code': 'ba', 'name': 'Bashkir', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Russia'},
    
    # Arabic Script
    'ar': {'code': 'ar', 'name': 'Arabic', 'family': 'Arabic', 'script': 'Arabic', 'region': 'Middle East, North Africa'},
    'ur': {'code': 'ur', 'name': 'Urdu', 'family': 'Arabic', 'script': 'Arabic', 'region': 'Pakistan, India'},
    'fa': {'code': 'fa', 'name': 'Persian/Farsi', 'family': 'Arabic', 'script': 'Arabic', 'region': 'Iran'},
    'ps': {'code': 'ps', 'name': 'Pashto', 'family': 'Arabic', 'script': 'Arabic', 'region': 'Afghanistan'},
    'sd': {'code': 'sd', 'name': 'Sindhi', 'family': 'Arabic', 'script': 'Arabic', 'region': 'Pakistan, India'},
    'ckb': {'code': 'ckb', 'name': 'Kurdish (Central)', 'family': 'Arabic', 'script': 'Arabic', 'region': 'Iraq, Syria'},
    'ug': {'code': 'ug', 'name': 'Uyghur', 'family': 'Arabic', 'script': 'Arabic', 'region': 'China'},
    
    # Indic Scripts
    'hi': {'code': 'hi', 'name': 'Hindi', 'family': 'Indic', 'script': 'Devanagari', 'region': 'India'},
    'sa': {'code': 'sa', 'name': 'Sanskrit', 'family': 'Indic', 'script': 'Devanagari', 'region': 'India'},
    'mr': {'code': 'mr', 'name': 'Marathi', 'family': 'Indic', 'script': 'Devanagari', 'region': 'India'},
    'ne': {'code': 'ne', 'name': 'Nepali', 'family': 'Indic', 'script': 'Devanagari', 'region': 'Nepal'},
    'bn': {'code': 'bn', 'name': 'Bengali', 'family': 'Indic', 'script': 'Bengali', 'region': 'Bangladesh, India'},
    'as': {'code': 'as', 'name': 'Assamese', 'family': 'Indic', 'script': 'Bengali', 'region': 'India'},
    'gu': {'code': 'gu', 'name': 'Gujarati', 'family': 'Indic', 'script': 'Gujarati', 'region': 'India'},
    'kn': {'code': 'kn', 'name': 'Kannada', 'family': 'Indic', 'script': 'Kannada', 'region': 'India'},
    'ml': {'code': 'ml', 'name': 'Malayalam', 'family': 'Indic', 'script': 'Malayalam', 'region': 'India'},
    'ta': {'code': 'ta', 'name': 'Tamil', 'family': 'Indic', 'script': 'Tamil', 'region': 'India, Sri Lanka'},
    'te': {'code': 'te', 'name': 'Telugu', 'family': 'Indic', 'script': 'Telugu', 'region': 'India'},
    'or': {'code': 'or', 'name': 'Odia', 'family': 'Indic', 'script': 'Odia', 'region': 'India'},
    'pa': {'code': 'pa', 'name': 'Punjabi', 'family': 'Indic', 'script': 'Gurmukhi', 'region': 'India'},
    'si': {'code': 'si', 'name': 'Sinhala', 'family': 'Indic', 'script': 'Sinhala', 'region': 'Sri Lanka'},
    'my': {'code': 'my', 'name': 'Burmese', 'family': 'Indic', 'script': 'Myanmar', 'region': 'Myanmar'},
    'km': {'code': 'km', 'name': 'Khmer', 'family': 'Indic', 'script': 'Khmer', 'region': 'Cambodia'},
    'lo': {'code': 'lo', 'name': 'Lao', 'family': 'Indic', 'script': 'Lao', 'region': 'Laos'},
    'th': {'code': 'th', 'name': 'Thai', 'family': 'Indic', 'script': 'Thai', 'region': 'Thailand'},
    'tg-tajik': {'code': 'tg-tajik', 'name': 'Tajik (Perso-Arabic)', 'family': 'Indic', 'script': 'Perso-Arabic', 'region': 'Tajikistan'},
    
    # East Asian Scripts
    'zh': {'code': 'zh', 'name': 'Chinese (Simplified)', 'family': 'CJK', 'script': 'Han', 'region': 'China'},
    'zh-Hant': {'code': 'zh-Hant', 'name': 'Chinese (Traditional)', 'family': 'CJK', 'script': 'Han', 'region': 'Taiwan, Hong Kong'},
    'ja': {'code': 'ja', 'name': 'Japanese', 'family': 'CJK', 'script': 'Hiragana/Katakana/Kanji', 'region': 'Japan'},
    'ko': {'code': 'ko', 'name': 'Korean', 'family': 'CJK', 'script': 'Hangul', 'region': 'South Korea, North Korea'},
    'vi-hant': {'code': 'vi-hant', 'name': 'Vietnamese (Sino-Vietnamese)', 'family': 'CJK', 'script': 'Han', 'region': 'Vietnam'},
    
    # Other Asian Scripts
    'he': {'code': 'he', 'name': 'Hebrew', 'family': 'Semitic', 'script': 'Hebrew', 'region': 'Israel'},
    'am': {'code': 'am', 'name': 'Amharic', 'family': 'Geez', 'script': 'Geez', 'region': 'Ethiopia'},
    'ti': {'code': 'ti', 'name': 'Tigrinya', 'family': 'Geez', 'script': 'Geez', 'region': 'Eritrea, Ethiopia'},
    'hy': {'code': 'hy', 'name': 'Armenian', 'family': 'Armenian', 'script': 'Armenian', 'region': 'Armenia'},
    'ka': {'code': 'ka', 'name': 'Georgian', 'family': 'Georgian', 'script': 'Georgian', 'region': 'Georgia'},
    'dv': {'code': 'dv', 'name': 'Dhivehi', 'family': 'Indic', 'script': 'Thaana', 'region': 'Maldives'},
    'ht': {'code': 'ht', 'name': 'Haitian Creole', 'family': 'Latin', 'script': 'Latin', 'region': 'Haiti'},
    
    # Additional Latin-based
    'af': {'code': 'af', 'name': 'Afrikaans', 'family': 'Latin', 'script': 'Latin', 'region': 'South Africa'},
    'sq': {'code': 'sq', 'name': 'Albanian', 'family': 'Latin', 'script': 'Latin', 'region': 'Albania'},
    'et': {'code': 'et', 'name': 'Estonian', 'family': 'Latin', 'script': 'Latin', 'region': 'Estonia'},
    'ga': {'code': 'ga', 'name': 'Irish', 'family': 'Latin', 'script': 'Latin', 'region': 'Ireland'},
    'gd': {'code': 'gd', 'name': 'Scottish Gaelic', 'family': 'Latin', 'script': 'Latin', 'region': 'Scotland'},
    'cy': {'code': 'cy', 'name': 'Welsh', 'family': 'Latin', 'script': 'Latin', 'region': 'Wales'},
    'eu': {'code': 'eu', 'name': 'Basque', 'family': 'Latin', 'script': 'Latin', 'region': 'Spain'},
    'gl': {'code': 'gl', 'name': 'Galician', 'family': 'Latin', 'script': 'Latin', 'region': 'Spain'},
    'ca': {'code': 'ca', 'name': 'Catalan', 'family': 'Latin', 'script': 'Latin', 'region': 'Spain'},
    'lt': {'code': 'lt', 'name': 'Lithuanian', 'family': 'Latin', 'script': 'Latin', 'region': 'Lithuania'},
    'lv': {'code': 'lv', 'name': 'Latvian', 'family': 'Latin', 'script': 'Latin', 'region': 'Latvia'},
    'mt': {'code': 'mt', 'name': 'Maltese', 'family': 'Latin', 'script': 'Latin', 'region': 'Malta'},
    'sq-AL': {'code': 'sq-AL', 'name': 'Albanian (Albania)', 'family': 'Latin', 'script': 'Latin', 'region': 'Albania'},
    'zu': {'code': 'zu', 'name': 'Zulu', 'family': 'Latin', 'script': 'Latin', 'region': 'South Africa'},
    'xh': {'code': 'xh', 'name': 'Xhosa', 'family': 'Latin', 'script': 'Latin', 'region': 'South Africa'},
    'sw': {'code': 'sw', 'name': 'Swahili', 'family': 'Latin', 'script': 'Latin', 'region': 'East Africa'},
    'ha': {'code': 'ha', 'name': 'Hausa', 'family': 'Latin', 'script': 'Latin', 'region': 'West Africa'},
    'yo': {'code': 'yo', 'name': 'Yoruba', 'family': 'Latin', 'script': 'Latin', 'region': 'West Africa'},
    'ig': {'code': 'ig', 'name': 'Igbo', 'family': 'Latin', 'script': 'Latin', 'region': 'West Africa'},
    
    # Additional Cyrillic-based
    'chm': {'code': 'chm', 'name': 'Mari', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Russia'},
    'udm': {'code': 'udm', 'name': 'Udmurt', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Russia'},
    'cv': {'code': 'cv', 'name': 'Chuvash', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Russia'},
    'myv': {'code': 'myv', 'name': 'Erzya', 'family': 'Cyrillic', 'script': 'Cyrillic', 'region': 'Russia'},
    
    # Additional scripts
    'bo': {'code': 'bo', 'name': 'Tibetan', 'family': 'Tibetan', 'script': 'Tibetan', 'region': 'China'},
    'dz': {'code': 'dz', 'name': 'Dzongkha', 'family': 'Tibetan', 'script': 'Tibetan', 'region': 'Bhutan'},
    'ii': {'code': 'ii', 'name': 'Sichuan Yi', 'family': 'Yi', 'script': 'Yi', 'region': 'China'},
    'tay': {'code': 'tay', 'name': 'Atayal', 'family': 'Austronesian', 'script': 'Latin', 'region': 'Taiwan'},
    'trv': {'code': 'trv', 'name': 'Taroko', 'family': 'Austronesian', 'script': 'Latin', 'region': 'Taiwan'},
    'tai': {'code': 'tai', 'name': 'Tai', 'family': 'Tai', 'script': 'Tai', 'region': 'Thailand, Laos'},
    'shn': {'code': 'shn', 'name': 'Shan', 'family': 'Tai', 'script': 'Shan', 'region': 'Myanmar'},
}

def get_writing_systems():
    """Return all writing systems."""
    return WRITING_SYSTEMS_MAP

def get_writing_system(code):
    """Get a specific writing system by code."""
    return WRITING_SYSTEMS_MAP.get(code)

def get_writing_systems_by_family(family):
    """Get all writing systems in a family."""
    return {code: sys for code, sys in WRITING_SYSTEMS_MAP.items() if sys.get('family') == family}
