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
            self.alerts[1].ledGlows = True


def calculateStats(numbers):
    if len(numbers):
        average = sum(numbers) / len(numbers)
        maximum = max(numbers)
        minimum = min(numbers)
        computedStats = {"avg": average, "max": maximum, "min": minimum}
    else:
        computedStats = {"avg": math.nan, "max": math.nan, "min": math.nan}

    return computedStats
