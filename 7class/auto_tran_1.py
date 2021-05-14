# сделать автоматический перевод фразы
# How is it going ? Just for the record ,
# Good . Take care ! No doubt .

incom = "How is it going ? Just for the record ," \
        " Good . Take care ! No doubt . "
print(incom)
dict = {
    'How': 'Как',
    'is': '',
    'it': 'это',
    'going': 'идет',
    '?': '?',
    'Just': 'просто',
    'for': 'для',
    'the': '',
    'record': 'записи',
    'Good': 'хорошо',
    'Take': 'возьми',
    'care': 'забота',
    'No': 'не',
    'doubt': 'сомневайся',
    '?': '?',
    '!': '!',
    '.': '.',
    ',':  ',',

}
for item in incom.split():
    print(dict[item])

