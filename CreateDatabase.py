from Web import *
import os

def test2(identifier):
    seq = ProteinReader()
    seq.read_sequense(identifier)
    s = seq.get_sequense()

    dom = ProteinDomainReader()
    dom.read_domains(identifier)
    d = dom.get_domains()

    for st in d:
        end = d[st][0]
        d[st].append(s[st - 1:end])
    
    return d


def build_all_database(filename_orig,file_not_orig,config): #работает НЕ с 4 буквенной строкой
    #orig = open(filename_orig,"r")
    #database_orig = eval(orig.readline())
    #orig.close()

    database_orig = test2(filename_orig)


    filename_not_orig = file_not_orig.split('/')
    path_cache_not_orig = config.path_folder_cache + '\CACHE_' + filename_not_orig[-1]

    cache_not_orig = open(path_cache_not_orig,"r")

    filename_check = file_not_orig.split('/')
    path_filename_check = config.path_folder_cache + '\DICT_' + filename_check[-1]

    if os.path.exists(path_filename_check):
        dict_not_orig = open(path_filename_check,"r")
        database_not_orig = eval(dict_not_orig.readline())
        dict_not_orig.close()
        return (database_not_orig,[key for key in database_not_orig],cache_not_orig.readline())
    else:
        return build_database_not_orig(database_orig,cache_not_orig,path_filename_check)

def build_database_not_orig(origin,filename,filename_check):    
    database = {}
    arr_start = []

    string = filename.readline()
    st,end = 0,len(string)
    for key in origin:
        cache = st
        target_str = origin[key][2]
        target_len = origin[key][0] - key + 1
        target_name = origin[key][1]
        while st < end:
            if check(st,target_len,target_str,string):
                arr_start.append(st + 1)
                database[st + 1] = [st + target_len, target_name, target_str]
                st += 1
                break
            else:
                st += 1
        if st == end:
            st = cache
    f = open(filename_check,'w')
    f.write(str(database))
    f.close()
    return (database,arr_start,string)

def check(st,target_len,target_str,string):
    if st + target_len > len(string):
        return 0
    for i in range(st,st + target_len):
        if string[i] != target_str[i - st]:
            return 0
    return 1

def binary_search_right(arr,target):
    left,right = 0,len(arr)-1
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right

def write_block(st,end,index,string1,sub_str,config):
    string = ''
    for i in range(st,end):
        if sub_str != '' and i == index-1:
            string += f'{config.stop_color_text}{sub_str}({string1[i]}){config.base_color_text}'
        elif i == index-1:
            string += f'{config.stop_color_text}{string1[i]}{config.base_color_text}'
        else:
            string += string1[i]
    return string + '<br>'

def find_block_v2(database,arr_start,string,num):
    if arr_start != []:
        if num <= 0 or num > len(string):
            return (f'Номер за пределами', -1, -1)

        elif 1 <= num < arr_start[0]:
            return (f'Соединение -> {database[arr_start[0]][1]} ',0, arr_start[0] - 1)

        elif database[arr_start[-1]][0] < num <= len(string):
            return (f'{database[arr_start[-1]][1]} -> Соединение ', database[arr_start[-1]][0], len(string))

        else:
            index_st = binary_search_right(arr_start,num)
            value_st = arr_start[index_st]
            value_end = database[arr_start[index_st]][0]
            if value_st <= num <= value_end:
                return (f'{database[arr_start[index_st]][1]}', value_st - 1, value_end)
            else:
                return (f'{database[arr_start[index_st]][1]} -> Соединение -> {database[arr_start[index_st+1]][1]}',database[arr_start[index_st]][0], arr_start[index_st + 1] - 1)
    else:
        return ('Ни одного блока', 0, len(string))