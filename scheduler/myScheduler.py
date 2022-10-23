class Scheduler :
    def __init__(self) :
        self.month_per_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        self.int_to_day = {0 : 'Sun', 1 : 'Mon', 2 : 'Tue', 3 : "Wed", 4 : 'Thu', 5 : 'Fri', 6 : 'Sat'}

    def checkLeapYear(self, year : int) :
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0) :
            return True
        else :
            return False

    def findFirstDay(self, year : int, month : int) :
        day = 0

        # calculate year
        for y in range(1,year) :
            if self.checkLeapYear(y) :
                day += 366
            else :
                day += 365
        
        #calculate month
        for m in range(1,month) :
            if m == 2 and self.checkLeapYear(year):
                day += 29
            else :
                day += self.month_per_day[m]
        day += 1
        
        #Find FirstDay
        return day % 7
    
    def disp_calendar(self, year : int, month : int, start_day : int) :
        day = self.month_per_day[month]
        if month == 2 and self.checkLeapYear(year) : 
            day += 1
        
        print('=============< %4d.%4d >============='% (year, month))
        print('%5s%5s%5s%5s%5s%5s%5s'%('Sun','Mon','Tue','Wed','Thu','Fri','Sat'))
        print('=======================================')
        day_cnt = 0
        for _ in range(start_day):
            print('     ',end='')
            day_cnt += 1
        for d in range(1,day+1) :
            print('%5d'%(d), end = '')
            day_cnt += 1
            if day_cnt == 7 :
                print()
                day_cnt = 0
        print()
        print('=======================================')