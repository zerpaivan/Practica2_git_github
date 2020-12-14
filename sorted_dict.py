def sortedDict(dict):
    sorted_dict = {}
    sorted_dict = sorted_dict.fromkeys(sorted(dict.keys()))
    for i in sorted_dict:
        sorted_dict[i] = sorted(dict[i])
    return sorted_dict

if __name__ == "__main__":
    d1 = {"x":[3,2,1], "a": [-7, 5, -1], "j": [3], "d": [4,0]}
    print(sortedDict(d1))
