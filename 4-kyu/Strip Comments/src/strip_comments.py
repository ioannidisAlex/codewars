def strip_comments(string, markers):
    l_list = string.split('\n')
    for marker in markers:
        l_list = [item.split(marker)[0].rstrip() for item in l_list]
    return '\n'.join(l_list)
