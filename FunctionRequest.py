﻿from CreateDatabase import build_all_database,find_block_v2,write_block
from Replace3_1 import build_sequense,transform_mutation
from Web import *

def test1(identifier):
    exons = ExonReader()
    exons.read_exons(identifier)

    sequense = SequenseExonReader()
    sequense.read_sequense(identifier)
    
    arr_str = []
    arr_len = []
    ind = 0
    arr_as = exons.get_exons() 
    for i in range(len(arr_as)):
        arr_str.append(sequense.get_sequense()[ind:ind + arr_as[i]])
        ind += arr_as[i]
        arr_len.append(ind)

    t = (arr_len, arr_str, sequense.get_sequense(), sequense.get_extra()[0])
    return t

def build_array(filename):
    f = open(filename,'r')
    n,avg = map(int, f.readline().split())
    arr_len, arr_str, string = [],[],''
    for i in range(n):
        l,s = f.readline().split()
        arr_len.append(int(l))
        arr_str.append(s)
        string += s
        if i > 0:
            arr_len[i] += arr_len[i-1]
    return (arr_len, arr_str, string, avg)

def binary_search_left(arr,target):
    left,right = 0,len(arr)-1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

def read_request(request,file_req):    
    if 'del' in request:
        nums,request = request.split('del') 
    elif 'ins' in request:
        nums,request = request.split('ins') 
    elif '+' in request:
        nums,request = request.split('+') 
    elif '-' in request:
        nums,request = request.split('-')
    elif 'find' in request:
        nums,request = request.split('find')
    elif 'arg' in request:
        nums,request = request.split('arg')

    #arr_len, arr_str, string, avg = build_array(file_req)
    arr_len, arr_str, string, avg = test1(file_req)

    num,len_num = nums,1
    if '_' in nums:
        nums = nums.split('_')
        num = int(nums[0])
        len_num = int(nums[1]) - int(nums[0]) + 1
    else: 
        num = int(nums)

    return (arr_len, arr_str, string, num, len_num, avg, request)

def calcul_mod(index,arr_len,avg):
    i_st = binary_search_left(arr_len,avg)
    if index == i_st:
        if i_st > 0:
            return avg - arr_len[i_st-1]
        else:
            return arr_len[i_st] - avg
    else:
        if (arr_len[index-1] - avg - 1)%3 == 2:     #в прошлом Экзоне тройка закончилась
            return 0 
        elif (arr_len[index-1] - avg - 1)%3 == 1:   #в прошлом Экзоне тройке не хватило одной буквы
            return 1
        else:                                       #в прошлом Экзоне тройке не хватило двух букв
            return 2 

def calcul_mod_v2(index,arr_len,avg):
    i_st = binary_search_left(arr_len,avg)
    if index == i_st:
        if (arr_len[index] - avg - 1)%3 == 2: 
            return 0 
        elif (arr_len[index] - avg - 1)%3 == 1: 
            return 1
        else:
            return 2
    else:
        if (arr_len[index-1] - avg - 1)%3 == 2:     #в прошлом Экзоне тройка закончилась
            return 0 
        elif (arr_len[index-1] - avg - 1)%3 == 1:   #в прошлом Экзоне тройке не хватило одной буквы
            return 1
        else:                                       #в прошлом Экзоне тройке не хватило двух букв
            return 2 

def calcul_index_letter(index,index_letter,arr_len):
    if index > 0:
        return index_letter - arr_len[index-1]
    else:
        return index_letter

def build_string(string,index_letter,len_letter,let):
    letter = ''
    for i in range(index_letter,index_letter + len_letter):
        letter += string[i]
    return (string[:index_letter] + let + string[index_letter+len_letter:],letter)

def build_string_v2(arr_str,index,arr_len,avg):
    i_st = binary_search_left(arr_len,avg)
    if index == i_st: #первый
        return arr_str[index + 1]
    elif index == len(arr_str)-1: #последний
        return arr_str[index - 1]
    else:
        return arr_str[index - 1] + arr_str[index + 1]

def find_stop(mod,index,arr_str,string):
    end = index
    d = set(['TGA','TAG','TAA'])
    while end <= len(arr_str) - 1:
        if index != end:
            if border_check(string,mod - 3,d):
                return (string,end,mod - 3)
        
        i,j = mod,len(string)-2
        while i < j:            
            word = string[i] + string[i + 1] + string[i + 2]
            if word in d:
                return (string,end,i)
            i += 3

        if end + 1 <= len(arr_str) - 1:
            end += 1
            string += arr_str[end]
            mod = i + 3
        else:
            break

    return (string,end,-1)

def border_check(string,index,d):
    return string[index] + string[index + 1] + string[index + 2] in d

def output_exon(index_letter,letter,index_stop,string1,curr,config):
    string = ''
    for i in range(len(string1)):
        if not curr:
            if i == index_letter:
                string += config.stop_color_text + letter + config.base_color_text
            if i == index_stop:
                string += config.find_color_text
            if i == index_stop + 3:
                string += config.base_color_text
        elif curr == -2:
            if i == index_letter:
                string += config.stop_color_text + letter + '('
            if i == index_letter + 1:
                string += ')' + config.base_color_text
            if i == index_stop:
                string += config.find_color_text
            if i == index_stop + 3:
                string += config.base_color_text
        else:
            if i == index_letter:
                string += config.stop_color_text
            elif i == index_letter + curr:
                string += config.base_color_text
            if i == index_stop:
                string += config.find_color_text
            elif i == index_stop + 3:
                string += config.base_color_text
        string += string1[i]
    return string

def transform_bef_string(string,avg,*args):
    if args[0] == 'del':
        return string[avg:args[1] + avg - 1] + string[args[1] + avg + args[2] - 1:]
    elif args[0] == 'find':
        return string[avg:]
    elif args[0] == 'ins':
        return string[avg:args[1] + avg - 1] + args[3] + string[args[1] + avg + args[2] - 1:]
    elif args[0] == 'arg':
        return string[avg:args[1] + avg - 1] + args[3] + string[args[1] + avg + args[2] - 1:]
    elif args[0] == '-':
        return string[avg:args[1]] + string[args[2]:]

def output_block(obj1,st1,end1,obj2,config):
    string = ''
    for i in range(0,min([len(obj1),len(obj2)])):
        if obj1[st1 + i] != obj2[i]:
            break

    ind = i
    for i in range(st1,ind + st1):
        string += obj1[i]
    string += config.stop_color_text
    for i in range(ind + st1,end1):
        string += obj1[i]

    string += config.base_color_text
    string += '<br>'

    for i in range(0,ind):
        string += obj2[i]
    string += config.difference_color_text
    for i in range(ind,len(obj2)):
        string += obj2[i]
    string += config.base_color_text
    return string + '<br>'


def one(request,file_orig,file_req,config):
    arr_len, arr_str, bef_string, num, len_num, avg, request = read_request(request,file_req)

    build_sequense(file_req,bef_string,avg,config)    

    index_target_str_in_arr_str = binary_search_left(arr_len,num + avg) #индекс целевого Экзона в массиве arr_str
    index_num_in_target_str = calcul_index_letter(index_target_str_in_arr_str,num - 1 + avg,arr_len) #индекс искомого номера/начала диапазона в целевом Экзоне строке

    target_str,letter = build_string(arr_str[index_target_str_in_arr_str],index_num_in_target_str,0,'') #целевой Экзон и строка из удаляемых символов(если удаляли)

    # обернуть асинхронно
    database,arr_start,aft_string = build_all_database(file_orig,file_req,config)
    num_for_arr_start = (num - 1) // 3
    name_block,st1,end1 = find_block_v2(database,arr_start,aft_string,num_for_arr_start + 1) 
    #

    bef_string = transform_bef_string(bef_string,avg,'find')
    mutation_string = transform_mutation(st1 * 3, bef_string)

    string = name_block + '<br>'
    string += write_block(0,end1 - st1,num_for_arr_start + 1 - st1,mutation_string,'',config)
    if name_block != 'Номер за пределами':
        string += f"Экзон: {index_target_str_in_arr_str + 1}<br>"
        string += output_exon(index_num_in_target_str,letter,-1,target_str,1,config)
    return string

def two(request,file_orig,file_req,config):
    arr_len, arr_str, bef_string, num, len_num, avg, request = read_request(request,file_req)
    build_sequense(file_req,bef_string,avg,config)

    index_target_str_in_arr_str = binary_search_left(arr_len,num + avg) #индекс целевого Экзона в массиве arr_str
    mod = calcul_mod(index_target_str_in_arr_str,arr_len,avg) #лишние элементы в начале строки
    index_num_in_target_str = calcul_index_letter(index_target_str_in_arr_str,num - 1 + avg,arr_len) #индекс искомого номера/начала диапазона в целевом Экзоне строке
    
    target_str,letter = build_string(arr_str[index_target_str_in_arr_str],index_num_in_target_str,len_num,'') #целевой Экзон и строка из удаляемых символов(если удаляли)
    target_str,end,index_stop = find_stop(mod,index_target_str_in_arr_str,arr_str,target_str) 

    database,arr_start,aft_string = build_all_database(file_orig,file_req,config)
    num_for_arr_start = (num - 1) // 3
    name_block,st1,end1 = find_block_v2(database,arr_start,aft_string,num_for_arr_start + 1) 
    
    bef_string = transform_bef_string(bef_string,avg,'del',num,len_num)
    mutation_string = transform_mutation(st1 * 3, bef_string)    

    string = name_block + '<br>'
    string += output_block(aft_string,st1,end1,mutation_string,config)

    if index_stop == -1:
        string += f"Экзон: {index_target_str_in_arr_str + 1}<br>Конца нет<br>"
    else:
        string += f"Экзон: {index_target_str_in_arr_str + 1}<br>Стоп в: {end + 1}<br>"

    string += output_exon(index_num_in_target_str,letter,index_stop,target_str,0,config)
    return string

def three(request,file_orig,file_req,config):
    arr_len, arr_str, bef_string, num, len_num, avg, request = read_request(request,file_req)
    build_sequense(file_req,bef_string,avg,config)

    index_target_str_in_arr_str = binary_search_left(arr_len,num + avg) #индекс целевого Экзона в массиве arr_str
    mod = calcul_mod_v2(index_target_str_in_arr_str,arr_len,avg) #лишние элементы в начале строки
    
    target_str = build_string_v2(arr_str,index_target_str_in_arr_str,arr_len,avg) #целевой Экзон и строка из удаляемых символов(если удаляли)
    target_str,end,index_stop = find_stop(mod,index_target_str_in_arr_str + 1,arr_str,target_str) 

    database,arr_start,aft_string = build_all_database(file_orig,file_req,config)
    num_for_arr_start = (arr_len[max(index_target_str_in_arr_str - 1,0)] + mod - 1 - avg) // 3 
    name_block,st1,end1 = find_block_v2(database,arr_start,aft_string,num_for_arr_start + 1) 
    
    bef_string = transform_bef_string(bef_string,avg,'-',arr_len[index_target_str_in_arr_str - 1],arr_len[index_target_str_in_arr_str]) #дописать условия для границ
    mutation_string = transform_mutation(st1 * 3, bef_string)    

    string = name_block + '<br>'
    string += output_block(aft_string,st1,end1,mutation_string,config)

    if index_stop == -1:
        string += f"Удален Экзон: {index_target_str_in_arr_str + 1}<br>Конца нет<br>"
    else:
        string += f"Удален Экзон: {index_target_str_in_arr_str + 1}<br>Стоп в: {end + 1}<br>"

    string += output_exon(-1,'',index_stop,target_str,0,config)
    return string

def four(request,file_orig,file_req,config):
    arr_len, arr_str, bef_string, num, len_num, avg, request = read_request(request,file_req)
    build_sequense(file_req,bef_string,avg,config)

    index_target_str_in_arr_str = binary_search_left(arr_len,num + avg) #индекс целевого Экзона в массиве arr_str
    mod = calcul_mod(index_target_str_in_arr_str,arr_len,avg) #лишние элементы в начале строки
    index_num_in_target_str = calcul_index_letter(index_target_str_in_arr_str,num - 1 + avg,arr_len) #индекс искомого номера/начала диапазона в целевом Экзоне строке
    
    target_str,letter = build_string(arr_str[index_target_str_in_arr_str],index_num_in_target_str + 1,0,request) #целевой Экзон и строка из удаляемых символов(если удаляли)
    target_str,end,index_stop = find_stop(mod,index_target_str_in_arr_str,arr_str,target_str) 

    database,arr_start,aft_string = build_all_database(file_orig,file_req,config)
    num_for_arr_start = (num - 1) // 3
    name_block,st1,end1 = find_block_v2(database,arr_start,aft_string,num_for_arr_start + 1) 
    
    bef_string = transform_bef_string(bef_string,avg,'ins',num + 1,0,request)
    mutation_string = transform_mutation(st1 * 3, bef_string)    

    string = name_block + '<br>'
    string += output_block(aft_string,st1,end1,mutation_string,config)

    if index_stop == -1:
        string += f"Экзон: {index_target_str_in_arr_str + 1}<br>Конца нет<br>"
    else:
        string += f"Экзон: {index_target_str_in_arr_str + 1}<br>Стоп в: {end + 1}<br>"

    string += output_exon(index_num_in_target_str + 1,'',index_stop,target_str,len(request),config)
    return string

def five(request,file_orig,file_req,config):
    arr_len, arr_str, bef_string, num, len_num, avg, request = read_request(request,file_req)
    build_sequense(file_req,bef_string,avg,config)

    index_target_str_in_arr_str = binary_search_left(arr_len,num + avg) #индекс целевого Экзона в массиве arr_str
    index_num_in_target_str = calcul_index_letter(index_target_str_in_arr_str,num - 1 + avg,arr_len) #индекс искомого номера/начала диапазона в целевом Экзоне строке
    
    target_str,letter = build_string(arr_str[index_target_str_in_arr_str],index_num_in_target_str,len_num,request) #целевой Экзон и строка из удаляемых символов(если удаляли)

    database,arr_start,aft_string = build_all_database(file_orig,file_req,config)
    num_for_arr_start = (num - 1) // 3
    name_block,st1,end1 = find_block_v2(database,arr_start,aft_string,num_for_arr_start + 1) 
    
    bef_string = transform_bef_string(bef_string,avg,'arg',num,len_num,request)
    mutation_string = transform_mutation(st1 * 3, bef_string)    

    string = name_block + '<br>'
    string += write_block(0,min(len(mutation_string),end1 - st1),num_for_arr_start + 1 - st1,mutation_string, aft_string[num_for_arr_start],config)

    string += f"Экзон: {index_target_str_in_arr_str + 1}<br>"

    string += output_exon(index_num_in_target_str,letter,-1,target_str,-2,config)
    return string

def func_request(request,orig,file_req, config):
    if 'find' in request:
        return one(request,orig,file_req,config)

    elif 'del' in request:
        return two(request,orig,file_req,config)

    elif '+' in request or '-' in request:
        return three(request,orig,file_req,config)

    elif 'ins' in request:
        return four(request,orig,file_req,config)

    elif 'arg' in request:
        return five(request,orig,file_req,config)