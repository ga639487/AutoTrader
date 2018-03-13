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
    
    buy = 0
    status = 0
    day = 0
    data = []

    f = open(args.testing, 'r')  
  
    for row in csv.reader(f):
        data.append(row[0])
        data.append(row[1])
        data.append(row[2])
        data.append(row[3])
        day+=1
    f.close()
    with open(args.output, 'w') as csv_writer:
        csv_writer.write('0')
        csv_writer.write('\n')
        for i in range(1, day-1):
            if status != 1 and data[i*4-3]+data[i*4-2] > data[i*4-1]*2:
                status+=1
                buy = data[i*4]
                csv_writer.write('1')
                csv_writer.write('\n')
            elif status != -1 and data[i*4] > buy:
                status-=1
                csv_writer.write('-1')
                csv_writer.write('\n')
            else:
                csv_writer.write('0')
                csv_writer.write('\n')
