# accept string , extract numbers , take all possible combination of those numbers

def find_numbers(string):
    
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    string_ints = [word for word in string if word in numbers]
    
    return string_ints


def combinations(list):
    
    list = find_numbers(list)
    comb = []
    all_combinations = False
    i = 0
    
    while all_combinations == False:
        
        combinations = ''
        
        for integer in list:
            combinations += integer
                
        if combinations not in comb:
            comb.append(combinations)
            i = i + 1
            continue
        
        else:
            all_combinations = True
            print('All combinations have been found')
            
    return comb


def shuffle_numbers(list):
    fake = []
    for i in range(0, len(list)):
        list = list[:i] + list[i:]
        fake.append(list)
        
