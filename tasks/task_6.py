str_t: str = input('Введите строку: ')

tuple_t =  tuple(set(str_t))
len_t = len(tuple_t)


print('Уникальные символы:', tuple_t)
print('Количество уникальных символов:', len_t)