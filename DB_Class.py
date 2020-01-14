import sqlite3


class Mosques:
    def __init__(self):
        self.db = sqlite3.connect("mosques.db")
        self.db.execute("create table if not exists mos(id integer primary key  autoincrement,"
                        "name text,Latitude  float ,longitude float ,report text ,state boolean)")
        self.db.commit()

    def __insert__(self):
        name = input("أدخل أسم المسجد:\n")
        Latitude = input("أدخل أحداثيات خطوط العرض :\n")
        longitude = input("أدخل أحداثيات خطوط الطول  :\n")
        report = input("أدخل  نص البلاغ :\n")
        state = 0
        self.db.execute("insert into mos(name, Latitude, longitude, report, state) values (?,  ?,  ?,  ?,  ?)",
                        (name, Latitude, longitude, report, state))
        self.db.commit()
        print("تم أضافة مسجد(", name, ")بنجاح")
        print("\033[H\033[J")

    def __display__(self):
        print("~~~~معلومات المساجد~~~~\n")
        conn = sqlite3.connect("mosques.db")
        cur = conn.cursor()
        info = cur.execute("select *  from mos")
        for i in info:
            print("--------------------------")
            print("رقم المسجد: ", i[0])
            print("اسم المسجد: ", i[1])
            print("أحداثيات خطوط العرض: ", i[2])
            print("أحداثيات خطوط الطول: ", i[3])
            print("البلاغ: ", i[4])
            if i[5] == 0:
             print("حالة البلاغ: لم يتم حل المشكلة\n")
            else:
                print("حالة البلاغ:تم  حل المشكلة\n")

    def __display_info__(self):
        print("~~~~~المساجد المسجلة لديك هي~~~~~\n")
        info = self.db.execute("select *  from mos")
        for i in info:
            print("--------------------------")
            print("رقم المسجد: ", i[0])
            print("اسم المسجد: ", i[1])
            print("البلاغ: ", i[4])
            if i[5] == 0:
             print("حالة البلاغ: لم يتم حل المشكلة\n")
            else:
                print("حالة البلاغ:تم  حل المشكلة\n")

    def __delete__(self):
        self.__display_info__()
        delete_id = input("أدخل رقم المسجد لكي يتم حذفه :\f")
        self.db.execute("DELETE FROM mos WHERE id=?", (delete_id,))
        self.db.commit()
        print("تم حدف مسجد رقم: ", delete_id)

    def __update__(self):
        self.__display_info__()
        conn = sqlite3.connect("mosques.db")
        cur = conn.cursor()
        update_id = input("أدخل رقم المسجد من أجل تحديث حالة البلاغ: ")
        print("\033[H\033[J")
        new_update = input("هل تم الحل المشكلة ؟")
        update_data = self.db.execute("UPDATE mos SET state = ? where id = ?", (new_update, update_id))
        self.db.commit()
        print("شكرآ لك تم تحديث حالة البلاغ!")

    def __search__(self):
        conn = sqlite3.connect("mosques.db")
        cur = conn.cursor()
        ask = input("1 البحث برقم المسجد\n"
                    " 2 البحث بحالة البلاغ \n")
        if ask == '1':
            search_id = input("أدخل رقم المسجد:\n")
            data_id = "SELECT * from mos WHERE id =?"
            info = cur.execute(data_id, (search_id,))
            info = cur.fetchall()
            for i in info:
                print("--------------------------")
                print("رقم المسجد: ", i[0])
                print("اسم المسجد: ", i[1])
                print("البلاغ: ", i[4])
                if i[5] == 0:
                    print("حالة البلاغ: لم يتم حل المشكلة\n")
                else:
                    print("حالة البلاغ:تم  حل المشكلة\n")
        elif ask == '2':
            data_id = "SELECT * from mos WHERE state =0"
            info = cur.execute(data_id)
            info = cur.fetchall()
            for i in info:
                print("---------- ----------------")
                print("رقم المسجد: ", i[0])
                print("اسم المسجد: ", i[1])
                print("البلاغ : ", i[4])
        else:
            print("خطأ,الرجاء الـتأكد من أختيارك !")
            return
