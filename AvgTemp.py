lst=[]    
days = int(input('how many days in the list: '))
for i in range(days):
    temps = int(input('insert temperature: '))
    lst.append(temps)
print('list includes', days,'days:', lst)
def AvgTemp():
    total = sum(lst)
    avg = total // len(lst)
    return avg
print('Average temperature is:', AvgTemp(),'degree')
def countTemp(avg,lst):
    countTemp = 0
    for temps in lst:
        if temps >= avg:
            countTemp += 1
    return countTemp
avg = AvgTemp()
print(countTemp(avg,lst), end= ' ')
print('days above average temperature')
        




