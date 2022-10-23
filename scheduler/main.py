from myScheduler import Scheduler

if __name__ == '__main__' :
    year, month = map(int, input('일정을 확인하고 싶은 년도와 월을 입력하세요. (ex 2015 3) : ').split())
    
    scheduler = Scheduler()
    first_day = scheduler.findFirstDay(year, month)
    
    scheduler.disp_calendar(year, month, first_day)