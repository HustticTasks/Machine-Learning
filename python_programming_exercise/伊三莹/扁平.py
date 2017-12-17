def flat_dict(src_dict, res_dict):
    if not isinstance(src_dict, dict):
        return
    for key in src_dict:
        # 说明: 防止第一次零时数据中多加一个.
        cur = res_dict['_']
        if not cur:
            res_dict['_'] += key
        else:
            res_dict['_'] += '.{0}'.format(key)
        # 说明: 如果当前元素不是字典则记录它
        if not isinstance(src_dict[key], dict):
            res_dict.update({res_dict['_']: src_dict[key]})
            # 说明: 既然不是字典则可能需要遍历同级元素所以需要还原到加key之前的数据
            res_dict['_'] = res_dict['_'].rstrip('.{0}'.format(key))
            continue
        # 说明: 如果当前元素依然是字典则继续递归此元素
        flat_dict(src_dict[key], res_dict)


if __name__ == '__main__':
    # 说明: _中保存零时扁平化数据
    result = {'_': ''}
    manman = {'a': {'b': {'c': 1, 'd': 2}, 'x': 2}}
    flat_dict(manman, result)
    # 说明: 处理完后pop出_零时数据
    result.pop('_')
    print(result)
