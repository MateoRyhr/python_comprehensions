# 2,10
def get_dict_slice(dict, range):
    dict_to_list = [(key,value) for key,value in dict.items()]
    dict_slice = {}
    for i in range:
        dict_slice[f'{dict_to_list[i][0]}'] = float(dict_to_list[i][1])
        print(dict_to_list[i][0] + ': ' + dict_to_list[i][1])
    return dict_slice

def get_country_by_key_value(data,key,key_value):
    return next(filter(lambda country : country[key] == key_value,data))