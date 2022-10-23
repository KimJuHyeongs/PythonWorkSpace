class Scheduler :
    def __init__(self) :
        self.month_per_day = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        self.id = list()
        self.pw = list()
        self.check_login = False
        self.login_id = ''
        self.max_user = 5
        self.cur_user = 0
        self.max_schedule = 100
        self.cur_schedule = 0
        # id, year, month, day
        self.my_sechdule = []

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
        
        if not self.on_schedule_month(year, month) :
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
        else :
            print('=============< %4d.%4d >============='% (year, month))
            print('%5s%5s%5s%5s%5s%5s%5s'%('Sun','Mon','Tue','Wed','Thu','Fri','Sat'))
            print('=======================================')
            day_cnt = 0
            for _ in range(start_day):
                print('     ',end='')
                day_cnt += 1
            for d in range(1,day+1) :
                if self.on_schedule_day(year, month, d) > 0 :
                    print('  *',end='')
                    print('%2d'%(d),end='')
                else :
                    print('%5d'%(d), end = '')
                day_cnt += 1
                if day_cnt == 7 :
                    print()
                    day_cnt = 0
            print()
            print('=======================================')
    
    def is_enroll_num(self, tmp_id) :
        if tmp_id in self.id :
            print('동일한 아이디가 이미 존재합니다.\n 다른 아이디를 입력하세요')
            return False

        return True
    
    def enroll_num(self) :
        check_logout = False
        if self.check_login :
            check_logout = input('로그아웃 후 이용할 수 있습니다.\n로그아웃 하시겠습니까?(y/Y) : ')
            if check_logout == 'y' or check_logout == 'Y':
                self.check_login = False
            else :
                return False
        
        if self.cur_user > self.max_user :
            print('더이상 회원가입이 불가능합니다.') 
            return False
        
        tmp_id = input('생성할 아이디를 입력하세요 : ')
        if self.is_enroll_num(tmp_id) :
            self.id.append(tmp_id)
            tmp_pw = input('생성할 비밀번호를 입력하세요 : ')
            self.pw.append(tmp_pw)
            self.cur_user += 1
            return True
        else :
            return False
        
    def login_out(self) :
        if self.check_login :
            print('로그아웃 되었습니다.')
            self.check_login = False
            self.login_id = ''
            #로그아웃 성공
            return 2
        tmp_id = input('아이디를 입력하세요 : ')
        if tmp_id not in self.id :
            return 0
        tmp_pw = input('비밀번호를 입력하세요 : ')
        if tmp_pw not in self.pw :
            return 0
        
        self.login_id = tmp_id
        self.check_login = True
        #로그인 성공    
        return 1
                    
    def input_schedule(self) :
        if not self.check_login :
            print('로그인 후 이용할 수 있습니다.')
            return False
        
        if self.cur_schedule > self.max_schedule :
            print('등록 가능한 스케줄의 수를 초과했습니다.')
            return False

        s_year, s_month = map(int,input('스케줄을 등록할 날짜를 입력하세요 (ex 2015 3) : ').split())
        first_day = self.findFirstDay(s_year, s_month)
        self.disp_calendar(s_year, s_month, first_day)
        print()

        s_day = int(input('스케줄을 예약할 날짜를 입력하세요 (ex 25): '))
        self.my_sechdule.append([self.login_id, s_year, s_month, s_day])
        self.cur_schedule += 1
        return True
    
    def on_schedule_month(self, year, month) :
        for idx in range(self.cur_schedule) :
            if self.my_sechdule[idx][1] == year and self.my_sechdule[idx][2] == month :
                return True
        
        return False
    
    def on_schedule_day(self, year, month, day) :
        result = 0
        
        for idx in range(self.cur_schedule) :
            if self.my_sechdule[idx][1] == year and self.my_sechdule[idx][2] == month and self.my_sechdule[idx][3] == day :
                result += 1
        
        return result
    
    def search_schedule(self) :
        if not self.check_login :
            print('로그인 후 이용할 수 있습니다.')
            return False
        
        s_year, s_month = map(int,input('스케줄을 조회할 날짜를 입력하세요 (ex 2015 3) : ').split())
        first_day = self.findFirstDay(s_year, s_month)
        self.disp_calendar(s_year, s_month, first_day)
        print()

        s_day = int(input('스케줄을 조회할 날짜를 입력하세요 (ex 25): '))
        print('입력하신 날짜에 예약된 스케줄의 수는 %d개 입니다.'%(self.on_schedule_day(s_year, s_month, s_day)))

        return True
        