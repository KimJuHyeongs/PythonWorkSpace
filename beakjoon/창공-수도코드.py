# def 예약(아이디) :
#     global 총_주문번호, 예약_queue
    
#     총_주문번호, 웨이팅번호 = 총_주문번호 + 1, len(예약_queue) + 1
#     예약_queue.append(아이디, 총_주문번호, 웨이팅번호)
#     return 총_주문번호, 웨이팅번호

# # def 주문및결제(아이디, 테이블번호) :
# #     global 장바구니_dict, 테이블_dict, 주문_dict, 총_주문번호
# #     금액, 업체 = 0, list()
    
# #     for 번호, 메뉴이름 , 메뉴가격 in (장바구니_dict[아이디]) :
# #         금액 += 메뉴가격
# #         업체.append((번호, 메뉴이름))
    
# #     try :
# #         #결제 성공
# #         if 결제(금액):
# #             for 업체번호, 메뉴이름 in 업체 :
# #                 #각 업체에 주문 메뉴 전달
# #                 전달(업체번호, 메뉴이름)
# #                 주문[아이디].append(총_주문번호, list())
            
# #             del 장바구니_dict[아이디]
# #             # 각 테이블의 주문한 음식 수
# #             테이블_dict[테이블번호][2] += len(업체)
            
# #             return True
# #         #결제 실패
# #         else:
# #             return False
# #     # 결제 중 에러 발생
# #     except :
# #         return False

# # def 식사종료(식판번호):
# #     global  테이블_dict, 주문_dict
# #     결과 = -1
    
# #     for key, value in 주문_dict.items():
# #         # 식판 번호
# #         if value[0] == 식판번호:
# #             # 각 테이블의 주문한 음식 수
# #             테이블_dict[key][2] -= 1
# #             if 테이블_dict[key][2] == 0:
# #                 결과 = key
# #             break
    
# #     return 결과
    


# # def 자리선택(방문인원, 아이디) :
# #     global 테이블_dict, 현재_사용중인_테이블_수
    
# #     사용가능 = 전체_테이블_수 - 사용중인_테이블_수
# #     필요한_수 = max(1, (방문인원 // 4) )
# #     선택가능 = 사용가능 - 필요한_수
# #     현재선택 = 0
    
# #     while (선택가능 > 현재선택) :
# #         테이블_번호 = 테이블선택()
# #         # 테이블 사용 여부
# #         테이블_dict[테이블_번호][0] = True
# #         # 테이블 사용자 아이디
# #         테이블_dict[테이블_번호][1] = 아이디
# #         현재선택 += 1
    
# #     if 현재선택 == 선택가능:
# #         현재_사용중인_테이블_수 += 현재선택
# #         return True
# #     else :
# #         return False
    
# # def 예약_자리발생():
# #     global 예약_queue
    
# #     현재아이디, _ , _ = 예약_queue.pop(0)
# #     for 아이디, 대기표, 웨이팅 in (예약_queue) :
# #         웨이팅 -= 1
    
# #     return 현재아이디
    

  
# # def 빈자리_판단(방문인원) :
# #     사용가능 = 전체_테이블_수 - 사용중인_테이블_수
# #     필요한_수 = max(1, (방문인원 // 4) )
    
# #     if 사용가능 >= 필요한_수:
# #         return True
# #     else :
# #         return False
    
    
    
# # a = {1 : 'abc', 2 : 'bfe'}
# # for k,v in a.items():
# #     if(v == 'bfe'):
# #         print(k)