# CS 303E Quiz 2C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters


# Problem 1: Separate Messages
def separateMessages(s):
    newString = ''
    characterCount = 0
    for character in s:
        newString += character
        characterCount += 1
        if characterCount == 10:
            newString += '/'
            characterCount = 0
    return newString.lower()
    
    
    pass


# Problem 2: Alarm Clock
class AlarmClock:
    def __init__(self, alarm_name, initial_time):
        self.__alarm_name = alarm_name
        self.__alarm_time = initial_time

    def isRinging(self, current_time):
        if current_time == self.__alarm_time or current_time == self.__alarm_time + 1:
            return 'Alarm is ringing'
        else:
            return 'Alarm is not ringing'

    def changeTime(self, new_time):
        if 0 <= new_time <= 23:
            self.__alarm_time = new_time

    def __str__(self):
        return self.__alarm_name, 'Alarm set for', self.__alarm_time


    pass


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.

    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # print(separateMessages("Example Sentences can be Written Here"))

    # clock = AlarmClock("Get Out of Bed", 7)
    # print(clock)
    # print(clock.isRinging(8))
    # clock.changeTime(10)
    # print(clock)


    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT