# متد های دیکشنری
User = {
    "name":"mohammad",
    "age": 19,
    0918:True
}

User.keys() # تمامی کلید ها

User.values() # تمامی مقدار ها

User.items() # تمامی آیتم ها(کلید و مقدار)

User.get('age') # گرفتن ولیو با کلید

User.clear() # پاک کردن تمامی آیتم ها

User.pop(0918) # آیتم مدنظر را حدف میکند - ورودی دوم مقدار جایگزین است که در صورت نبودن ارور ندهد

User.popitem() # آخرین آیتم را حذف میکند

User.setdefault('yaer') #  اگر کلید مدنظر وجود داشت آن را برمیگرداند وگرنه آن را به دیکشنری اضافه میکند

User.update({'a':'dooo'}) # اگر کلید مدنظر وجود داشت آن را آپدیت میکند درغیر اینصورت آن را به دیکشنری آضافه میکند


del User["age"] # حذف آیتمی از دیکشنری

sorted(User,reverse=False) # مرتب سازی دیکشنری - فعال کردن آن مرتب سازی را برعکس انجام میدهد

dict(one=1,tow=2) # ساخت و تبدیل به دیکشنری

len(User) # تعداد آیتم های دیکشنری


#کپی سطحی و عمیق
# برای کپی کردن کامل و قطع ارتباط با پدر جهت تغیرات روی کپی بدون تغیر پدر
User_2 = User.copy()
# اما این روش برای دیکشنری های تو در تو جواب نمی دهد و در صورت تغیر دیکشنری پدر هم تغیر میکند . برای حل آن باید از ماژول کپی استفاده کرد
import copy
User_3 = copy.deepcopy(User)


