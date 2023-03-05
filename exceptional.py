#from exceptional import convert
import sys

DIGIT_MAP = {
    'zerp' : '0',
    'one' :  '1',
    'two' :  '2',
}

def  convert(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
        #print(f"Convesion completada! x = {x}")
    except (KeyError, TypeError) as e:
        #print(f"Convesion fallida!")
        print(f"Convesion fallida {e!r}", file=sys.stderr)
        pass   
    return -1
    

    #print(expcls.convert("one two".split()))
