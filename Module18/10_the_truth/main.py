input_text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shift_sym(text, key):
    new_text = ''
    for sym in text:
        if sym in LETTERS:
            num = LETTERS.find(sym)
            new_text += LETTERS[num - key]
        else:
            new_text += sym
    return new_text

def shift_letters(word, number):
    new_word = ''
    if number < len(word):
        new_word += word[-number::] + word[:-number]
    else:
        new_number = number % len(word)
        new_word += word[-new_number::] + word[:-new_number]
    return new_word

new_text = shift_sym(input_text, 1)
list_text = new_text.split()

number = 3
new_list_text = []
for word in list_text:
    if word.find('/') == -1:
        new_list_text.append(shift_letters(word, number))
    else:
        new_list_text.append(shift_letters(word, number))
        number += 1
final_text = ' '.join(new_list_text).replace('(', "'")
print('\n',final_text.replace('/', '.\n'))