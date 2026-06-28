def mutate_string(string, position, character):
    my_list=list(string)
    my_list[position]=character
    final_list=''.join(my_list)
    return final_list


s = "abracadabra"
i=5
c="k"
s_new = mutate_string(s, i, c)
print(s_new)