

def find_numbers(string):
    
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    string_ints = [word for word in string if word in numbers]
    
    return string_ints


def permutation(wilson):
    
    list_of_numbers = find_numbers(wilson)
  
    if len(list_of_numbers) == 0:
        print('There are no combinations')
        return None
    
    if len(list_of_numbers) == 1: 
        return [list_of_numbers] 
  
    combinations = [] 
  
    for i in range(len(list_of_numbers)):
        
        first_part = list_of_numbers[i]
        remainder_list = list_of_numbers[:i] + list_of_numbers[i+1:]
        
        ## reocurrance
        for p in permutation(remainder_list):
            combinations.append([first_part] + p) 
    
    return combinations


x = 'HELLO WILL 3 5'

perms = permutation(x)
print(perms)
