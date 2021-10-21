import math

class EmailAlert:
    def __init__(self):
        self.emailSent = False


class LEDAlert:
    def __init__(self):
        self.ledGlows = False


class StatsAlerter:
    def __init__(self, maxThreshold, alerts):
        self.maxThreshold = maxThreshold
        self.alerts = alerts

    def checkAndAlert(self, numbers):
        computedStats = calculateStats(numbers)

        if computedStats["max"] > self.maxThreshold:
            self.alerts[0].emailSent = True
            self.alerts[0].ledGlows = True


def calculateStats(numbers):
    if len(numbers):
        avgNum = sum(numbers) / len(numbers)
        maxNum = max(numbers)
        minNum = min(numbers)
    else:
        avgNum=math.nan
        maxNum=math.nan
        minNum=math.nan
    computedStats = {"avg": avgNum, "max": maxNum, "min": minNum}

    return computedStats
