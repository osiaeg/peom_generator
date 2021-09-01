import pymorphy2
morph = pymorphy2.MorphAnalyzer(lang='ru')

def translate_tag(tag : str) -> str:
    try:
        out = morph.lat2cyr(tag)
    except AttributeError:
        return None
    return out


def get_word_info(word: str) -> dict:
    p = morph.parse(word)[0]
    out_dict = {
            'Часть речи' : translate_tag(p.tag.POS),
            'Одушевленность': translate_tag(p.tag.animacy),
            'Вид' : translate_tag(p.tag.aspect),
            'Падеж' : translate_tag(p.tag.case),
            'Род' : translate_tag(p.tag.gender),
            'Включенность говорящего в действие' : translate_tag(p.tag.involvement),
            'Наклонение' : translate_tag(p.tag.mood),
            'Число' : translate_tag(p.tag.number),
            'Лицо' : translate_tag(p.tag.person),
            'Время' : translate_tag(p.tag.tense),
            'Переходность' : translate_tag(p.tag.transitivity),
            'Залог' : translate_tag(p.tag.voice),
            'Начальная форма' : p.normal_form
            }
    return out_dict
