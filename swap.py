
def swap_case(s):
    new_s=[]
    for item in s:
        if item.isalpha():
            if item.islower():
                new_s.append(item.upper())
            else:
                new_s.append(item.lower())
        else:
            new_s.append(item)
    return ''.join(new_s)


s = "HackerRank.com presents pythonist 2."
result = swap_case(s)
print(result)