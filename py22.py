# متد های ریاضیات و اعداد
# برای کار با اعداد باید از کتابخانه (math) استفاده کرد

num_1 = 2
num_2 = 0.5

min(1,2,3,4,5,6,7,8,9) # 1 => کوچکترین عدد را برمیگرداند
max(1,2,3,4,5,6,7,8,9) # 9 => بزرگترین عدد را برمیگرداند
sum([1,2,3]) # 6 => [جمع تمامی آیتم ها]


num_2.as_integer_ratio() # مقیاس عدد را برمیگرداند (1-2)یعنی یک دوم

num_1.bit_count() # تعداد یک ها در باینری آن عدد را برمیگرداند




""" کتابخانه math """
import math

# عدد پی
print(math.pi())


# کوچک ترین عدد صحیح بزرگتر از عدد مدنظر را برمیگرداند
print(math.ceil(4.3)) # 5

# تبدیل منفی به مثبت و برعکس
print(math.fabs(-8)) # 8

# جزر یک عدد را برمیگرداند
print(math.sqrt(9)) # 3

# اعشار و صحیح یک عدد را از هم جدا میکند و داخل تاپلی برمیگرداند
print(math.modf(5.68)) # ((5),(68))