file_data = "sample_01.data"
sum = 0
with open (file_data, 'r') as fh:
    for line in fh:
        list_s = str.split(line)
        for num in range(0, 5, 1):
            list_f = float(list_s[num])
            sum += list_f
print(sum)
        