class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        
        if arrivalTime+delayedTime>=24:
            return (arrivalTime+delayedTime)-24
        else:
            return arrivalTime+delayedTime     


       
        