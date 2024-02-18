def read_match_prefrences(path: str) -> dict:
    infile = open(path, 'r')
    file = infile.readlines()
    infile.close()

    match_prefrence = dict()
    match = None

    for line in file:
        data = line.strip().split(';')
        prefrence = data[1:]
        man_or_woman = data[0]
        match_prefrence[man_or_woman] = [match, prefrence] # MAHAMADOU NITPICK

    return match_prefrence
# match_prefrence = read_match_prefrences("C:/Users/Marq/Desktop/workspace/program 1/program1/women0.txt")
# print(match_prefrence)

def dict_as_str(men_or_women_dict, key = None, bool = False):
    result = ''
    for k in sorted(men_or_women_dict, key= key, reverse= bool):
        result += (f' {k} -> {men_or_women_dict[k]}\n')
    return result

def who_prefer(prefrences: list, p1: str, p2: str) -> str:
    for prefrence in prefrences:
        if prefrence in (p1, p2):
            return prefrence
# print(who_prefer(['w1', 'w2' ,'w3'], 'w2', 'w3'))

def extract_matches(men_dict: dict) -> set:
    set_of_matches = set()
    for man in men_dict:
        match = man, men_dict[man][0] 
        set_of_matches.add(match)
    return set_of_matches
# print(extract_matches(match_prefrence))

def make_match(men_dict, women_dict, trace = False) -> set:
    men_duplicate = men_dict
    unmatched = set(men_duplicate.keys())
    engaged_pairs = {}
    
    if trace == True: print(f'\nWomen Prefrences (unchanging)\n{dict_as_str(women_dict)}')

    while unmatched:
        unmatched_duplicate = unmatched.copy() #sloppy
        man = unmatched_duplicate.pop()
        prefrences = men_duplicate[man][1]


        for woman in prefrences:
            if trace == True: print(f'Men Prefrences (current)\n{dict_as_str(men_duplicate)}\nununmatched men = {unmatched}\n') #why 'if trace:' not working without '== True' 
            
            if woman not in engaged_pairs:
                engaged_pairs[woman] = man
                if trace == True: print(f'{man} proposes to {woman}, who is currently unmatched, accepting proposal\n')
                break

            else:
                engaged_man = engaged_pairs[woman]
                woman_prefrences = women_dict[woman][1]
                woman_prefers = who_prefer(woman_prefrences, engaged_man, man)

                if woman_prefers == man:
                    engaged_pairs[woman] = man
                    unmatched_duplicate.add(engaged_man)
                    men_duplicate[engaged_man][0] = None #sloppy
                    if trace == True: print(f'{man} proposes to {woman}, who is currently matched, accepting the proposal (likes new match better)\n')
                    break
                
                if trace == True: print(f'{man} proposes to {woman}, who is currently matched, rejecting the proposal (likes current match better)\n')
        
        unmatched = set(unmatched_duplicate) #sloppy
        men_duplicate[man][0] = woman #name variable
        prefrences.remove(woman)
    
    if trace == True: return f'Tracing terminated, the final matches: {extract_matches(men_duplicate)}'
    else: return f'\nThe final matches: {extract_matches(men_duplicate)}'

print(make_match(read_match_prefrences("C:/Users/Marq/Desktop/workspace/program 1/program1/men0.txt"),read_match_prefrences("C:/Users/Marq/Desktop/workspace/program 1/program1/women0.txt"), True))


# Here are example dictionaries you can use to test without needing to download file:
men_preferences = {
    
    'm2': [None, ['w3', 'w1', 'w2']],
    'm1': [None, ['w3', 'w2', 'w1']],
    'm3': [None, ['w2', 'w1', 'w3']]
}

women_preferences = {
    'w1': [None, ['m1', 'm2', 'm3']],
    'w2': [None, ['m2', 'm1', 'm3']],
    'w3': [None, ['m3', 'm2', 'm1']]
}


if __name__ == '__main__':
    men_dict_file = input('Specify the file name representing the preferences for men: ')
    women_dict_file = input('Specify the file name representing the preferences for women: ')

    men_dict = read_match_prefrences(men_dict_file)
    women_dict = read_match_prefrences(women_dict_file)

    print(f'\nMen Prefrences\n{dict_as_str(men_dict)}\n\nWomen Prefrences\n{dict_as_str(women_dict)}')

    tracing_method = input('Specify choice for tracing algorithm[True]: ')

    print(make_match(men_dict, women_dict, tracing_method))

