#(B,C,D) 5ta float o'zgaruvchilar, qiymati va turini chiqarish
flaot_list = [10.2,20.5,30.8,40.9,50.1]
def display_type_and_value(list):
    for i in list:
        print(i, type(i))

display_type_and_value(flaot_list)

#(E,F) 2ta o'nlik son kiritish va ular bilam matematika amallarini bajarish
def float_raqamlari(flt1, flt2):
    return f"Summa: {flt1 + flt2}, " \
           f"Ayirma: {flt1 - flt2}, " \
           f"Ko'paytma: {flt1 * flt2}, " \
           f"Bo'linma: {flt1 / flt2}"
           
result = float_raqamlari(10.5, 5.2)
print(result)
