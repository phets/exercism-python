def recite(start_verse, end_verse):
    
    predicates = [
        'the house that Jack built',
        'the malt',
        'the rat',
        'the cat',
        'the dog',
        'the cow with the crumpled horn',
        'the maiden all forlorn',
        'the man all tattered and torn',
        'the priest all shaven and shorn',
        'the rooster that crowed in the morn',
        'the farmer sowing his corn',
        'the horse and the hound and the horn'
    ]
    
    verbs = [
        'lay in',
        'ate',
        'killed',
        'worried',
        'tossed',
        'milked',
        'kissed',
        'married',
        'woke',
        'kept',
        'belonged to'
    ]
    
    output = []
    
    for verse in range(start_verse - 1,end_verse):
        phrase = f'This is {predicates[verse]}'
        for inside_verse in range(verse,0,-1):
            phrase += f' that {verbs[inside_verse-1]} {predicates[inside_verse-1]}'
        phrase += '.'
        output.append(phrase)
        
    return output
