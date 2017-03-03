def solution_three(str):
    if len(str)<2:
        return''
    return str[0:2] + str[-2:]
print(solution_three('informationsecurity'))
print(solution_three('hp'))
print(solution_three('w'))
