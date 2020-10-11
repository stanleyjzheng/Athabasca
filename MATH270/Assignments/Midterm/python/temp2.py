def common_letters():
    return set(word_1).intersection(word_2)

def two_set(name):
    set1 = set('jfiuuu')
    set2 = set('stanley')
    if name not in set1 & set2:
        return name
    else: 
        return 'not in set'

print(two_set('stanley'))