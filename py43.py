""" سطح دسترسی در کلاس """

# برای اینکه ما به برنامه نویس بگوییم که یکسری داده خصوصصی و یا قفل هستند از یکسری قرارداد استفاده میکنیم

class Data:
    def __init__(self,id,name,password,car) -> None:
        self._id = id # => یعنی خصوصی است(پروتیکتد) و فقط داخل کلاس و کلاس های فرزند قابل استفاده است

        self.name = name # => روش دیفال که آزاد است(پابلیک)

        self.__pasworad = password  # => یعنی داده قفل است(پرایوت)و فقط داخل کلاس قابل دسترسی میباشد

        self.__car__ = car  # برای دیتا هایی که کاربرد خاصی دارند




# این موارد فقط هشدار هستند و مانع استفاده به طور کامل نمیشوند
# اما اگر میخواهی از قانون سرپیچی کنی و ازشان استفاده کنی برای داده های پرایوت ارور میدهد
# براید از این روش برای دسترسی بهش استفاده کرد

print(_Data.__password) # _اسم کلاس __ داده قفل شده