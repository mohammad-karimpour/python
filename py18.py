# ست ها
# ست ها ترتیب ثابتی ندارند برای همین نمیتوان با ایندکس روش کار کرد
# ست ها عناصر تکراری ندارند و قبول نمیکنند
# ست ها عناصر قابل تغیر مانند لیست و دیکشنری قبول نمیکنند
num_1 = {1,2,3,4,5,6,7,8,9}
num_2 = {4,5,6,7,24,65,80}

# کار کردن با مجموعه
print(num_1 - num_2) # بدست آوردن مخرج ست اول(آیتم هایی که در آیتم ست دوم نیستند را برمیگرداند)
print(num_1 | num_2) # اجتماع آیتم های هر دو را کنار هم قرار میدهد
print(num_1 & num_2) # اشتراک آیتم های مشترک را برمیگرداند
print(num_1 ^ num_2) # تقارن همه آیتم ها بجر آیتم های مشتر را برمی گرداند
print(num_1 < num_2) # برسی زیر مجموعه بودن