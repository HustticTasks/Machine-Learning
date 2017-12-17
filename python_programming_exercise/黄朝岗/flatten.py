def flatten_dict(d):
    ret = dict()
    for k, v in d.items():
        if isinstance(v, dict):
            for sub_k, sub_v in flatten_dict(v).items():
                ret[k + '.' + sub_k] = sub_v
        else:
            ret[k] = v
    return ret

if __name__ == '__main__':
    print(flatten_dict({'a': {'b': {'c': 1, 'd': 2}, 'x': 2}}))
