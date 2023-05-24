def start_spring(**kwargs):
    last_result = ''
    work_dict = {}
    for k, v in kwargs.items():
        if v not in work_dict:
            work_dict[v] = [k]
        else:
            work_dict[v].append(k)
    temp_result = sorted(work_dict.items(), key=lambda x:(-len(x[1]), x[0]))
    for parts in temp_result:
        type, object = parts[0], parts[1]
        last_result += f'{type}:\n'
        sorted_objects = sorted(object)
        for item in sorted_objects:
            last_result += f'-{item}\n'
    return last_result




example_objects = {"Water Lilly": "flower",
        "Swifts": "bird",
        "Callery Pear": "tree",
        "Swallows": "bird",
        "Dahlia": "flower",
        "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
