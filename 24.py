file_data = 'sample_02.data.txt'
sum = 0
x=0
with open (file_data, 'r') as fh:
    for a in fh:
        sum+=float(a)
        x+=1
print(sum/x)