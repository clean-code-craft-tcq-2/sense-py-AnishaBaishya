class EmailAlert:
  def _init_(self):
    self.emailSent = False
    
class LEDAlert:
  def _init_(self):
    self.ledGlows = False
    
class StatsAlerter:
  def _init_(self,maxThreshold,alerts):
    self.maxThreshold = maxThreshold
    self.alerts = alerts
  
  def checkAndAlert(self,numbers):
    computedStats = calculateStats(numbers)
    
    if computedStats["max"] > self.maxThreshold:
      self.alerts[0].emailSent = True
      self.alerts[1].ledGlows = True
      
      
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
