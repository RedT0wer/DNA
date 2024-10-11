import os

class Color:
    red = '<span style="color: red;">'
    pink = '<span style="color: #FF1493;">'
    light_blue = '<span style="color: blue;">'
    base = '<span style="color: black;">'

def build_all_database(filename_orig,file_not_orig): #работает НЕ с 4 буквенной строкой
    orig = open(filename_orig,"r")
    database_orig = eval(orig.readline())
    orig.close()

    filename_not_orig = file_not_orig.split('/')
    filename_not_orig[-1] = 'CACHE_' + filename_not_orig[-1]
    filename_not_orig = '/'.join(filename_not_orig)

    cache_not_orig = open(filename_not_orig,"r")

    filename_check = file_not_orig.split('/')
    filename_check[-1] = 'DICT_' + filename_check[-1]
    filename_check = '/'.join(filename_check)

    if os.path.exists(filename_check):
        dict_not_orig = open(filename_check,"r")
        database_not_orig = eval(dict_not_orig.readline())
        dict_not_orig.close()
        return (database_not_orig,[key for key in database_not_orig],cache_not_orig.readline())
    else:
        return build_database_not_orig(database_orig,cache_not_orig,filename_check)

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

def write_block(st,end,index,string1,sub_str):
    string = ''
    for i in range(st,end):
        if sub_str != '' and i == index-1:
            string += f'{Color.red}{sub_str}({string1[i]}){Color.base}'
        elif i == index-1:
            string += f'{Color.red}{string1[i]}{Color.base}'
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

def find_block(database,arr_start,string,num):
    try:
        if num <= 0 or num > len(string):
            print(f'Номер за пределами [1:{len(string)}]')

        elif 1 <= num < arr_start[0]:
            print(f'Соединение -> {database[arr_start[0]][1]} ')
            write_block(0, arr_start[0]-1, num, string,'')

        elif database[arr_start[-1]][0] < num <= len(string):
            print(f'{database[arr_start[-1]][1]} -> Соединение ')
            write_block(database[arr_start[-1]][0], len(string), num, string,'')

        else:
            index_st = binary_search_right(arr_start,num)
            value_st = arr_start[index_st]
            value_end = database[arr_start[index_st]][0]
            if value_st <= num <= value_end:
                if index_st > 0 and database[arr_start[index_st-1]][0] >= value_st:
                    print('Кринге ситуация!')
                    print(database[arr_start[index_st-1]][1])
                    write_block(arr_start[index_st-1]-1, database[arr_start[index_st-1]][0], num, string,'')
                    print(database[arr_start[index_st]][1])
                    write_block(value_st-1, value_end, num, string,'')
                else:
                    print(f'{database[arr_start[index_st]][1]}')
                    write_block(value_st-1, value_end, num, string,'')
            else:
                print(f'{database[arr_start[index_st]][1]} -> Соединение -> {database[arr_start[index_st+1]][1]}')
                write_block(database[arr_start[index_st]][0], arr_start[index_st+1]-1, num, string,'')
    except:
        print('Ни одного блока')