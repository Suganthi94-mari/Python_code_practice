# Step1: iterate items in outer loop
# step2: inner loop for validate next by next items
# step3: swap items

items=[23.45,12,76,34,67]
for i in range(len(items)):
    for j in range(0,len(items)-i-1):
        if items[j]>items[j+1]:
            items[j] , items[j+1] =items[j+1],items[j]
print(items)

