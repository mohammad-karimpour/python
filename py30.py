# دکوریتور ها
# دکوریتور ها توابعی هستند که برای اعمال تغیرات به تابعی دیگر داده میشوند 
# پوشش دهنده یک تابع - اضافه کردن قابلیت به تابع  - مانور زدن روی یک تابع


# ساختار
# باید یک تابع بسازید که یک ورودی دارد (ورودی همان فانگشننی میشود که قرار است روی آن دکوریتور اعمال شود)
# داخل تابع دکوریتور یک تابعی دیگر برای اعمال دستورات ایجاد میکنیم و همان را در آخر ریترن میکنیم
#  بهتر که ورودی های تابع داخل دکوریتور با تابع مد نظر بی نهایت قرار دهید که بتوانید برای تابع عای دیگه هم قابل استفاده باشد


# نمونه ساختار
def doc(func):
    def hash(*args,**kwargs):
        # دستورات قبل تابع مورد هدف
        values = func(*args,**kwargs)
        # دستورات بعد تابع مورد هدف
        return values
    return hash





# دکوریت کردن یک تابع

@doc
def num():
    pass


# میتوان چند دکوریتور را برای یک تابع استفاده کرد

@foo
@doc
def num():
    pass







# برای اینکه موقع تغیرات اصل فانگشن حفط شود و کپی برداری کند میتوانید از این ماژول استفاده کرد
import functools

def doc(func):
    @functools.wraps(func)
    def hash(*args,**kwargs):
        # دستورات قبل تابع مورد هدف
        values = func(*args,**kwargs)
        # دستورات بعد تابع مورد هدف
        return values
    return hash









# نمونه واقعی 
# میخواهیم قبل و بعد خروجی فانگشن از * استفاده کنیم

def star(func):
    def some(*args,**kwargs):
        print('***********')
        func()
        print('***********')
    return some

@star
def lola(g): 
    print(g)    

lola('mohammad') # ***********
                 # mohammad
                 # ***********    