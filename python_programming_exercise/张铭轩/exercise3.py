todo = {'a': {'b': {'c': 1, 'd': 2}, 'x': 2}}
flattened={}
def flatten(todo, flattenedKey=''):
    for k, v in todo.items():
        if isinstance(v, dict):
            flatten(v, flattenedKey=flattenedKey + k + '.')
        else:
            flattened[flattenedKey + k] = v


flatten(todo)
print(flattened)