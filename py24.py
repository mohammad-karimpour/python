# حلقه (For)
# for (نماینده هر آیتم ) in (داده مد نطر)
nums = [1,2,3,4,5,6,7,8,9]

for i in nums:
    print(i*2) # 2,4,6,8,10,12,14,16,18

# حلقه تو در تو
for i in [[1,2,3,4],[5,6,7,8,9]]:
    print(i) # 1:[1,2,3,4]  2:[5,6,7,8,9]
    for l in i:
        print(l*2) # 1:[2,4,6,8]  2:[10,12,14,16,18]


# چند نماینده
for a,*b,c in nums:
    print(a,b*2,c) # 1, 4,6,8,10,12,14,16 ,9

    
    