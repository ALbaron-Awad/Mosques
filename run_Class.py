from DB_Class import Mosques


x = Mosques()


def main():
    while True:
        print("\033[H\033[J")
        ask = int(input('\n------------------------------------------\n'
                  'أدخل رقم (1)لإضافة مسجد جديد ' 
                        '\n أدخل رقم (2) لتحديث بلاغ لمسجد'
                        '\n  أدخل رقم (3) للبحث عن  مسجد '
                        '\nأدخل رقم (4) لعرض المساجد المسجلة'
                        '\n أدخل رقم (5) لحذف مسجد      '
                        '\n\n~~~~~~~~من فضلك أدخل أختيارك~~~~~~\n\n'))
        if ask == 1:
            x.__insert__()
        elif ask == 2:
            x.__update__()
        elif ask == 3:
         x.__search__()
        elif ask == 4:
         x.__display__()
        elif ask == 5:
         x.__delete__()
    else:
        print('خطأ, الرجاء التأكد من أختيارك !')
        exit()


main()
