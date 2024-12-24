import datetime
import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
           s = file.readline()
           all_data.append(int(s))
           if not s:
               break



filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = datetime.datetime.now()
for i in filenames:
    read_info(i)
end_time = datetime.datetime.now()
result_time = end_time - start_time
print(f'Линейный вызов{result_time}')

if __name__ == '__main__':
    start_time2 = datetime.datetime.now()




    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end2 = datetime.datetime.now()
    time_of_multiprocessing = end2 - start_time2
    print(f'Мультипроцессный вызов : {time_of_multiprocessing}')


