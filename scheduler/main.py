from myScheduler import Scheduler

if __name__ == '__main__' :
    # year, month = map(int, input('일정을 확인하고 싶은 년도와 월을 입력하세요. (ex 2015 3) : ').split())
    scheduler = Scheduler()
    
    while True :
        print('====[ 회의실 예약 시스템 ]=====')
        print('1. 사번 등록/삭제')
        print('2. 로그인/로그아웃')
        print('3. 회의실 예약')
        print('4. 회의실 예약 상태 조회')
        print('0. 종료')
        print('===========================')
        menu = int(input('> 번호 선택 : '))
        if menu == 0 :
            break
        elif menu == 1 :
            check_enroll = scheduler.enroll_num()
            if check_enroll :
                print('회원가입에 성공했습니다.')
            else :
                print('회원가입에 실패했습니다.')
        elif menu == 2 :
            check_login_out = scheduler.login_out()
            if check_login_out == 1 :
                print('로그인에 성공했습니다.')
            elif check_login_out == 2:
                print('로그아웃에 성공했습니다.')
            else :
                print('로그인/로그아웃에 실패했습니다.')
        elif menu == 3 :
            check_reservation = scheduler.input_schedule()
            if check_reservation :
                print('회의실 예약에 성공했습니다.')
            else :
                print('회의실 예약에 실패했습니다.')
        elif menu == 4 :
            check_search = scheduler.search_schedule()
            if check_search :
                print('스케줄 조회에 성공했습니다.')
            else :
                print('스케줄 조회에 실패했습니다.')
        else :
            print('존재하지 않는 선택 메뉴입니다.\n다시 선택해주세요')

        