def groupAnagrams(strs):
    d = {}

    for word in strs:
        key = "".join(sorted(word))
        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]

    return list(d.values())