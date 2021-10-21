
def calculateStats(numbers):
  if(len(numbers)):
    avg=sum(numbers)/len(numbers)
    numbers.sort()
    max = numbers[-1]
    min = numbers[0]
  else:
    avg=0
    max=0
    min=0
  computedStats = {'avg' :avg, 'max' : max, 'min' : min}
  return computedStats
