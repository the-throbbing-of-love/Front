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
define a = Character('a선배', color="#c8ffc8") #활발한 여선배
define m = Character('김미래', color="#c8ffc8") #동급생 츤데레 여학생
define a = Character('금아리', color="#c8ffc8") #동급생 신비주의 여학생
define s = Character('시스템') #힌트&설명
define d = Character('학동운') #연인관계의 도움친구
define pn = ""
define q = Character('???') #첫 등장


#캐릭터
image a_base = im.Scale("images/charater/a/a_base.png", 950, 1000)




label start:
    # $ send_to_raspberry_pi()
    scene white
    $ set_player_name()
    s "주인공 이름이 [pn]으로 설정되었습니다."

    jump first_day
# 1일차
label first_day:
    
    scene black

    #영상 있으면 만들기

    s "이 게임은 사용자의 심박수의 증가&감소에따라 선택지가 달라지니 이 포인트를 잘 활용해서 플레이하시길 바랍니다."

    s "재밌게 플레이해주세요."

    "주인공은 심박동 센서를 통해 자신의 심박수를 측정했다."
    # $ player_heart_rate = renpy.call_in_new_context("measure_heart_rate")  # 심박수 측정

    # Chapter 1: 입학식
    "봄의 따뜻한 햇살이 비치는 교정에 부스들이 가득 펼쳐져 있었다."
    "신입생인 나는 새로 시작하는 대학 생활에 설레기도 하고, 한편으론 낯선 분위기에 긴장도 되었다."
    
    # 선배 등장
    show a_base at left with dissolve 
    a "안녕! 신입생 맞지? 동아리 알아보고 있어?"
    
    # 첫 대화 선택지
    menu:
        #심박 높음
        "조금 둘러보고 있어요":
            "부스 구경 중이던 내게 선배가 친근하게 다가왔다."
            a "그럼 우리 사진 동아리는 어때? 다양한 활동도 많고 재밌어!"
        
        "네, 하지만 뭐가 좋을지 모르겠네요":
            "막연히 둘러보고 있던 내게 선배가 추천을 시작했다."
            a "음, 사진 동아리 어때? 여행도 가고 추억도 남길 수 있어."
        #심박 낮음
        "아니요":
            a "에이 그러지말구"
            a "우리 사진 동아리 어때?!"
        
        "....":
            "sda"
        

        
    "나는 선배의 말에 이끌려 사진 동아리에 흥미가 생겼다."
    
    # 동아리 가입을 권유하며 선택지를 제공
    a "좋아! 관심 있다면 참가서 작성하고 가. 네가 관심 있으면 나중에 후회 안 할 거야!"
    menu:
        "사진 동아리에 가입한다":
            "동아리 참가서를 작성하며 선배의 기대 어린 눈빛을 느낄 수 있었다."
            show a_senior at left with dissolve
            a "잘 생각했어! 이거 꽉 채워서 작성해줘!"
            
            # 가입 이유 확인 선택지
            "작성을 마치자 선배가 질문했다."
            a "근데 정말 하고 싶어서 작성한 거 맞아? 잠깐의 호기심만으로는 힘들 수도 있어."
            menu:
                "네, 하고 싶어서 작성했어요":
                    "내가 정말 이 동아리에 기대가 컸다는 생각에 진심을 담아 대답했다."
                    a "좋아, 그런 마음이라면 반드시 우리 동아리에 잘 어울릴 거야!"
                
                "아직 잘 모르겠지만, 해보고 결정해볼게요":
                    a "그래, 해보면서 점차 느껴봐. 사진 찍는 즐거움은 경험해 봐야 알 수 있거든."
            
            a "첫 모임은 다음 주 수요일 오후 6시! 장소는 동아리 방이니까 잊지 마!"
        
        "아직 결정을 내리지 않았다":
            a "알겠어. 혹시라도 마음이 바뀌면 언제든 우리 동아리로 와!"
            "나는 조금 더 고민하기로 하고, 다른 부스를 둘러보기로 했다."

    # 집으로 가는 길
    "그렇게 입학식이 끝나고 집으로 가는 길에 들뜬 마음을 진정시키며 캠퍼스를 걷고 있었다."
    "갑자기 사람들이 모여서 환호하는 소리가 들려 발걸음을 멈췄다."
    
    # 댄스 공연 장면
    scene bg_dance_stage
    "사람들이 모여 있는 쪽으로 다가가 보니, 무대 위에서 댄스 공연이 한창이었다."
    "화려한 춤과 함께 무대를 채운 그들 중에서도 유독 눈에 띄는 선배가 있었다."
    
    # 동아리 장 등장
    show dance_leader at center with dissolve
    "그녀는 강렬한 눈빛으로 무대를 지배하며, 멋진 춤 동작을 선보이고 있었다."
    "나는 그 선배가 자꾸만 눈에 들어와 공연이 끝날 때까지 시선을 떼지 못했다."
    
    # 선배 정체 확인
    "공연이 끝난 후, 옆에 있던 친구가 그녀를 가리키며 말했다."
    friend "저 선배, 우리 학교에서 엄청 유명해! 듣자 하니, 네가 가입한 사진 동아리의 동아리 장이래!"
    
    "동아리 장이자, 그 화려한 무대 위의 주인공… 뭔가 묘하게 가슴이 두근거렸다."
    "이제 다음 주 첫 모임이 더욱 기다려지는 걸 느끼며, 나는 집으로 향했다."