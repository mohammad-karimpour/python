# شرط ها 
"""
if => اگر => اولین کلمه کلیدی برای شرط
elif => درغیر اینصورت اگر => شرط های ثانویه که وابسته به شرط اول هستند و تعداد آنها دلخواه است
else => در غیر این صورت => آخرین کلمخ کلیدی که بدون شرط هست و دستور آن زمانی اجرا میشود که خارج از شرط های قبلی باشد
"""
"""
سینتکس

if شرط :
    دستور
"""


if 8>2 :
    print(True)
elif 8<2 :
    print(True , "yes")
elif 8==2 :
    print(True , "no")
else:
    print(False)


# شرط های تو در تو

if 10==(3+7) :
    if 10>=4 :
        print("yes")
    else:
        print("no")
    print(True)
else:
    print(False)                     