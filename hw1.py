file_data = "sample_01.data"
sum = 0
with open (file_data, 'r') as fh: #open and read file_data
    for line in fh:
        list_s = str.split(line)  #split the data in line list
        for num in range(0, 5, 1):
            list_f = float(list_s[num]) #change the type of data into float
            sum += list_f
print(sum)
        AIzaSyAyYb-UiiNVErISC3uZf65uKG5I2hC4o9E