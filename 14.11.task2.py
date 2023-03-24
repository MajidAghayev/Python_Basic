def clean_dict_value(d,bad_val):
    d={key:val for key,val in d.items() if val != bad_val}
    return d
print(clean_dict_value({'a':5,'b':6,"c":5},5))
