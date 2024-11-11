# init python:
#     import requests

#     def send_to_raspberry_pi():
#         url = 'http://10.150.151.164:5000'  # 서버의 GET 엔드포인트

#         try:
#             response = requests.get(url)
#             response.raise_for_status()  # HTTP 오류가 발생하면 예외 발생
#             received_value = response.text  # 문자열로 응답 받기
#             renpy.notify("서버에서 받은 값: " + received_value)
#         except Exception as e:
#             renpy.notify("서버에 연결할 수 없습니다.")
#             renpy.error(str(e))


init python:
    def set_player_name():
        global pn
        pn = renpy.input("당신의 이름을 입력하세요:")

        # 이름이 비어 있을 경우 기본 이름으로 설정
        if pn == "":
            pn = "김주인"

# 캐릭터 호감도 초기화
$ f_hana_love = 0
$ f_ari_love = 0
$ f_mirae_love = 0

# 플레이어의 심박수 측정
label measure_heart_rate:
    # 초기 심박수 측정
    $ player_initial_heart_rate = renpy.call_in_new_context("measure_heart_rate")
    return
#배경사진
image white =  "images/background/white.png"

#플레이어
define h = Character('이하나', color="#c8ffc8") #활발한 여학생
define m = Character('김미래', color="#c8ffc8") #차분하고 논리적인 여학생
define a = Character('금아리', color="#c8ffc8") #신비주의 여학생
define s = Character('시스템') #힌트&설명
define d = Character('학동운') #연인관계의 도움친구
define pn = ""
define q = Character('???') #첫 등장





label start:
    # $ send_to_raspberry_pi()
    scene black
    $ set_player_name()
    s "주인공 이름이 [pn]으로 설정되었습니다."
    menu:
        "test1":
            "test1"
        "test2":
            "test2"
        "test3":
            "test3"
        "test4":
            "test4"

    jump first_day
# 1일차
label first_day:
    
    scene black

    #영상 있으면 만들기

    s "이 게임은 사용자의 심박수의 증가&감소에따라 선택지가 달라지니 이 포인트를 잘 활용해서 플레이하시길 바랍니다."

    s "재밌게 플레이해주세요."

    "주인공은 심박동 센서를 통해 자신의 심박수를 측정했다."
    $ player_heart_rate = renpy.call_in_new_context("measure_heart_rate")  # 심박수 측정


    "..."
    
    ".."

    #스크린 바꾸는거 넣기


    "오늘은 학교에 가는 첫번째 날이다"

    pn "그럼 활기차게 출발해 볼까?"



    "학교에 가는도중 누군가 말을 건다"

    q "우리 학교 교복인데 처음 보는거같은데..? "
    q "오늘 전학온다는 친구야?! "
    
    #하나 캐릭터 등장

    h "안녕! 나는 1학년 4반에 이하나라고 해!!"

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "하나에게 반가운 얼굴로 인사하기":
                pn "안녕 만나서 반가워"
                $ f_hana_love += 5
                h "웅 안녕!!"
                h "나랑 친하게 지내자!"
                h "늦어서 먼저 갈께!"
                h "학교에서 보자!!"
                jump next_encounter1
            "하나에게 농담하기":
                pn "나 전학생 안전학생"
                $ f_hana_love += 10
                h "우와.."
                h "너 생각보다 재미있는 사람이네!"
                h "나랑 학교 같이 가자 !"
                jump next_encounter1
    else:
        menu:
            "하나에게 소극적으로 인사하기":
                pn "ㅇ.. 안녕?"
                $ f_hana_love -= 5
                h "어... 안녕?"
                jump next_encounter1
            "하나에게 무관심하기:":
                pn "..."
                $ f_hana_love -= 10
                h "어... 학교에서 보자..!"
                jump next_encounter1

label next_encounter1:
    "하나를 "
    "이제 차분하고 논리적인 여자, 진이 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "진에게 자신감 있게 이야기하기:":
                $ f_jin_love += 10
                "진: '너의 심박수가 많이 올라가고 있네!'"
                jump mirae_encounter1
            "진에게 질문하기:":
                $ f_jin_love += 5
                "진: '어떤 과목이 제일 좋아?'"
                jump mirae_encounter1
    else:
        menu:
            "진에게 조용히 말하기:":
                $ f_jin_love -= 5
                "진: '너의 기분이 어때?'"
                jump mirae_encounter1
            "진에게 무관심하기:":
                $ f_jin_love -= 10
                "진: '그래도 관심을 가져줬으면 좋겠네.'"
                jump mirae_encounter1

label mirae_encounter1:
    "이제 신비로운 전학생, 미래가 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "미래에게 호기심을 보이며 질문하기:":
                $ f_mirae_love += 10
                "미래: '너의 감정을 읽을 수 있어. 흥미롭네.'"
                jump end_first_day
            "미래에게 자신 있게 이야기하기:":
                $ f_mirae_love += 5
                "미래: '너와 이야기하고 싶어!'" 
                jump end_first_day
    else:
        menu:
            "미래에게 무관심하기:":
                $ f_mirae_love -= 10
                "미래: '너와의 대화가 너무 그립다.'"
                jump end_first_day
            "미래에게 조용히 말하기:":
                $ f_mirae_love -= 5
                "미래: '어떤 이야기를 할까? 아쉽다.'"
                jump end_first_day

label end_first_day:
    "첫날이 끝났다."
    jump second_day

# 2일차
label second_day:
    scene bg school
    "두 번째 날, 주인공은 긴장한 마음으로 학교에 갔다."
    $ player_heart_rate = renpy.call_in_new_context("measure_heart_rate")  # 새로운 심박수 측정

    "하나가 먼저 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "하나에게 자신 있게 이야기하기:":
                $ f_hana_love += 10
                "하나: '너의 기분이 좋구나!'"
                jump jin_encounter2
            "하나에게 농담하기:":
                $ f_hana_love += 5
                "하나: '재미있는 사람이네!'"
                jump jin_encounter2
    else:
        menu:
            "하나에게 소극적으로 대답하기:":
                $ f_hana_love -= 5
                "하나: '어... 안녕?'"
                jump jin_encounter2
            "하나에게 무관심하기:":
                $ f_hana_love -= 10
                "하나: '아쉬워... 더 많은 대화가 필요해.'"
                jump jin_encounter2

label jin_encounter2:
    "진이 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "진에게 도움 요청하기:":
                $ f_jin_love += 10
                "진: '물론이지! 도와줄게.'"
                jump mirae_encounter2
            "진에게 질문하기:":
                $ f_jin_love += 5
                "진: '어떤 과목이 제일 좋아?'"
                jump mirae_encounter2
    else:
        menu:
            "진에게 무관심하기:":
                $ f_jin_love -= 10
                "진: '그래도 관심을 가져줬으면 좋겠네.'"
                jump mirae_encounter2
            "진에게 짧게 대답하기:":
                $ f_jin_love -= 5
                "진: '나는 너를 잘 모르겠어.'"
                jump mirae_encounter2

label mirae_encounter2:
    "미래가 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "미래에게 호기심을 보이며 질문하기:":
                $ f_mirae_love += 10
                "미래: '너의 감정을 읽을 수 있어. 흥미롭네.'"
                jump end_second_day
            "미래에게 흥미로운 이야기하기:":
                $ f_mirae_love += 5
                "미래: '너의 이야기를 더 듣고 싶어.'"
                jump end_second_day
    else:
        menu:
            "미래에게 무관심하기:":
                $ f_mirae_love -= 10
                "미래: '너와의 대화가 너무 그립다.'"
                jump end_second_day
            "미래에게 조용히 말하기:":
                $ f_mirae_love -= 5
                "미래: '어떤 이야기를 할까? 아쉽다.'"
                jump end_second_day

label end_second_day:
    "두 번째 날이 끝났다."
    jump third_day

# 3일차
label third_day:
    scene bg school
    "세 번째 날, 주인공은 친구들과 함께 공부하기로 했다."
    $ player_heart_rate = renpy.call_in_new_context("measure_heart_rate")  # 새로운 심박수 측정

    "하나가 먼저 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "하나에게 공부에 대해 이야기하기:":
                $ f_hana_love += 10
                "하나: '좋은 아이디어야! 같이 하자!'"
                jump jin_encounter3
            "하나에게 계획을 말하기:":
                $ f_hana_love += 5
                "하나: '너와 함께하는 게 기대돼!'"
                jump jin_encounter3
    else:
        menu:
            "하나에게 조용히 말하기:":
                $ f_hana_love -= 5
                "하나: '너무 긴장하지 마!'"
                jump jin_encounter3
            "하나에게 무관심하기:":
                $ f_hana_love -= 10
                "하나: '아쉽다... 이야기하고 싶었는데.'"
                jump jin_encounter3

label jin_encounter3:
    "진이 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "진에게 공부 방법을 물어보기:":
                $ f_jin_love += 10
                "진: '내가 도와줄게!'" 
                jump mirae_encounter3
            "진에게 좋은 팁을 주기:":
                $ f_jin_love += 5
                "진: '고마워, 나도 배울게!'" 
                jump mirae_encounter3
                ### Ren'Py 스토리 초안 (3일차 ~ 7일차)


# 3일차 (계속)
label mirae_encounter3:
    "미래가 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "미래에게 감정을 표현하기:":
                $ f_mirae_love += 10
                "미래: '너의 감정을 이해할 수 있어. 흥미롭네.'"
                jump end_third_day
            "미래에게 흥미로운 질문하기:":
                $ f_mirae_love += 5
                "미래: '너와 대화하는 게 즐거워!'"
                jump end_third_day
    else:
        menu:
            "미래에게 무관심하기:":
                $ f_mirae_love -= 10
                "미래: '아쉽다... 대화할 기회가 없었네.'"
                jump end_third_day
            "미래에게 짧게 대답하기:":
                $ f_mirae_love -= 5
                "미래: '더 이야기할 걸 그랬어.'"
                jump end_third_day

label end_third_day:
    "세 번째 날이 끝났다."
    jump fourth_day

# 4일차
label fourth_day:
    scene bg school
    "네 번째 날, 주인공은 친구들과의 점심시간을 기다리고 있었다."
    $ player_heart_rate = renpy.call_in_new_context("measure_heart_rate")  # 새로운 심박수 측정

    "하나가 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "하나와 점심 먹기로 약속하기:":
                $ f_hana_love += 10
                "하나: '좋아! 같이 가자!'"
                jump jin_encounter4
            "하나에게 재미있는 이야기하기:":
                $ f_hana_love += 5
                "하나: '너와의 대화가 기대돼!'" 
                jump jin_encounter4
    else:
        menu:
            "하나에게 조용히 대답하기:":
                $ f_hana_love -= 5
                "하나: '왜 이렇게 수줍어해?'" 
                jump jin_encounter4
            "하나에게 무관심하기:":
                $ f_hana_love -= 10
                "하나: '아쉬워... 더 많은 대화가 필요해.'" 
                jump jin_encounter4

label jin_encounter4:
    "진이 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "진에게 점심 메뉴 추천하기:":
                $ f_jin_love += 10
                "진: '좋은 선택이야! 나도 그거 좋아해.'"
                jump mirae_encounter4
            "진에게 점심 계획을 공유하기:":
                $ f_jin_love += 5
                "진: '너와 함께 하는 게 기대돼!'"
                jump mirae_encounter4
    else:
        menu:
            "진에게 점심에 대한 질문하기:":
                $ f_jin_love -= 5
                "진: '너의 입맛을 잘 모르겠어.'"
                jump mirae_encounter4
            "진에게 무관심하기:":
                $ f_jin_love -= 10
                "진: '그래도 내 점심은 중요해.'" 
                jump mirae_encounter4

label mirae_encounter4:
    "미래가 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "미래에게 흥미로운 이야기를 나누기:":
                $ f_mirae_love += 10
                "미래: '너의 감정은 나에게 보이네. 신기해!'"
                jump end_fourth_day
            "미래에게 다가가서 물어보기:":
                $ f_mirae_love += 5
                "미래: '너와의 대화가 즐거워.'"
                jump end_fourth_day
    else:
        menu:
            "미래에게 조용히 다가가기:":
                $ f_mirae_love -= 10
                "미래: '너와 대화하기가 어려워...' "
                jump end_fourth_day
            "미래에게 무관심하기:":
                $ f_mirae_love -= 5
                "미래: '아쉽다... 더 이야기하고 싶었어.'"
                jump end_fourth_day

label end_fourth_day:
    "네 번째 날이 끝났다."
    jump fifth_day

# 5일차
label fifth_day:
    scene bg school
    "다섯 번째 날, 친구들과의 공부가 기다려졌다."
    $ player_heart_rate = renpy.call_in_new_context("measure_heart_rate")  # 새로운 심박수 측정

    "하나가 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "하나에게 공부 방법 물어보기:":
                $ f_hana_love += 10
                "하나: '너와 함께 공부하면 좋겠다!'"
                jump jin_encounter5
            "하나와 함께 공부하자고 제안하기:":
                $ f_hana_love += 5
                "하나: '좋은 아이디어야! 같이 해보자!'"
                jump jin_encounter5
    else:
        menu:
            "하나에게 간단히 대답하기:":
                $ f_hana_love -= 5
                "하나: '너가 좀 긴장했나 봐.'" 
                jump jin_encounter5
            "하나에게 무관심하기:":
                $ f_hana_love -= 10
                "하나: '아쉬워... 대화가 필요해.'" 
                jump jin_encounter5

label jin_encounter5:
    "진이 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "진에게 공부를 함께 하자고 제안하기:":
                $ f_jin_love += 10
                "진: '좋아, 함께 하면 좋겠어!'" 
                jump mirae_encounter5
            "진에게 공부할 과목에 대해 이야기하기:":
                $ f_jin_love += 5
                "진: '좋은 아이디어야! 나는 그 과목이 좋아.'" 
                jump mirae_encounter5
    else:
        menu:
            "진에게 조용히 대답하기:":
                $ f_jin_love -= 5
                "진: '넌 좀 소극적이네.'" 
                jump mirae_encounter5
            "진에게 무관심하기:":
                $ f_jin_love -= 10
                "진: '그래도 내 공부는 중요해.'" 
                jump mirae_encounter5

label mirae_encounter5:
    "미래가 다가왔다."

    if player_heart_rate > player_initial_heart_rate:
        menu:
            "미래에게 공부 방법에 대해 물어보기:":
                $ f_mirae_love += 10
                "미래: '너의 감정이 잘 드러나고 있어. 신기해!'"
                jump end_fifth_day
            "미래에게 흥미로운 질문하기:":
                $ f_mirae_love += 5
                "미래: '너와의 대화가 즐거워!'" 
                jump end_fifth_day
    else:
        menu:
            "미래에게 무관심하기:":
                $ f_mirae_love -= 10
                "미래: '아쉽다... 대화하기가 힘들어.'" 
                jump end_fifth_day
            "미래에게 조용히 말하기:":
                $ f_mirae_love -= 5
                "미래: '더 이야기할 걸 그랬어.'" 
                jump end_fifth_day

label end_fifth_day:
    "다섯 번째 날이 끝났다."
    jump sixth_day


# 6일차


label sixth_day:
    scene bg school
    "학교에 가는 길에 오늘도 여전히 긴장한 주인공의 심박수는 높았다."
    
    "하나는 오늘도 먼저 다가왔다."
    $ heart_rate = renpy.call_in_new_context("measure_heart_rate")

    "하나: '오늘도 화이팅! 심박수 많이 올라갔네?'"

    if heart_rate > initial_heart_rate:
        menu:
            "하나에게 격려하기:":
                $ f_hana_love += 10
                "하나: '너무 좋다! 계속 이렇게 해보자!'"
                jump sixth_day_next_encounter
            "하나에게 안심시키기:":
                $ f_hana_love += 5
                "하나: '편하게 해. 친구로서 도와줄게!'"
                jump sixth_day_next_encounter
    else:
        menu:
            "하나에게 주의 깊게 듣기:":
                $ f_hana_love += 5
                "하나: '괜찮아? 나한테 말해도 돼!'"
                jump sixth_day_next_encounter
            "하나에게 무관심하기:":
                $ f_hana_love -= 5
                "하나: '왜 이렇게 쌀쌀맞아? 좀 더 즐겁게 지내자!'"
                jump sixth_day_next_encounter

label sixth_day_next_encounter:
    "진이 다가와 오늘도 차분하게 이야기한다."

    if heart_rate > initial_heart_rate:
        menu:
            "진에게 흥미로운 사실 말하기:":
                $ f_jin_love += 10
                "진: '너의 심박수가 변하고 있어. 무엇이 그렇게 흥미로워?'"
                jump sixth_day_mirae_encounter
            "진에게 자신의 감정 공유하기:":
                $ f_jin_love += 5
                "진: '나도 그런 기분 알겠어. 우리 같이 고민해보자.'"
                jump sixth_day_mirae_encounter
    else:
        menu:
            "진에게 고민 상담하기:":
                $ f_jin_love += 5
                "진: '뭔가 고민 있는 것 같아. 이야기해봐.'"
                jump sixth_day_mirae_encounter
            "진에게 무관심하기:":
                $ f_jin_love -= 5
                "진: '내가 도와줄게... 무시하지 마.'"
                jump sixth_day_mirae_encounter

label sixth_day_mirae_encounter:
    "미래가 다가와서 신비롭게 말을 건넨다."

    if heart_rate > initial_heart_rate:
        menu:
            "미래에게 마음의 비밀 이야기하기:":
                $ f_mirae_love += 10
                "미래: '너의 심장 소리가 들려. 무언가 특별한 것이 있네.'"
                jump end_sixth_day
            "미래에게 감정 표현하기:":
                $ f_mirae_love += 5
                "미래: '너와의 대화는 언제나 신비롭다.'"
                jump end_sixth_day
    else:
        menu:
            "미래에게 감정 숨기기:":
                $ f_mirae_love -= 5
                "미래: '너무 감정을 숨기지 마. 솔직해지는 게 좋아.'"
                jump end_sixth_day
            "미래에게 무관심하기:":
                $ f_mirae_love -= 5
                "미래: '너의 마음을 더 알고 싶었는데 아쉬워.'"
                jump end_sixth_day

label end_sixth_day:
    jump seventh_day
    "오늘 하루가 끝났다. 호감도가 변화하였다."
    # 후속 스토리 추가


label seventh_day:
    scene bg school
    "마지막 날, 주인공은 긴장과 기대가 섞인 마음으로 학교에 갔다."
    
    $ heart_rate = renpy.call_in_new_context("measure_heart_rate")

    "하나가 다가와서 밝게 웃었다."

    if heart_rate > initial_heart_rate:
        menu:
            "하나에게 오늘의 계획 말하기:":
                $ f_hana_love += 10
                "하나: '와! 정말 기대돼! 같이 놀러 가자!'"
                jump seventh_day_final_encounter
            "하나에게 긍정적인 이야기하기:":
                $ f_hana_love += 5
                "하나: '너랑 이야기하니까 기분이 좋다!'"
                jump seventh_day_final_encounter
    else:
        menu:
            "하나에게 고민 털어놓기:":
                $ f_hana_love += 5
                "하나: '너와 얘기하는 게 도움이 돼.'"
                jump seventh_day_final_encounter
            "하나에게 무관심하기:":
                $ f_hana_love -= 5
                "하나: '오늘은 왜 이렇게 쌀쌀맞아?'"
                jump seventh_day_final_encounter

label seventh_day_final_encounter:
    "진이 오랜만에 나타나서 차분하게 말한다."

    if heart_rate > initial_heart_rate:
        menu:
            "진에게 진지하게 이야기하기:":
                $ f_jin_love += 10
                "진: '너의 진심이 느껴져. 정말 고마워!'"
                jump end_seventh_day
            "진에게 애정 표현하기:":
                $ f_jin_love += 5
                "진: '너와 함께하는 시간이 소중해.'"
                jump end_seventh_day
    else:
        menu:
            "진에게 고민 나누기:":
                $ f_jin_love += 5
                "진: '모두가 힘든 날도 있어. 괜찮아.'"
                jump end_seventh_day
            "진에게 무관심하기:":
                $ f_jin_love -= 5
                "진: '좀 더 솔직해지면 좋겠어.'"
                jump end_seventh_day

label end_seventh_day:
    "미래가 조용히 다가와 말했다."

    if heart_rate > initial_heart_rate:
        menu:
            "미래에게 고백하기:":
                $ f_mirae_love += 10
                "미래: '너의 마음을 읽었어. 나도 너를 좋아해.'"
                jump seventh_day_conclusion
            "미래에게 깊은 대화하기:":
                $ f_mirae_love += 5
                "미래: '우리의 미래는 정말 흥미롭겠네.'"
                jump seventh_day_conclusion
    else:
        menu:
            "미래에게 솔직해지기:":
                $ f_mirae_love += 5
                "미래: '진솔한 대화는 언제나 중요해.'"
                jump seventh_day_conclusion
            "미래에게 무관심하기:":
                $ f_mirae_love -= 5
                "미래: '아쉬워. 좀 더 알 수 있었는데.'"
                jump seventh_day_conclusion

label seventh_day_conclusion:
    "모든 일이 끝나고, 주인공은 자신의 감정을 돌아보았다."
    if f_hana_love >= f_jin_love and f_hana_love >= f_mirae_love:
        jump hana_ending_check
    elif f_jin_love >= f_hana_love and f_jin_love >= f_mirae_love:
        jump jin_ending_check
    else:
        jump mirae_ending_check




label hana_ending_check:
    if f_hana_love >= 70:
        jump hana_good_ending
    elif f_hana_love >= 40:
        jump hana_normal_ending
    else:
        jump hana_bad_ending

label jin_ending_check:
    if f_jin_love >= 70:
        jump jin_good_ending
    elif f_jin_love >= 40:
        jump jin_normal_ending
    else:
        jump jin_bad_ending

label mirae_ending_check:
    if f_mirae_love >= 70:
        jump mirae_good_ending
    elif f_mirae_love >= 40:
        jump mirae_normal_ending
    else:
        jump mirae_bad_ending

label hana_good_ending:
    scene bg sunset
    "하나: '너와 함께한 시간들 정말 즐거웠어. 우리 계속 함께 할 수 있을까?'"
    "주인공은 하나와 손을 맞잡고 밝은 미래를 약속했다."
    return

label hana_normal_ending:
    scene bg park
    "하나: '우리 친구로 남아도 괜찮겠지? 그래도 즐거웠어.'"
    "주인공과 하나는 친밀한 친구로 남게 되었다."
    return

label hana_bad_ending:
    scene bg cloudy_day
    "하나: '우리 더 이상 만날 이유가 없는 것 같아.'"
    "주인공과 하나는 서서히 멀어졌다."
    return

label jin_good_ending:
    scene bg library
    "진: '네가 나를 이렇게 이해해주다니 놀라워. 우리 더 깊이 알아가볼래?'"
    "진과 주인공은 서로에 대한 깊은 이해를 바탕으로 연인이 되었다."
    return

label jin_normal_ending:
    scene bg street
    "진: '우리 그냥 이 정도 관계가 좋을 것 같아. 부담 없이.'"
    "주인공과 진은 서로 존중하며 좋은 관계를 유지했다."
    return

label jin_bad_ending:
    scene bg dark_room
    "진: '너랑은 생각이 좀 많이 다른 것 같아. 앞으로 각자 길을 가는 게 좋겠어.'"
    "주인공과 진은 더 이상 만나지 않게 되었다."
    return

label mirae_good_ending:
    scene bg forest
    "미래: '네 감정을 이렇게까지 읽어내게 될 줄 몰랐어. 정말 신기한 사람이야.'"
    "주인공과 미래는 서로의 감정을 깊이 이해하며 새로운 여정을 함께 떠났다."
    return

label mirae_normal_ending:
    scene bg school
    "미래: '우린 그냥 스쳐 지나가는 인연이었을지도 몰라. 그래도 고마워.'"
    "주인공과 미래는 서로를 기억하며 헤어졌다."
    return

label mirae_bad_ending:
    scene bg foggy
    "미래: '너와 함께할 미래는 없을 것 같아. 미안해.'"
    "미래와 주인공은 갈라서고, 다시는 서로를 마주치지 않았다."
    return
