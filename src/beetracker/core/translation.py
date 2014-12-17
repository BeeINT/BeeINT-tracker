from modeltranslation.translator import translator, TranslationOptions
from core.models import WhatToDoSeason

class WhatToDoSeasonTranslationOptions(TranslationOptions):
    fields = ('headline', 'copy',)

translator.register(WhatToDoSeason, WhatToDoSeasonTranslationOptions)