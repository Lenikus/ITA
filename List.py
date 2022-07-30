def is_list_in_list(what, where):
    res = -1;
    sl = len(where)
    ssl = len(what)
    i = 0
    while i < sl - ssl + 1:
        j = 0
        while j < ssl:
            if what[j] != where[i + j]:
                break
            else:
                if j == ssl - 1:
                    res = i
            j = j + 1
        i = i + 1
    return res


def list_replace(where, pos, what, by_what):
    # pos = where.index(what)
    for item in what:
        where.remove(item)
    for item in by_what:
        where.insert(pos, item)
        pos = pos + 1
