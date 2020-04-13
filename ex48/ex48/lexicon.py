def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(sentence):
    result = []
    tag = ''
    for word in sentence.split():
        if word in ['east','west','north','south']:
            tag = 'direction'
        elif word in ['go', 'kill', 'stop','eat']:
            tag  = 'verb'
        elif word in ['door','bear','princess','cabinet']:
            tag = 'noun'
        elif word in ['the','in','of','from','at','it']:
            tag = 'stop'
        elif convert_number(word):
            word = int(word)
            tag = 'number'
        else:
            tag = 'error'
        result.append((tag, word))
    return result