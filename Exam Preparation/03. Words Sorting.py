def words_sorting(*args):
    result = ''
    work_dict = dict()
    for pieces in args:
        total = 0
        for word in pieces:
            total += ord(word)
        if pieces not in work_dict:
            work_dict[pieces] = total
    dic_count = sum(work_dict.values())
    if dic_count % 2 == 1:
        for k, v in sorted(work_dict.items(),key=lambda x:x[1],reverse=True):
            result += f"{k} - {v}\n"
    else:
        for k, v in sorted(work_dict.items()):
            result += f"{k} - {v}\n"
    return result




print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
