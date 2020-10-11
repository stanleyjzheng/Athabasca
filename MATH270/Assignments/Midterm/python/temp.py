def name_100_times(name):
    return name*100

def list_name_100_times(name):
    return [i for i in name*100]

l1 = [('Stanley', 16), ('Zoey', 4)]

def name_age_times(l1):
    out = []
    for name, age in l1:
        out.append(name*age)
    return out

print(name_age_times(l1))