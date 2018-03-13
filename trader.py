# You can write code above the if-main block.

if __name__ == '__main__':
    # You should not modify this part.
    
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training_data.csv',
                       help='input training data file name')
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
    
    # The following part is an example.
    # You can modify it at will.
    
    import csv
    
    f = open('testing_data.csv', 'r')
    buy = 0
    status = 0
    day = 0
    output = []
    data = []
    for row in csv.reader(f):
        data.append(row[0])
        data.append(row[1])
        data.append(row[2])
        data.append(row[3])
        day+=1
    f.close()
    output.append(0)
    for i in range(1, day-1):
        if status != 1 and data[i*4-3]+data[i*4-2] > data[i*4-1]*2:
            status+=1
            buy = data[i*4]
            output.append(1)
        elif status != -1 and data[i*4] > buy:
            status-=1
            output.append(-1)
        else:
            output.append(0)

    print (output)
    print (len(output))
    with open('output.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(output)