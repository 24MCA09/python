

class Time:
    def __init__(self, hour, minu, sec):
        self.hour = hour
        self.minu = minu
        self.sec = sec

    def sum(self, other):
        stotal = self.sec + other.sec
        mtotal = self.minu + other.minu + stotal // 60
        htotal = self.hour + other.hour + mtotal // 60
        stotal %= 60
        mtotal %= 60
        htotal %= 24  # To ensure hours are in a 24-hour format
        return Time(htotal, mtotal, stotal)

    def __add__(self, other):
        return self.sum(other)


# Input times in HH:MM:SS format
h, m, s = map(int, input("Enter time 1 (HH:MM:SS): ").split(":"))
t1 = Time(h, m, s)

h, m, s = map(int, input("Enter time 2 (HH:MM:SS): ").split(":"))
t2 = Time(h, m, s)

# Adding the two times
t3 = t1 + t2

# Displaying the total time
print("Total time = ", t3.hour, ":", t3.minu, ":", t3.sec)

