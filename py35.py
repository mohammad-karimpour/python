# خلاصه نویسی
# خلاصه کردن حلقه و شرط هایی که روی لیست و دیکشنری

# ابتدا آن چیزی را مینویسم که قراره خروجی آخر برای لیست یا دیکشنری باشد
# بعد به ترتیب مابقی دستورات را بدون : مینویسیم
# میتوان از حلقه و شرط های تودرتور هم استفاده کرد


# لیست (ست - تاپل)

num = [ s**2 for s in range(10) if s%2 == 0] # 0 , 4 , 16 , 36 , 64

for s in range(10):
    if(s%2 == 0):
        num.append(s**2) # 0 , 4 , 16 , 36 , 64



# دیکشنری

User = {ite:ite*10 for ite in range(10)}  # {1:10 , 2:20 , 3:30 , 4:40 , ...}

for ie in range(10):
    User.update({ie:ie*10}) # {1:10 , 2:20 , 3:30 , 4:40 , ...}
   