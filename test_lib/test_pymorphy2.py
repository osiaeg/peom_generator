import pymorphy2
morph = pymorphy2.MorphAnalyzer(lang='ru')
p = morph.parse('стали')[0]
grammema = p.tag

print(morph.lat2cyr(grammema))
