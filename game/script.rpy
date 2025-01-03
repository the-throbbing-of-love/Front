﻿init:
    #a 텍스트 박스
    style a_textbox:
        background im.Scale("images/textbox/a_textbox.png", 2024, 389)  # 캐릭터 전용 박스 배경
        font "ONE Moblie POP.ttf"
        color "#000000" 
        size (0.5, 0.5)  # 너비 500px, 세로는 화면 크기의 20%로 설정
        xpos 0.5  # 화면 가로 중앙
        text_align 3.5
        padding (410, 10) 
        ypos 1.14  # 화면 아래쪽
        xanchor 0.5  # 기준점을 중앙으로 설정
        yanchor 0.5  # 기준점을 중앙으로 설정
        xminimum 600  # 텍스트 박스 최소 너비
        yminimum 150  # 텍스트 박스 최소 높이



    style name_base:
        xanchor -0.4  # 기준점을 중앙
        yanchor -1.65 

    # 대사 텍스트 베이스
    style what_base:
        yanchor -4.5  # 높이


    #b 텍스트 박스
    style b_textbox:
        background im.Scale("images/textbox/b_textbox.png", 2024, 389)  # 캐릭터 전용 박스 배경
        font "ONE Moblie POP.ttf"
        color "#000000" 
        size (0.5, 0.5)  # 너비 500px, 세로는 화면 크기의 20%로 설정
        xpos 0.5  # 화면 가로 중앙
        text_align 3.5
        padding (410, 10) 
        ypos 1.14  # 화면 아래쪽
        xanchor 0.5  # 기준점을 중앙으로 설정
        yanchor 0.5  # 기준점을 중앙으로 설정
        xminimum 600  # 텍스트 박스 최소 너비
        yminimum 150  # 텍스트 박스 최소 높이


    #c 텍스트 박스
    style c_textbox:
        background im.Scale("images/textbox/c_textbox.png", 2024, 389)  # 캐릭터 전용 박스 배경
        font "ONE Moblie POP.ttf"
        color "#000000" 
        size (0.5, 0.5)  # 너비 500px, 세로는 화면 크기의 20%로 설정
        xpos 0.5  # 화면 가로 중앙
        text_align 3.5
        padding (410, 10) 
        ypos 1.14  # 화면 아래쪽
        xanchor 0.5  # 기준점을 중앙으로 설정
        yanchor 0.5  # 기준점을 중앙으로 설정
        xminimum 600  # 텍스트 박스 최소 너비
        yminimum 150  # 텍스트 박스 최소 높이


    #base 텍스트 박스
    style base_textbox:
        background im.Scale("images/textbox/character_box.png", 2024, 389)  # 캐릭터 전용 박스 배경
        font "ONE Moblie POP.ttf"
        color "#000000" 
        size (0.5, 0.5)  # 너비 500px, 세로는 화면 크기의 20%로 설정
        xpos 0.5  # 화면 가로 중앙
        text_align 3.5
        padding (410, 20) 
        ypos 1.14  # 화면 아래쪽
        xanchor 0.5  # 기준점을 중앙으로 설정
        yanchor 0.5  # 기준점을 중앙으로 설정
        xminimum 600  # 텍스트 박스 최소 너비
        yminimum 150  # 텍스트 박스 최소 높이


init python:
    import requests
    import json

    def send_to_raspberry_pi(new_round_number, scene):
        url = 'http://10.150.150.219:8000/heart/measurement'  # 서버의 POST 엔드포인트
        data = {  # 요청 본문 데이터
            'round_id': new_round_number,
            'page': scene
        }

        try:
            # POST 요청 보내기
            response = requests.post(url, data)
            response.raise_for_status()  # HTTP 오류가 발생하면 예외 발생
            
            # 응답을 JSON 형식으로 파싱
            received_value = response.json()  # JSON을 dict로 변환
            
            # dict를 문자열로 변환하여 출력
            
            return received_value
        except requests.exceptions.JSONDecodeError:
            renpy.notify("서버에서 JSON 응답을 받지 못했습니다.")
        except Exception as e:
            renpy.notify("서버에 연결할 수 없습니다.")
            renpy.error(str(e))




init python:
    import requests
    import json

    def create_new_round():
        #새로운 라운드 만들기
        url = 'http://10.150.150.219:8000/round/new-round'  # API URL

        try:
            # POST 요청
            response = requests.post(url)
            response.raise_for_status()

            # 응답 처리
            response_data = response.json()
            new_round = response_data.get("new-round")  # 'new-round' 키만 추출

            if new_round is not None:
                return {"success": True, "new_round": new_round}
            else:
                return {"success": False, "error": "응답에 회차 정보가 없습니다."}

        except requests.exceptions.RequestException as e:
            # 네트워크 오류 처리
            return {"success": False, "error": f"서버 연결 실패: {str(e)}"}
        except json.JSONDecodeError:
            # JSON 디코딩 오류
            return {"success": False, "error": "유효하지 않은 JSON 응답"}
        except Exception as e:
            # 기타 오류
            return {"success": False, "error": f"알 수 없는 오류: {str(e)}"}



init python:
    import requests
    import json

    def analyze_emotion(new_round_number, scene):
        """
        감정 분석 API 호출 함수
        """
        url = "http://10.150.150.219:8000/AI-analyze/face"  # API URL
        payload = {
            "round_id": new_round_number,
            "page": scene
        }

        try:
            response = requests.post(url, payload)
            response.raise_for_status()  # 예외 처리
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"status": 500, "error": f"서버 연결 실패: {str(e)}"}
        except json.JSONDecodeError:
            return {"status": 500, "error": "유효하지 않은 JSON 응답입니다."}









#트랜스펌
transform move_to_left:
    xalign 0.5 yalign 0.5  # 화면 중앙에서 시작
    zoom 0.5  
    linear 2.0 xalign 0.2 zoom 1.0 




init python:
    def set_player_name():
        global pn
        pn = renpy.input("당신의 이름을 입력하세요:")

        # 이름이 비어 있을 경우 기본 이름으로 설정
        if pn == "":
            pn = "김주인"

# 캐릭터 호감도 초기화
default a_love = 0
default b_love = 0
default c_love = 0


#커플 되었을때
default a_cup = 0
default b_cup = 0
default c_cup = 0

#이벤트 토큰
default a_back = 0
default b_back = 0
default danchan = 0
default danhan = 0

default round_id = 1
default page = 1

default test = None
default game_start = None
default api_url = None
default payload = None
default new_round_number = None
default comeimg = None
default scene = None 
default capephoto = None
default send_emotions = None 

# 플레이어의 심박수 측정
label measure_heart_rate:
    # 초기 심박수 측정
    $ player_initial_heart_rate = renpy.call_in_new_context("measure_heart_rate")
    return


#배경사진
image muda =  im.Scale("images/background/muda.png",1920,1080) 
image white =  im.Scale("images/background/white.png",1920,1080) 
image bg_school_event = im.Scale("images/background/bg_school_event.png",1920,1080) 
image school_event = im.Scale("images/background/school_event.jpeg",1920,1080) 
image school_buss = im.Scale("images/background/buss.png",1920,1080) 
image class = im.Scale("images/background/class.png",1920,1080) 
image hclass = im.Scale("images/background/hclass.png",1920,1080) 
image dongai = im.Scale("images/background/dongai.png",1920,1080) 
image chdongai = im.Scale("images/background/chdongai.png",1920,1080) 
image camera1 = im.Scale("images/background/camera1.png",1920,1080) 
image haha = im.Scale("images/background/haha.png",1920,1080) 
image hidehaha = im.Scale("images/background/hidehaha.png",1920,1080) 
image backha = im.Scale("images/background/backha.png",1920,1080) 
image mount = im.Scale("images/background/mount.png",1920,1080) 
image realmount = im.Scale("images/background/realmount.png",1920,1080) 
image highmount = im.Scale("images/background/highmount.png",1920,1080) 
image restaurant = im.Scale("images/background/restaurant.png",1920,1080) 
image suk = im.Scale("images/background/suk.png",1920,1080) 
image gii = im.Scale("images/background/gii.png",1920,1080) 
image sukfront = im.Scale("images/background/sukfront.png",1920,1080) 
image macdow = im.Scale("images/background/macdow.png",1920,1080) 
image chdongnone = im.Scale("images/background/chdongnone.png",1920,1080) 
image booo = im.Scale("images/background/booo.png",1920,1080) 
image photo_booth = im.Scale("images/background/photo_booth.png",1920,1080) 
image dengi = im.Scale("images/background/dengi.png",1920,1080) 
image dongC = im.Scale("images/background/dong_C.png",1920,1080) 






#플레이어
define a = Character('윤아린', color="#AD9480", namebox_style="name_base" ,window_style="a_textbox", what_color="#000000", what_style="what_base") #활발한 여선배
define b = Character('이서현', color="#E9ADFF", namebox_style="name_base" ,window_style="b_textbox", what_color="#000000", what_style="what_base") #동급생 츤데레 여학생
define c = Character('박서연', color="#2F3364", namebox_style="name_base" ,window_style="c_textbox", what_color="#000000", what_style="what_base") #동급생 신비주의 여학생
define s = Character('시스템') #힌트&설명
define friend = Character('윤동운', namebox_style="name_base" ,window_style="base_textbox", what_color="#000000", what_style="what_base") #연인관계의 도움친구
define pn = ""
define q = Character('???', namebox_style="name_base" ,window_style="base_textbox", what_color="#000000", what_style="what_base") #첫 등장
define camera_senior = Character('김민주', namebox_style="name_base" ,window_style="base_textbox", what_color="#000000", what_style="what_base")
define unknown= Character('동급생', namebox_style="name_base" ,window_style="base_textbox", what_color="#000000", what_style="what_base")


#a
image a_base = im.Scale("images/charater/a/a_base.png", 1000, 1100)
image a_lol = im.Scale("images/charater/a/a_lol.png", 1000, 1100)
image a_sad = im.Scale("images/charater/a/a_sad.png", 1000, 1100)
image a_shy = im.Scale("images/charater/a/a_shy.png", 1000, 1100)
image a_TT = im.Scale("images/charater/a/a_TT.png", 1000, 1100)
image a_wak = im.Scale("images/charater/a/a_wak.png", 1000, 1100)
image a_worr = im.Scale("images/charater/a/a_worr.png", 1000, 1100)
image a_backha = im.Scale("images/charater/a/a_backha.png", 900, 1100)

#b
image b_base = im.Scale("images/charater/b/b_base.png", 1000, 1100)
image b_lol = im.Scale("images/charater/b/b_lol.png", 1000, 1100)
image b_sad = im.Scale("images/charater/b/b_sad.png", 1000, 1100)
image b_shy = im.Scale("images/charater/b/b_shy.png",1000, 1100)
image b_wak = im.Scale("images/charater/b/b_wak.png", 1000, 1100)
image b_worr = im.Scale("images/charater/b/b_worr.png", 1000, 1100)
image b_backha = im.Scale("images/charater/b/b_backha.png", 1000, 1000)



#c
image c_base = im.Scale("images/charater/c/c_base.png", 1000, 1100)
image c_lol = im.Scale("images/charater/c/c_lol.png", 1000, 1100)
image c_sad = im.Scale("images/charater/c/c_sad.png", 1000, 1100)
image c_shy = im.Scale("images/charater/c/c_shy.png", 1000, 1100)
image c_cute = im.Scale("images/charater/c/c_cute.png", 1000, 1100)
image c_worr = im.Scale("images/charater/c/c_worr.png", 1000, 1100)







#사이드캐릭터
image friend = im.Scale("images/charater/side/friend.png", 650, 1000)
image camera_senior = im.Scale("images/charater/side/camera_senior.png", 800, 1000)
image bongo = im.Scale("images/charater/side/bongo.png", 600, 1000)


#오브젝트
image report = im.Scale("images/object/report.png", 588, 832)
image goback1 = im.Scale("images/object/goback1.png", 560, 832)
image goback2 = im.Scale("images/object/goback2.png", 560, 832)
image goback3 = im.Scale("images/object/goback3.png", 560, 832)
image goback4 = im.Scale("images/object/goback4.png", 560, 832)
image goback = im.Scale("images/object/goback.png", 560, 832)
image gobackwin = im.Scale("images/object/gobackwin.png", 560, 832)
image gobacklose = im.Scale("images/object/gobacklose.png", 560, 832)
image gobackv2 = im.Scale("images/object/gobackv2.png", 560, 832)
image page1 = im.Scale("images/object/page1.png", 1080, 632)
image page2 = im.Scale("images/object/page2.png", 560, 832)
image page3 = im.Scale("images/object/page3.png", 560, 832)
image page4 = im.Scale("images/object/page4.png", 560, 832)
image page5 = im.Scale("images/object/page5.png", 560, 832)
image page6 = im.Scale("images/object/page6.png", 560, 832)





label open_camera_page:
    # Python 코드에서 웹 브라우저 열기
    python:
        import webbrowser
        # 서버의 /camera 경로를 호출
        url = f"http://10.150.150.219:8000/camera?scene={scene}&round_id={new_round_number}"
        webbrowser.open(url)
    
    return


label all_picture:
    # Python 코드에서 웹 브라우저 열기
    python:
        import webbrowser
        # 서버의 camera 경로를 호출
        url = f"http://10.150.150.219:8000/history?round_id={new_round_number}"
        webbrowser.open(url)
    
    return

label start:
    s "어떠한 플레이를 원하시나요?"
    menu:
        "기능을 중요로 보는 짧은 플레이":
            jump first_day
        "긴 스토리와 기능을 합친 긴 플레이":
            jump long_first_day
# 1일차
label first_day:
    $ scene = 1
    scene black
    #영상 있으면 만들기
    # Chapter 1: 입학식
    scene black
    s "이 게임은 사용자의 심박수의 증가&감소와 감정에따라 선택지가 달라지니 이 포인트를 잘 활용해서 플레이하시길 바랍니다."
    s "재밌게 플레이해주세요."   
    $ game_start = create_new_round() #라운드 불러오기
    $ new_round_number = game_start['new_round'] #라운드 값 함수에 저장
    
    "[new_round_number]번쨰 회차가 생성되었습니다"
    scene bg_school_event with dissolve
    play music "audio/bgm/base_music.mp3"
    "대학 입구에 도착하니, 웅장한 교문이 나를 맞이했다."


    # call open_camera_page #카메라 불러오기
    # $ send_emotions = analyze_emotion(new_round_number, scene) #표정불러오기
    #안써도됨# $ send_emotions_text = json.dumps(send_emotions, ensure_ascii=False).replace("{", "{{").replace("}", "}}")
    #안써도됨# "응답 데이터: [send_emotions_text]"

    # $ test = send_to_raspberry_pi(round_id, page) # 심박수 측정 호출



    
    "이곳에서 앞으로의 내 삶이 어떻게 바뀔지 상상하니 가슴이 두근거렸다."
    "새로운 시작에 대한 설렘과 약간의 두려움이 뒤섞인 복잡한 감정이 밀려왔다."


    scene school_event
    "입구를 지나니 봄의 따뜻한 햇살이 비치는 교정에 부스들이 가득 펼쳐져 있었다."
    "신입생인 나는 새로 시작하는 대학 생활에 설레기도 하고, 한편으론 낯선 분위기에 긴장도 되었다."
    
    # 친구 등장
    show friend at Transform(xalign=0.8, yalign=0.5) with dissolve:
        yalign 1.0

    friend "야, 무슨 동아리 들어갈 거야? 부스들 보니까 진짜 다양하더라."
    
    "친구의 말에 나는 주변을 둘러보았다. 각양각색의 동아리들이 자신들의 활동을 자랑하고 있었다."
    "스포츠, 학술, 문화... 선택지가 많아 어떤 동아리를 들어가야 할지 고민이 깊어졌다."


    friend "야 나 장유진이 불러서 나중에 보자!!"

    hide friend with dissolve

    "친구는 갑작스럽게 어디론가 뛰어갔다. 나는 홀로 남아 부스를 둘러보며 천천히 걸었다."

    scene school_buss
    "우연히 어떠한 부스를 지나고있었다."

    "누군가 나에게 말을 걸었다."

    # 선배 등장
    show a_base at move_to_left with dissolve
    q "안녕! 신입생 맞지? 동아리 알아보고 있어?"

    # 첫 대화 선택지
    $ send_emotions = analyze_emotion(new_round_number, scene)
    $ neutral = send_emotions["neutral"]
    $ happy = send_emotions["happy"]
    s "현재 감정 분석중입니다.. 웃으시면 '조금 둘러보고 있어요'라는 대사가 나오고 무표정이면 '네, 하지만 뭐가 좋을지 모르겠네요'라는 대사가 나옴니다."
    if happy >= neutral:
        #표정이 좋으면
        "조금 둘러보고 있어요"
        show a_base at left with move
        "부스 구경 중이던 내게 선배가 친근하게 다가왔다."
        a "그럼 우리 사진 동아리는 어때? 다양한 활동도 많고 재밌어!"
        "나는 사진 동아리에 대한 이야기를 들으며 조금씩 흥미가 생겼다."
        menu:
            "사진 동아리가 정말 그렇게 재미있나요?":
                $ a_love += 3
                "선배는 눈을 빛내며 고개를 끄덕였다."
                a "그럼! 단순히 사진 찍는 것만이 아니라, 전시회도 열고 전국 대회도 참여해!"
                "선배의 열정적인 설명에 나는 점점 더 끌렸다."
            
            "괜찮아 보이네요, 참가할게요.":
                $ a_love += 2
                "나는 사진 동아리에 참가하기로 결정했다."
                a "좋아! 그럼 참가서 작성해줘. 잘 생각했어!"
                "내가 참가서를 작성하는 동안 선배는 조언과 격려의 말을 아끼지 않았다."
    else:            
        #표정이 안좋으면
        "네, 하지만 뭐가 좋을지 모르겠네요"
        "막연히 둘러보고 있던 내게 선배가 추천을 시작했다."
        a "음, 사진 동아리 어때? 여행도 가고 추억도 남길 수 있어."
        menu:
            "사진 동아리 말고 다른 동아리도 추천해 주실 수 있나요?":
                $ a_love -= 3
                a "흠... 물론 다른 동아리도 많지. 하지만 사진 동아리는 너의 젊음을 기록하는 데 딱이야."
                "나는 선배가 말하는 '기록'이라는 단어가 마음에 와닿았다."
            
            "다른 동아리도 둘러보고 결정할게요.":
                $ a_love -= 2
                a "알겠어. 그래도 마음이 바뀌면 언제든 우리 동아리로 와!"
                "나는 아직 결정을 내리지 않고 다른 부스를 둘러보기로 했다."

    "나는 선배의 말에 이끌려 사진 동아리에 흥미가 생겼다."
    #extend 
    "그렇기에 나는 사진동아리에 들어가겠다고 다짐했다"
    # 동아리 가입을 권유하며 선택지를 제공
    
    a "좋아! 관심 있다면 참가서 작성하고 가. 네가 관심 있으면 나중에 후회 안 할 거야!"
    menu:
        "사진 동아리에 가입한다":
            hide a_base
            show a_shy at left
            $ a_love += 1
            a "잘 생각했어! 이거 꽉 채워서 작성해줘!"
            
            
            
            #이름적는 페이지
            show report at center
            a "여기에 이름을 적어줘!"
            $ set_player_name()
            "동아리 참가서를 작성하며 선배의 기대 어린 눈빛을 느낄 수 있었다."
            # 가입 이유 확인 선택지
            "[pn].."
            "작성을 마치자 선배가 질문했다."

            a "근데 정말 하고 싶어서 작성한 거 맞아? 잠깐의 호기심만으로는 힘들 수도 있어."
            menu:
                "네, 하고 싶어서 작성했어요":
                    $ a_love += 2
                    "내가 정말 이 동아리에 기대가 컸다는 생각에 진심을 담아 대답했다."
                    a "좋아, 그런 마음이라면 반드시 우리 동아리에 잘 어울릴 거야!"
                    "선배는 만족스러운 미소를 지으며 내 손을 힘차게 잡아주었다."
                
                "아직 잘 모르겠지만, 해보고 결정해볼게요":
                    $ a_love += 1
                    a "그래, 해보면서 점차 느껴봐. 사진 찍는 즐거움은 경험해 봐야 알 수 있거든."
                    "선배는 격려의 말과 함께 곧 열릴 첫 모임을 기대하라며 내 어깨를 두드렸다."
            
            a "첫 모임은 다음 주 수요일 오후 6시! 장소는 동아리 방이니까 잊지 마!"
    # 집으로 가는 길
    # @@@@@@@@@@@@@@@@@@@@@@@@@
    scene dengi
    "그렇게 입학식이 끝나고 집으로 가는 길에 들뜬 마음을 진정시키며 캠퍼스를 걷고 있었다."
    "이제 다음 주 첫 모임이 더욱 기다려지는 걸 느끼며, 나는 집으로 향했다."
    stop music fadeout 2.5
    scene black
    "..."
    ".."
    "."

    jump chapter_2

# Chapter 2: 첫 동아리 모임
label chapter_2:
    $ scene = 2
    "다음날이 되었다"
    play music "audio/bgm/base2_music.mp3"
    scene hclass
    "학교에 모든 수업이 끝나고 동아리 모임으로 향했다"
    scene class
    "동아리 앞에 도착했다."
    scene dongai
    play sound "audio/sound/DoorOpen.mp3"
    
    "드디어 사진 동아리의 첫 모임 날이 되었다. 동아리 방에 들어서자 여러 신입생과 선배들이 모여 있었다."
    
    # B 등장
    show b_base at right with dissolve
    b "안녕하세요! 혹시 여기가 사진 동아리 맞나요?"
    
    "들어오는 나와 동시에 동기인 서현이가 반갑게 인사하며 동아리 방에 들어왔다."
    "이곳에서 앞으로의 내 삶이 어떻게 바뀔지 상상하니 가슴이 두근거렸다."
    s "현재 심장박동 분석중입니다.. 높아지면 '서현에게 친근하게 인사를 건냈다'라는 선택지로 이동하고 낮아지면 '조용히 자리에 앉았다'라는 선택지로 이동합니다."
    $ test = send_to_raspberry_pi(new_round_number, scene) # 심박수 측정 호출
    if test['rising'] == True:
        #심장박동 오르면
        "서현에게 친근하게 인사를 건냈다"
        "나 역시 그에게 가볍게 손을 흔들며 인사를 건넸다."
        $ b_love += 3
        menu:
            "동아리에 대한 기대를 이야기한다":
                $ b_love += 2
                b "저도요! 새로운 사람들도 만나고, 여러 추억을 남길 수 있겠죠."
                hide b_base
            "대학 생활에 대한 설렘을 이야기한다":
                $ b_love += 2
                b "저도요! 대학 생활에서 뭔가 멋진 경험을 하고 싶었거든요."
                hide b_base
    else:
        #심장박동 내려가면
        "조용히 자리에 앉았다"
        $ b_love -= 2
        hide b_base
        "나는 살짝 긴장한 마음을 추스르며 조용히 자리에 앉았다."
        "주변을 둘러보며, 점차 채워지는 동아리 방의 분위기에 마음이 두근거렸다."
        menu:
            "옆 사람에게 조용히 인사를 건넨다":
                $ b_love -= 1
                "옆에 앉은 동급생이 나를 보며 미소를 지어주었다."
            "그저 가만히 자리에 앉아있다":
                "나는 아직 어색함을 느끼며 주변을 둘러보았다."
        
    # 카메라 조작 중인 선배와 조우
    "곧이어 동아리 방은 여러 신입생과 기존 멤버들로 가득 찼다."
    "모두가 자리를 잡고 앉자, 동아리 장인 선배가 앞으로 나와 우리를 환영했다."

    # 동아리 환영식
    show a_base at center with dissolve
    a "안녕, 모두들! 우리 사진 동아리에 온 걸 환영해."
    a "나는 동아리 장이고, 앞으로 잘 부탁할게!"
    
    "환영식은 간단한 소개와 앞으로의 활동 계획, 그리고 동아리의 전통에 대한 설명으로 이루어졌다."
    "여러 선배들이 돌아가면서 자신들의 경험과 추억을 공유하며 분위기를 풀어주었다."
    
    
    $ send_emotions = analyze_emotion(new_round_number, scene)
    $ neutral = send_emotions["neutral"]
    $ happy = send_emotions["happy"]
    s "현재 감정 분석중입니다.."
    if happy >= neutral:
        #표정 좋으면
        "환영식에 집중한다"
        $ a_love += 1
        "선배들의 이야기를 들으며 사진 동아리가 얼마나 다양한 활동을 해왔는지 알 수 있었다."
        "가끔 웃음이 터지기도 하고, 진지한 순간도 이어지며 분위기는 점점 훈훈해졌다."
        menu:
            "선배들의 경험에 감동한다":
                $ a_love += 1
                "사진에 대한 열정이 이렇게 강렬할 줄 몰랐다."
            "활동 계획에 대해 질문한다":
                $ a_love += 2
                a "좋은 질문이야! 다음 달에는 캠퍼스 사진 전시회를 열 계획이야."
        #표정 안좋으면
    else:
        "옆의 동급생들과 작은 얘기를 나눈다"
        $ a_love -= 1
        "옆에 앉은 동급생들과 가볍게 속삭이며 인사를 나누었다."
        "동아리 장의 이야기를 들으면서도, 서로의 기대와 설렘을 공유했다."
        menu:
            "동아리에 대해 얘기한다":
                "옆에 앉은 서현와 동아리 활동에 대한 기대를 이야기했다."
                $ b_love += 2
            "친근하게 서로를 알아간다":
                "이름과 전공을 물으며 옆에 앉은 동급생들과 친근하게 대화를 나누었다."

    # 동아리 장의 인기 비밀 발견
    "이야기가 진행되는 도중, 뒤편에서 누군가 작은 목소리로 속삭였다."
    unknown "저 선배, 축제 때 가장 예쁜 선배로 유명하잖아. 몰랐어?"
    
    "그 말에 나는 다시 동아리 장을 바라보았다. 댄스 공연에서 이미 강렬한 인상을 주었던 선배였지만, 그녀가 그렇게 유명한 인물인 줄은 몰랐다."
    "선배가 주목받는 이유가 단순한 외모 때문이 아니라, 그녀의 자신감과 열정이 만들어낸 것이란 생각이 들었다."
    hide a_base
    # C 동급생과의 만남
    "환영식이 끝난 후, 다른 동아리 멤버들이 자유롭게 이야기를 나누고 있었다."
    "그때, 방 구석에서 혼자 앉아 있는 한 신입생이 눈에 띄었다. 동급생으로 보였고, 다른 사람들과 어울리지 않고 조용히 있는 모습이 조금 특이했다."
    menu:
        #심장박동이 오르면

        "???에게 다가가 인사를 건넨다":
            scene dongC
            $ c_love += 5
            "나는 용기를 내어 그에게 다가가 인사를 건넸다."
            show c_lol
            c "…아, 안녕하세요."
            "그녀는 잠시 놀란 듯했지만, 차분한 표정으로 대답했다. 그의 말투에는 어딘가 신비로운 분위기가 감돌았다."
            $ test = send_to_raspberry_pi(new_round_number, scene) # 심박수 측정 호출
            s "현재 심장박동 측정중입니다 높아지면 어떤 대사가 나오고 낮아지면 어떤게 나옴니다."
            "이곳에서 앞으로의 내 삶이 어떻게 바뀔지 상상하니 가슴이 두근거렸다."
            if test['rising'] == True:
                "서연에게 동아리 활동에 대한 생각을 물어본다"
                hide c_lol
                show c_worr
                $ c_love += 2
                c "솔직히 아직은 잘 모르겠어요. 그냥... 분위기를 느껴보고 싶었을 뿐이에요."
                "서연의 대답은 마치 자신이 어떤 정체성을 찾고 있는 것처럼 느껴졌다."
                hide c_worr
                scene dongai
            else:
                "서연에게 카메라에 대해 물어본다"
                $ c_love += 1
                c "아직 카메라는 잘 모르겠어요. 배워가며 생각해보려구요."
                "서연는 약간의 호기심을 보이며 말을 이어갔다."
                hide c_lol
                scene dongai
        #심장박동이 내려가면
        "혼자 있게 내버려둔다":
            $ c_love -= 1
            "그가 혼자 있고 싶어 하는 것 같아서 굳이 다가가지 않고 멀리서 지켜보기로 했다."
            "그러나 그의 차분한 분위기와 시선이 계속 신경 쓰였다."
            $ test = send_to_raspberry_pi(new_round_number, scene) # 심박수 측정 호출
            if test['rising'] == True:
                "서연에게 인사를 건네본다"
                scene dongC
                show c_lol
                $ c_love += 3
                c "…아, 안녕하세요."
                "그의 말투에는 어딘가 신비로운 분위기가 감돌았다."
                "마치 평범하지않은 신입생같다."
                hide c_lol
                scene dongai
            else:
                "방을 조용히 둘러본다"
                "나는 동아리 방의 분위기를 차분히 느끼며, 앞으로의 활동을 기대하기 시작했다."
                $ c_love -= 1
    "모든 것이 새롭고 설레는 대학 생활 속에서, 앞으로 어떤 이야기가 펼쳐질지 기대가 되는 마음으로 집으로 향했다."
    stop music fadeout 2.5
    scene black
    "..."
    ".."
    "."
    jump day_3

label day_3:
    $ scene = 3
    "다음날이 되었다"
    scene hclass
    play music "audio/bgm/base3_music.mp3"
    "학교에 모든 수업이 끝나고 동아리 모임으로 향했다"
    
    # 동아리 모임 시작
    scene dongai
    "오늘은 단체 사진을 찍는다고 해서 멤버들이 하나둘 동아리 방에 모여들었다."
    
    # 단체 사진 촬영 이벤트
    a "자, 다들 준비됐지? 단체 사진은 우리 동아리의 전통이야."
    b "맞아요. 매년 이렇게 사진을 찍어서 추억을 남기거든요."
    scene camera1
    "나는 멤버들과 함께 사진 촬영 준비를 했다. 카메라 앞에 서니 조금 긴장이 되었다."
    play sound "audio/sound/Storytelling.mp3"
    call open_camera_page from _call_open_camera_page #카메라 불러오기
    "찰칵! 카메라 셔터 소리와 함께 모두의 얼굴이 사진으로 남았다."
    scene dongai
    # 동아리 여행 공지
    show a_base
    a "그리고 중요한 공지 하나 더! 다음 주 동아리 여행 간다!"
    if danhan == 1:
        "저번에 들었던 단합 모임이다."
    b "우와, 여행이요? 어디로 가요?"
    a "이번엔 근교의 산으로 가기로 했어. 멋진 풍경 사진도 찍고 재미있게 놀자!"
    hide a_base
    "동아리 멤버들 사이에서 기대감이 가득한 목소리가 터져 나왔다."
    
    # 쇼핑 관련 이벤트 시작
    "모임이 끝난 후, 나는 집으로 가려던 참에 아린 선배가 다가왔다."
    show a_base at left
    a "[pn], 여행 전에 필요한 옷이나 준비물이 있으면 같이 사러 갈래?"
    
    menu:
        "제안을 수락한다":
            "나는 제안을 수락했다."
            $ a_love += 2
            a "좋아! 그럼 내일 백화점에서 만나자!"
            hide a_base 
            stop music fadeout 2.5
            jump a_date_shopping

        "제안을 거절한다":
            "나는 미안하다고 말하며 제안을 정중히 거절했다."
            a "아쉽지만 어쩔 수 없지. 그래도 준비 잘 해!"
            hide a_base 
            $ a_love -= 2
            stop music fadeout 2.5
            jump b_encounter

label a_date_shopping:
    # A와 쇼핑
    scene black
    "다음 날, 나는 선배와 함께 백화점으로 갔다."
    play music "audio/bgm/departmentstore.mp3"
    scene backha
    show a_base
    a "여기 정말 크다! 뭐부터 볼까?"
    "우리는 함께 옷가게를 돌아다니며 서로 어울리는 옷을 추천하기도 하고, 웃으며 시간을 보냈다."
    a "이거 한번 입어볼래?"
    menu:
        "선배가 추천한 옷을 입어본다":
            $ a_love += 1
            "나는 선배가 추천한 옷을 입어보기로 했다."
            a "와, 너한테 정말 잘 어울려! 완전 멋진데?"
            "선배의 칭찬에 조금 부끄러웠지만 기분이 나쁘진 않았다."

        "내가 선배에게 어울리는 옷을 추천한다":
            $ a_love += 2
            "나는 선배에게 어울릴 것 같은 옷을 추천했다."
            a "이거? 한번 입어볼게!"
            hide a_base
            "아린선배가 옷을 갈아입고 나오자, 마치 모델처럼 눈길을 끌었다."
            show a_backha at center
            a "어때? 괜찮아?"
            "나는 고개를 끄덕이며 칭찬했다."
            $ a_back = 1;
            hide a_backha

    "A와 함께한 쇼핑은 즐거웠고, 우리의 사이도 조금 더 가까워진 것 같았다."
    jump day_3_end

label b_encounter:
    stop music fadeout 2.5
    scene haha
    play music "audio/bgm/alley.mp3"
    # B와의 우연한 만남
    "오늘의 일과를 끝내고"
    "하교 도중, 나는 우연히 서현과 마주쳤다."
    show b_lol
    b "어? 너도 집에 가는 중이야?"
    "나는 고개를 끄덕였다. 그러자 서현이 제안했다."
    b "마침 잘 됐다! 나도 옷 좀 사려고 했는데, 같이 갈래?"
    
    menu:
        "제안을 수락한다":
            $ b_love += 3
            "나는 서현의 제안을 수락했다."
            b "좋아, 그럼 지금 가자!"   
            hide b_lol
            jump b_date_shopping

        "제안을 거절한다":
            $ b_love -= 2
            "나는 미안하다고 말하며 서현의 제안을 거절했다."
            b "아, 알겠어. 그럼 다음에 또 보자!"
            hide b_lol dissolve
            jump c_observation

label b_date_shopping:
    # B와 쇼핑
    stop music fadeout 2.5
    scene black
    "나는 서현과 함께 백화점으로 향했다."
    scene backha
    play music "audio/bgm/Bdepartmentstore.mp3"
    b "와, 여기는 언제 와도 신기해! 뭐부터 볼까?"
    "우리는 함께 여러 매장을 돌아다니며 쇼핑을 즐겼다."
    
    menu:
        "서현이 고른 옷을 칭찬한다":
            $ b_love += 2
            "나는 서현이 고른 옷을 보고 칭찬했다."
            b "정말? 나한테 어울려? 고마워!"
            "서현은 기뻐하며 옷을 구입했다."

        "내가 서현에게 어울리는 옷을 추천한다":
            $ b_love += 3
            "나는 서현에게 어울릴 것 같은 옷을 추천했다."
            show b_backha
            b "오, 이거 괜찮은데? 너 센스 좋다!"
            "서현은 내 추천을 받아들여 옷을 입어보고 만족스러워했다."
            $ b_back = 1;
            hide b_backha

    "서현과 함께한 쇼핑은 유쾌했고, 우리 사이도 더욱 가까워진 것 같았다."
    jump day_3_end

label c_observation:
    # C의 관찰 이벤트
    stop music fadeout 2.5
    scene hidehaha 
    play music "audio/bgm/C_alley"
    $ c_love += 5
    "나는 혼자 집으로 가는 길에 익숙한 시선을 느꼈다."
    "앞을 자세히보니, 멀리서 서연이 조용히 나를 지켜보고 있었다."
    "그는 눈이 마주치자 약간 당황한 듯 서둘러 자리를 떠났다."
    "그 모습이 묘하게 마음에 남았다."

    "서연이 나를 신경 쓰고 있다는 생각에, 괜히 가슴이 두근거렸다."
    jump day_3_end

label day_3_end:
    "그렇게 동아리 모임이 끝난 하루가 저물어갔다."
    stop music fadeout 2.5
    scene black
    "점점 더 흥미로운 일들이 일어날 것만 같았다."
    "이런저런 생각끝에 잠에 들었다."
    "..."
    ".."
    "."
    jump chapter_4




label chapter_4:
    $ scene = 4
    "다음 주가 되었다"
    # 여행 시작
    play music  "audio/bgm/travel.mp3"
    "오늘은 동아리 여행 날! 동아리 멤버들과 함께 봉고차에 탑승하여, 자연이 아름답기로 유명한 산으로 향했다."
    scene mount
    show bongo at left:
        xalign 0.0  # x축의 0.0은 화면의 왼쪽
        yalign 1.0  # 화면 중간에 표시
    "차 안에서는 모두 웃고 떠들며 여행의 시작을 기쁘게 맞이했다."

    # 대여한 봉고차
    "차가 산을 향해 달리는 동안 창밖으로 펼쳐지는 풍경이 아름다웠다."
    play sound "audio/sound/Car.mp3"
    show bongo:
        linear 4.0 xalign 1.0 
    "모두가 기분 좋게 웃으며 대화를 나누고 있었다."
    
    
    # 산에 도착
    hide bongo
    stop music fadeout 2.5
    play music "audio/bgm/Nature.mp3"
    scene realmount
    "도착한 산은 정말 아름다웠다. 푸른 숲과 맑은 공기가 나를 맞이했다."
    "우리는 다같이 산 정상으로 올라가기로 했다."

    # 산 정상까지 올라가는 길
    "산을 올라가면서 우리는 서로 중간중간 사진을 찍어주기도 하고, 재미있는 이야기를 나누기도 했다."
    "사진 찍을 때마다 누군가가 셔터를 누르고, 서로의 웃는 얼굴을 남겼다."
    if a_back == 1:
        show a_backha at left with dissolve
    else:
        show a_base at left with dissolve
    a "곧 정상이야 조금만 더 힘내!"
    
    if b_back == 1:
        show b_backha at right with dissolve:
            size (900,1100)
            yalign -1.0
    else:
        show b_base at right with dissolve
            
    b "얼른 올라가서 쉬자 ㅠㅠ"
    if b_back == 1:
        hide b_backha 
    else:
        hide b_base
        
    if a_back == 1:
        hide a_backha 
    else:
        hide a_base
    # 정상에서 단체 사진
    stop music fadeout 2.5
    scene highmount
    
    "우리는 마침내 산 정상에 도달했다."
    play music "audio/bgm/down.mp3"
    "탁 트인 풍경과 함께 우리는 기념사진을 찍자는 분위기였다."
    
    menu:
        "단체사진을 찍는다":
            $ scene = "4-2"
            "모두 사진찍을 준비를 했다."
            play sound "audio/sound/Storytelling.mp3"
            "찰칵 소리가 들렸다"
            call open_camera_page
            "단체 사진이 정말 마음에 들었다. 모두 함께 웃는 모습이 참 보기 좋았다."
            scene highmount
            "사진을 보고 나서 서로 웃으며 내려가기 시작했다."
            $ danchan = 1
        
        "무시하고 셀카를 찍는다":
            $ a_love -= 3
            $ b_love -= 2
            $ c_love += 3
            play sound "audio/sound/Storytelling.mp3"
            call open_camera_page #카메라 불러오기
            "내가 찍은 셀카가 잘 나온 것 같아 뿌듯해했다."
            "사진을 찍고 모두 기분 좋게 정상에서 내려왔다."
            
            

    # 산에서 내려가기
    "우리는 산에서 내려와 다 같이 밥을 먹으러 가기로 했다."
    "배가 고파진 우리는 근처 식당으로 향했다."

    scene restaurant
    "식당에서 우리는 맛있는 음식을 먹으며 즐거운 시간을 보냈다."
    if danchan == 1:
        "다들 여행을 만족스러워했다."
    else:
        "단체사진을 못 찍은걸 매우 아쉬워했지만,"
        "다들 여행을 만족스러워했다."

    # 숙소 도착
    scene suk
    
    "숙소에 도착한 우리는 각자 짐을 풀고 잠시 휴식을 취했다."
    stop music fadeout 2.5
    


    # C의 고백 이벤트 (C의 호감도가 높을 경우)
    if c_love > a_love and c_love > b_love:
        c "잠깐, 나랑 얘기 좀 할래?"
        play music "audio/bgm/c_music.mp3"
        "서연은 나를 조용히 불러 숙소 앞에서 나와 이야기를 나누었다."
        scene gii
        show c_shy
        c "사실, 오늘 너에게 고백하고 싶었어. 내가 너에게 느끼는 감정은 그냥 친구 이상의 거야."
        c "너도 나랑 같은 마음이었으면 좋겠어..."
        "그는 수줍게 고백했다. 나는 순간 마음이 두근거렸다."
        menu:
            "서연의 고백을 받아들인다":
                
                "나는 서연의 고백을 받아들였다."
                "서연는 정말 기쁜 표정으로 나를 바라보았다."
                hide c_shy
                show c_cute
                c "정말 고마워. 이제부터 우리 둘이 더 가까워지자!"
                hide c_cute
                $ c_cup = 1
            "서연의 고백을 거절한다":
                "나는 서연의 고백을 정중히 거절했다."
                stop music
                hide c_shy
                show c_sad
                c "알겠어, 네가 부담되지 않게 해줄게."
                "서연은 천생연분을 놓쳐"
                "울고있는 사람같았다."

    # A의 고백 이벤트 (A의 호감도가 높을 경우)
    elif a_love > b_love and a_love > c_love:
        a "잠깐 나와줄래? 숙소 앞에서 이야기하고 싶은 게 있어."
        "아린은 나를 숙소 앞에 불러 조용히 말했다."
        play music "audio/bgm/a_music.mp3"
        scene sukfront
        show a_shy
        a "사실 내가 네게 마음이 있었어. 우리가 동아리에서 친해지면서, 점점 네가 좋아졌어."
        a "이제 나의 마음을 알아줬으면 좋겠어."
        "아린은 고백을 하며 나를 바라봤다. 나는 조금 놀라웠지만 마음이 따뜻해졌다."
        menu:
            "아린의 고백을 받아들인다":
                "나는 아린의 고백을 받아들였다."
                a "정말?! 이제부터 우리 둘이 더 많이 함께 보내자!"
                $ a_cup = 1

            "아린의 고백을 거절한다":
                hide a_shy
                stop music
                "나는 아린의 고백을 거절했다."
                show a_sad
                a "알겠어. 부담 가지지 말고, 그래도 좋은 선후배로 계속 지내자!"
                "아린은 고백을 받아들일 수 없다는 내 말을 이해하고 대화를 마쳤다."

    # B의 고백 이벤트 (B의 호감도가 높을 경우)
    elif b_love > a_love and b_love > c_love:
        scene macdow
        play music "audio/bgm/b_music.mp3"
        show goback1:
            align (0.5, 0.2)
        b "나 오늘... 너에게 할 말이 있어."
        hide goback1
        show goback2:
            align (0.5, 0.2)
        b "카톡으로 할게."
        "서현은 나에게 카톡 메시지를 보내며 고백을 전했다."
        hide goback2
        show goback3:
            align (0.5, 0.2)
        b "사실, 나 너 좋아해."
        hide goback3
        show goback4:
            align (0.5, 0.2)
        b "네가 나에게 특별한 사람이라는 걸 알았어."
        "메시지로 고백을 전해온 서현의 고백을 받고 나는 마음이 흔들렸다."
        menu:
            "서현의 고백을 받아들인다":
                hide goback4
                show goback:
                    align (0.5, 0.2)
                "나는 서현의 고백을 받아들였다."
                hide goback
                show gobackwin:
                    align (0.5, 0.2)
                b "정말?? 이제부터 우리 사귀는거다!!"
                $ b_cup = 1
                hide gobackwin
            "서현의 고백을 거절한다":
                hide goback4
                show gobackv2:
                    align (0.5, 0.2)
                stop music
                "나는 서현의 고백을 거절했다."
                hide gobackv2
                show gobacklose:
                    align (0.5, 0.2)
                b "알겠어. 그래도 계속 친구로 잘 지내자"
                "서현은 내 거절을 아쉬워했다."
                hide gobacklose
    else:
        "아무 일이 일어나지않고"
        "서로 즐겁게 떠들며 해는 저물어갔다."

    # 샤워 후 잠
    stop music fadeout 2.5
    scene black
    "저녁이 되고, 우리는 각자 샤워를 하고 잠을 자러 갔다."
    "하루의 피로를 풀고, 곧 잠이 들었다."

    jump chapter_5







label chapter_5:
    $ scene = 5
    "다음날이 되었다"
    "오늘은 마지막 동아리날이다."
    play music "audio/bgm/festival.mp3"
    "기대감을 갖고 학교로 출발했다."

    # 학교에서 축제 준비
    "마지막으로, 나는 오늘의 기억을 간직하기 위해 '인생네컷' 촬영을 하기로 했다."
    scene photo_booth
    a "얘들아 웃어!"
    b "김치!"
    c "ㄱ,김치"
    play sound "audio/sound/Storytelling.mp3"
    call open_camera_page
    "촬영을 마친 후, 사진을 보며 그동안의 추억이 떠올랐다. 부스에서 웃고 떠들던 시간, 그리고 동아리 친구들과의 따뜻한 순간들이 떠오른다."



    # 추억 회상
    scene black
    # END
    # if happy-page == 1:
    #     show page1
    # elif happy-page == 2:
    #     show page1
    # elif happy-page == 3:
    #     show page1
    # elif happy-page == 4:
    #     show page1
    # elif happy-page == 5:
    #     show page1
    # elif happy-page == 6:
    #     show page1


    # if heart-page == 1:
    #     show page1
    # elif heart-page == 2:
    #     show page2
    # elif heart-page == 3:
    #     show page3
    # elif heart-page == 4:
    #     show page4
    # elif heart-page == 5:
    #     show page5
    # elif heart-page == 6:
    #     show page6
    call all_picture from _call_all_picture
    "오늘의 축제도 끝이 나고, 나는 다시 일상으로 돌아갔다."
    "하지만 그 날의 추억은 항상 내 마음 속에 남아 있을 것이다."

    stop music fadeout 2.5
    return





label long_first_day:
    $ scene = 1
    scene black
    #영상 있으면 만들기
    # Chapter 1: 입학식
    scene black
    s "이 게임은 사용자의 심박수의 증가&감소에따라 선택지가 달라지니 이 포인트를 잘 활용해서 플레이하시길 바랍니다."
    s "재밌게 플레이해주세요."      
    $ game_start = create_new_round() #라운드 불러오기
    $ new_round_number = game_start['new_round'] #라운드 값 함수에 저장
    
    "[new_round_number]번쨰 회차가 생성되었습니다"
    scene bg_school_event with dissolve
    play music "audio/bgm/base_music.mp3"
    "대학 입구에 도착하니, 웅장한 교문이 나를 맞이했다."


    # call open_camera_page #카메라 불러오기
    # $ send_emotions = analyze_emotion(new_round_number, scene) #표정불러오기
    #안써도됨# $ send_emotions_text = json.dumps(send_emotions, ensure_ascii=False).replace("{", "{{").replace("}", "}}")
    #안써도됨# "응답 데이터: [send_emotions_text]"

    # $ test = send_to_raspberry_pi(round_id, page) # 심박수 측정 호출



    
    "이곳에서 앞으로의 내 삶이 어떻게 바뀔지 상상하니 가슴이 두근거렸다."
    "새로운 시작에 대한 설렘과 약간의 두려움이 뒤섞인 복잡한 감정이 밀려왔다."


    scene school_event
    "입구를 지나니 봄의 따뜻한 햇살이 비치는 교정에 부스들이 가득 펼쳐져 있었다."
    "신입생인 나는 새로 시작하는 대학 생활에 설레기도 하고, 한편으론 낯선 분위기에 긴장도 되었다."
    
    # 친구 등장
    show friend at Transform(xalign=0.8, yalign=0.5) with dissolve:
        yalign 1.0

    friend "야, 무슨 동아리 들어갈 거야? 부스들 보니까 진짜 다양하더라."
    
    "친구의 말에 나는 주변을 둘러보았다. 각양각색의 동아리들이 자신들의 활동을 자랑하고 있었다."
    "스포츠, 학술, 문화... 선택지가 많아 어떤 동아리를 들어가야 할지 고민이 깊어졌다."


    friend "야 나 장유진이 불러서 나중에 보자!!"

    hide friend with dissolve

    "친구는 갑작스럽게 어디론가 뛰어갔다. 나는 홀로 남아 부스를 둘러보며 천천히 걸었다."

    scene school_buss
    "우연히 어떠한 부스를 지나고있었다."

    "누군가 나에게 말을 걸었다."

    # 선배 등장
    show a_base at move_to_left with dissolve
    q "안녕! 신입생 맞지? 동아리 알아보고 있어?"

    # 첫 대화 선택지
    s "현재 감정 분석중입니다.. 웃으시면 '조금 둘러보고 있어요'라는 대사가 나오고 무표정이면 '네, 하지만 뭐가 좋을지 모르겠네요'라는 대사가 나옴니다."
    $ send_emotions = analyze_emotion(new_round_number, scene)
    $ neutral = send_emotions["neutral"]
    $ happy = send_emotions["happy"]
    if happy >= neutral:
        #표정이 좋으면
        "조금 둘러보고 있어요"
        show a_base at left with move
        "부스 구경 중이던 내게 선배가 친근하게 다가왔다."
        a "그럼 우리 사진 동아리는 어때? 다양한 활동도 많고 재밌어!"
        "나는 사진 동아리에 대한 이야기를 들으며 조금씩 흥미가 생겼다."
        menu:
            "사진 동아리가 정말 그렇게 재미있나요?":
                $ a_love += 3
                "선배는 눈을 빛내며 고개를 끄덕였다."
                a "그럼! 단순히 사진 찍는 것만이 아니라, 전시회도 열고 전국 대회도 참여해!"
                "선배의 열정적인 설명에 나는 점점 더 끌렸다."
            
            "괜찮아 보이네요, 참가할게요.":
                $ a_love += 2
                "나는 사진 동아리에 참가하기로 결정했다."
                a "좋아! 그럼 참가서 작성해줘. 잘 생각했어!"
                "내가 참가서를 작성하는 동안 선배는 조언과 격려의 말을 아끼지 않았다."
    else:            
        #표정이 안좋으면
        "네, 하지만 뭐가 좋을지 모르겠네요"
        "막연히 둘러보고 있던 내게 선배가 추천을 시작했다."
        a "음, 사진 동아리 어때? 여행도 가고 추억도 남길 수 있어."
        menu:
            "사진 동아리 말고 다른 동아리도 추천해 주실 수 있나요?":
                $ a_love -= 3
                a "흠... 물론 다른 동아리도 많지. 하지만 사진 동아리는 너의 젊음을 기록하는 데 딱이야."
                "나는 선배가 말하는 '기록'이라는 단어가 마음에 와닿았다."
            
            "다른 동아리도 둘러보고 결정할게요.":
                $ a_love -= 2
                a "알겠어. 그래도 마음이 바뀌면 언제든 우리 동아리로 와!"
                "나는 아직 결정을 내리지 않고 다른 부스를 둘러보기로 했다."

    "나는 선배의 말에 이끌려 사진 동아리에 흥미가 생겼다."
    #extend 
    "그렇기에 나는 사진동아리에 들어가겠다고 다짐했다"
    # 동아리 가입을 권유하며 선택지를 제공
    
    a "좋아! 관심 있다면 참가서 작성하고 가. 네가 관심 있으면 나중에 후회 안 할 거야!"
    menu:
        "사진 동아리에 가입한다":
            hide a_base
            show a_shy at left
            $ a_love += 1
            a "잘 생각했어! 이거 꽉 채워서 작성해줘!"
            
            
            
            #이름적는 페이지
            show report at center
            a "여기에 이름을 적어줘!"
            $ set_player_name()
            "동아리 참가서를 작성하며 선배의 기대 어린 눈빛을 느낄 수 있었다."
            # 가입 이유 확인 선택지
            "[pn].."
            "작성을 마치자 선배가 질문했다."

            a "근데 정말 하고 싶어서 작성한 거 맞아? 잠깐의 호기심만으로는 힘들 수도 있어."
            menu:
                "네, 하고 싶어서 작성했어요":
                    $ a_love += 2
                    "내가 정말 이 동아리에 기대가 컸다는 생각에 진심을 담아 대답했다."
                    a "좋아, 그런 마음이라면 반드시 우리 동아리에 잘 어울릴 거야!"
                    "선배는 만족스러운 미소를 지으며 내 손을 힘차게 잡아주었다."
                
                "아직 잘 모르겠지만, 해보고 결정해볼게요":
                    $ a_love += 1
                    a "그래, 해보면서 점차 느껴봐. 사진 찍는 즐거움은 경험해 봐야 알 수 있거든."
                    "선배는 격려의 말과 함께 곧 열릴 첫 모임을 기대하라며 내 어깨를 두드렸다."
            
            a "첫 모임은 다음 주 수요일 오후 6시! 장소는 동아리 방이니까 잊지 마!"
    # 집으로 가는 길
    # @@@@@@@@@@@@@@@@@@@@@@@@@
    scene dengi
    "그렇게 입학식이 끝나고 집으로 가는 길에 들뜬 마음을 진정시키며 캠퍼스를 걷고 있었다."
    play sound "audio/sound/CheerSound.mp3"
    "갑자기 사람들이 모여서 환호하는 소리가 들려 발걸음을 멈췄다."
    "사람들이 모여 있는 쪽으로 다가가 보니, 무대 위에서 댄스 공연이 한창이었다."
    "화려한 춤과 함께 무대를 채운 그들 중에서도 유독 눈에 띄는 선배가 있었다."
    
    scene muda 
    "그녀는 강렬한 눈빛으로 무대를 지배하며, 멋진 춤 동작을 선보이고 있었다."
    "나는 그 선배가 자꾸만 눈에 들어와 공연이 끝날 때까지 시선을 떼지 못했다."
    
    # 선배 정체 확인
    "공연이 끝난 후, 옆에 있던 친구가 그녀를 가리키며 말했다."
    friend "저 선배, 우리 학교에서 엄청 유명해!"
    friend "듣자 하니, 네가 가입한 사진 동아리의 동아리 아린 선배님이래!"
    
    "동아리 장이자, 그 화려한 무대 위의 주인공… 뭔가 묘하게 가슴이 두근거렸다."
    "이제 다음 주 첫 모임이 더욱 기다려지는 걸 느끼며, 나는 집으로 향했다."
    stop music fadeout 2.5
    scene black
    "..."
    ".."
    "."

    jump long_chapter_2

# Chapter 2: 첫 동아리 모임
label long_chapter_2:
    $ scene = 2
    "다음날이 되었다"
    play music "audio/bgm/base2_music.mp3"
    scene hclass
    "학교에 모든 수업이 끝나고 동아리 모임으로 향했다"
    scene class
    "동아리 앞에 도착했다."
    scene dongai
    play sound "audio/sound/DoorOpen.mp3"
    
    "드디어 사진 동아리의 첫 모임 날이 되었다. 동아리 방에 들어서자 여러 신입생과 선배들이 모여 있었다."
    
    # B 등장
    show b_base at right with dissolve
    b "안녕하세요! 혹시 여기가 사진 동아리 맞나요?"
    
    "들어오는 나와 동시에 동기인 서현이가 반갑게 인사하며 동아리 방에 들어왔다."
    
    
    "이곳에서 앞으로의 내 삶이 어떻게 바뀔지 상상하니 가슴이 두근거렸다."
    s "현재 심장박동 분석중입니다.. 높아지면 '서현에게 친근하게 인사를 건냈다'라는 선택지로 이동하고 낮아지면 '조용히 자리에 앉았다'라는 선택지로 이동합니다."
    $ test = send_to_raspberry_pi(new_round_number, scene) # 심박수 측정 호출
    if test['rising'] == True:
        #심장박동 오르면
        "서현에게 친근하게 인사를 건냈다"
        "나 역시 그에게 가볍게 손을 흔들며 인사를 건넸다."
        $ b_love += 3
        menu:
            "동아리에 대한 기대를 이야기한다":
                $ b_love += 2
                b "저도요! 새로운 사람들도 만나고, 여러 추억을 남길 수 있겠죠."
                hide b_base
            "대학 생활에 대한 설렘을 이야기한다":
                $ b_love += 2
                b "저도요! 대학 생활에서 뭔가 멋진 경험을 하고 싶었거든요."
                hide b_base
    else:
        #심장박동 내려가면
        "조용히 자리에 앉았다"
        $ b_love -= 2
        hide b_base
        "나는 살짝 긴장한 마음을 추스르며 조용히 자리에 앉았다."
        "주변을 둘러보며, 점차 채워지는 동아리 방의 분위기에 마음이 두근거렸다."
        menu:
            "옆 사람에게 조용히 인사를 건넨다":
                $ b_love -= 1
                "옆에 앉은 동급생이 나를 보며 미소를 지어주었다."
            "그저 가만히 자리에 앉아있다":
                "나는 아직 어색함을 느끼며 주변을 둘러보았다."
        
    # 카메라 조작 중인 선배와 조우
    scene chdongai
    show camera_senior at left with dissolve
    "한쪽에서는 선배가 카메라를 만지며 세팅 중이었다."
    "내가 궁금한 표정으로 바라보자 선배가 미소를 지으며 말을 걸었다."
    
    camera_senior "신입생이구나? 카메라에 관심 있니?"
    #얼굴
    menu:
        "네, 배우고 싶어요.":
            "선배는 흐뭇한 표정으로 고개를 끄덕였다."
            camera_senior "좋아, 앞으로 기초부터 차근차근 알려줄 테니까 기대해!"
            menu:
                "어떤 활동을 하는지 물어본다":
                    camera_senior "촬영뿐 아니라, 전시회나 외부 활동도 많이 있어. 분명 재밌을 거야!"
                "자신의 카메라에 대해 묻는다":
                    camera_senior "이건 내가 오래 쓰던 카메라야. 너도 차츰 자신만의 카메라를 갖게 될 거야."

        "아직 잘 모르겠어요.":
            camera_senior "괜찮아, 해보면서 배워가는 거지. 처음엔 누구나 그렇거든."
            "선배는 내게 친근하게 다가오며 부담감을 덜어주려는 듯 격려의 말을 해주었다."
            menu:
                "감사 인사를 한다":
                    "나는 선배에게 감사의 미소를 보냈다."
                "조용히 고개만 끄덕인다":
                    "나는 고개를 끄덕이며 선배의 격려를 마음속에 담았다."

    # 동아리 멤버들이 다 모임
    hide camera_senior
    scene dongai
    "곧이어 동아리 방은 여러 신입생과 기존 멤버들로 가득 찼다."
    "모두가 자리를 잡고 앉자, 동아리 장인 선배가 앞으로 나와 우리를 환영했다."

    # 동아리 환영식
    show a_base at center with dissolve
    a "안녕, 모두들! 우리 사진 동아리에 온 걸 환영해."
    a "나는 동아리 장이고, 앞으로 잘 부탁할게!"
    
    "환영식은 간단한 소개와 앞으로의 활동 계획, 그리고 동아리의 전통에 대한 설명으로 이루어졌다."
    "여러 선배들이 돌아가면서 자신들의 경험과 추억을 공유하며 분위기를 풀어주었다."
    s "현재 감정 분석중입니다.."
    $ send_emotions = analyze_emotion(new_round_number, scene)
    $ neutral = send_emotions["neutral"]
    $ happy = send_emotions["happy"]
    if happy >= neutral:
        #표정 좋으면
        "환영식에 집중한다"
        $ a_love += 1
        "선배들의 이야기를 들으며 사진 동아리가 얼마나 다양한 활동을 해왔는지 알 수 있었다."
        "가끔 웃음이 터지기도 하고, 진지한 순간도 이어지며 분위기는 점점 훈훈해졌다."
        menu:
            "선배들의 경험에 감동한다":
                $ a_love += 1
                "사진에 대한 열정이 이렇게 강렬할 줄 몰랐다."
            "활동 계획에 대해 질문한다":
                $ a_love += 2
                a "좋은 질문이야! 다음 달에는 캠퍼스 사진 전시회를 열 계획이야."
        #표정 안좋으면
    else:
        "옆의 동급생들과 작은 얘기를 나눈다"
        $ a_love -= 1
        "옆에 앉은 동급생들과 가볍게 속삭이며 인사를 나누었다."
        "동아리 장의 이야기를 들으면서도, 서로의 기대와 설렘을 공유했다."
        menu:
            "동아리에 대해 얘기한다":
                "옆에 앉은 서현와 동아리 활동에 대한 기대를 이야기했다."
                $ b_love += 2
            "친근하게 서로를 알아간다":
                "이름과 전공을 물으며 옆에 앉은 동급생들과 친근하게 대화를 나누었다."

    # 동아리 장의 인기 비밀 발견
    "이야기가 진행되는 도중, 뒤편에서 누군가 작은 목소리로 속삭였다."
    unknown "저 선배, 축제 때 가장 예쁜 선배로 유명하잖아. 몰랐어?"
    
    "그 말에 나는 다시 동아리 장을 바라보았다. 댄스 공연에서 이미 강렬한 인상을 주었던 선배였지만, 그녀가 그렇게 유명한 인물인 줄은 몰랐다."
    "선배가 주목받는 이유가 단순한 외모 때문이 아니라, 그녀의 자신감과 열정이 만들어낸 것이란 생각이 들었다."
    hide a_base
    # C 동급생과의 만남
    "환영식이 끝난 후, 다른 동아리 멤버들이 자유롭게 이야기를 나누고 있었다."
    "그때, 방 구석에서 혼자 앉아 있는 한 신입생이 눈에 띄었다. 동급생으로 보였고, 다른 사람들과 어울리지 않고 조용히 있는 모습이 조금 특이했다."
    menu:
        #심장박동이 오르면

        "???에게 다가가 인사를 건넨다":
            scene dongC
            $ c_love += 5
            "나는 용기를 내어 그에게 다가가 인사를 건넸다."
            show c_lol
            c "…아, 안녕하세요."
            "그녀는 잠시 놀란 듯했지만, 차분한 표정으로 대답했다. 그의 말투에는 어딘가 신비로운 분위기가 감돌았다."
            $ test = send_to_raspberry_pi(new_round_number, scene) # 심박수 측정 호출
            "이곳에서 앞으로의 내 삶이 어떻게 바뀔지 상상하니 가슴이 두근거렸다."
            s "현재 심장박동 분석중입니다.."
            if test['rising'] == True:
                "서연에게 동아리 활동에 대한 생각을 물어본다"
                hide c_lol
                show c_worr
                $ c_love += 2
                c "솔직히 아직은 잘 모르겠어요. 그냥... 분위기를 느껴보고 싶었을 뿐이에요."
                "서연의 대답은 마치 자신이 어떤 정체성을 찾고 있는 것처럼 느껴졌다."
                hide c_worr
                scene dongai
            else:
                "서연에게 카메라에 대해 물어본다"
                $ c_love += 1
                c "아직 카메라는 잘 모르겠어요. 배워가며 생각해보려구요."
                "서연는 약간의 호기심을 보이며 말을 이어갔다."
                hide c_lol
                scene dongai
        #심장박동이 내려가면
        "혼자 있게 내버려둔다":
            $ c_love -= 1
            "그가 혼자 있고 싶어 하는 것 같아서 굳이 다가가지 않고 멀리서 지켜보기로 했다."
            "그러나 그의 차분한 분위기와 시선이 계속 신경 쓰였다."
            $ test = send_to_raspberry_pi(new_round_number, scene) # 심박수 측정 호출
            s "현재 심장박동 분석중입니다.. "
            if test['rising'] == True:
                "서연에게 인사를 건네본다"
                scene dongC
                show c_lol
                $ c_love += 3
                c "…아, 안녕하세요."
                "그의 말투에는 어딘가 신비로운 분위기가 감돌았다."
                "마치 평범하지않은 신입생같다."
                hide c_lol
                scene dongai
            else:
                "방을 조용히 둘러본다"
                "나는 동아리 방의 분위기를 차분히 느끼며, 앞으로의 활동을 기대하기 시작했다."
                $ c_love -= 1
    # A 또는 B 또는C와 마지막 대화
    "다들 집으로 돌아가기 전, 나는 용기를 내어 마지막 대화를 나누어 보기로 했다."
    menu:
        "아린선배에게 동아리 활동에 대해 자세히 물어본다":
            $ a_love +=2
            "나는 그녀에게 동아리에 대해 자세히 물었다."
            show a_lol
            a "우리 동아리에 관심이 많구나?"
            a "우리는 기본적으로 사진 촬영 기술을 배우고, 다양한 장소로 출사를 나가."
            a "단순히 찍는 것만이 아니라,"
            a "그 사진으로 전시회도 열고,"
            a "때로는 공모전에도 참여하기도 해!"
            "선배의 이야기에 나는 점점 더 흥미를 느꼈다."
            a "그리고 동아리 내에서는 각자 관심 있는 분야를 중심으로 작업할 기회도 있어."
            a "풍경 사진, 인물 사진, 심지어 필름 카메라를 사용하는 친구들도 많거든."
            menu:
                "풍경 사진에 대해 더 물어본다":
                    "나는 풍경 사진에 흥미가 생겨 선배에게 물어보았다."
                    a "풍경 사진은 정말 매력적이야."
                    a "자연의 색감이나 분위기를 카메라에 담는 건 특별한 경험이지."
                    a "다음 달에 계절 출사를 갈 계획인데, 같이 가면 좋아할 거야."
                
                "인물 사진에 대해 더 물어본다":
                    "나는 인물 사진에 흥미가 생겨 질문했다."
                    a "인물 사진은 순간을 담는 예술이야."
                    a "감정을 사진으로 표현하는 게 어려우면서도 정말 재미있지."
                    a "우리 동아리에는 서로 모델이 되어주며 연습하는 멤버들도 많아."
                
                "필름 카메라에 대해 더 물어본다":
                    "나는 필름 카메라에 흥미를 느껴 물었다."
                    a "필름 카메라는 참 독특하지. 디지털 카메라와는 또 다른 느낌이 있어."
                    a "현상 과정을 거쳐야 해서 더 신중하게 찍게 되는 것도 매력이고."
                    a "필름 카메라를 쓰는 멤버들에게 배울 기회도 있을 거야."
            a"마지막으로 조만간 단합을 위해 여행을 갈꺼니깐 미리 생각해봐! "
            a "어때? 이제 우리 동아리 활동이 조금 더 궁금해졌어?"
            "단합여행이라... 엄청나게 기대가된다."    
            $ danhan = 1
            hide a_lol
                

        "서현에게 친하게 지내자고 말해본다":
            $ b_love += 3
            "나는 용기를 내어 서현에게 친하게 지내자고 말했다."
            show b_lol
            b "정말요? 좋아요! 저도 같은 생각이었어요."
            "서현는 환하게 웃으며 내 제안을 흔쾌히 받아들였다."
            b "아직 아는 사람이 많지 않아서 조금 어색했는데, 덕분에 마음이 놓이네요."
    
            menu:
                "서현에게 왜 사진 동아리에 가입했는지 묻는다":
                    "나는 서현에게 사진 동아리를 선택한 이유를 물었다."
                    b "저요? 사실 사진 찍는 건 초보예요."
                    b "근데 친구가 추천해줘서 시작했어요. 추억을 남길 수 있는 활동이 멋지다고 하더라고요."
                    "서현의 솔직한 대답에 나는 공감하며 고개를 끄덕였다."
                
                "서현에게 어떤 사진을 찍어보고 싶은지 묻는다":
                    "나는 서현에게 어떤 사진을 찍어보고 싶냐고 물었다."
                    b "음... 저는 풍경 사진을 찍어보고 싶어요."
                    b "평소 여행을 좋아하는데, 여행지의 멋진 순간을 사진으로 남기면 정말 특별할 것 같아요."
                    "서현의 대답에 나도 공감하며 여행 사진에 대한 기대를 나누었다."
                
                "서현에게 학과나 취미를 물어본다":
                    "나는 서현에게 학과나 취미에 대해 물어보았다."
                    b "저는 문학과예요. 그래서인지 감정이나 분위기를 담는 사진이 매력적으로 느껴져요."
                    b "취미는 독서나 음악 듣기 정도? 심심한 편이에요."
                    "그의 소박한 취미가 왠지 정겹게 느껴졌다."

            b "우리 앞으로 자주 이야기해요! 같이 활동하면서 더 가까워질 수 있겠죠?"
            "서현과의 짧은 대화였지만, 우리는 빠르게 친해질 수 있을 거란 예감이 들었다."
            hide b_lol


        "서연에게 다음 모임 때도 올 건지 물어본다":
            scene dongC
            $ c_love +=3
            "나는 조심스럽게 서연에게 다음 모임 때도 올 계획이 있는지 물었다."
            show c_base
            c "다음 모임... 글쎄요."
            "서연는 잠시 생각에 잠긴 듯한 표정을 지었다."
            c "사실 아직 잘 모르겠어요. 이런 모임이 제게 맞을지는 확신이 안 서서요."
            menu:
                "서연에게 동아리 활동의 재미를 이야기해본다":
                    "나는 서연에게 동아리 활동이 얼마나 재미있을 수 있는지 말해보았다."
                    "사진을 통해 추억을 남기고, 새로운 사람들과 함께하는 것이 얼마나 즐거운지 이야기했다."
                    c "음... 듣고 보니 꽤 흥미롭네요."
                    c "저도 한 번 제대로 참여해봐야겠어요. 다음 모임엔 다시 와볼게요."
                    hide c_base
                    show c_cute
                    "서연의 대답에 안도하며 미소 지었다."
                    hide c_cute

                "서연에게 동아리 외의 관심사에 대해 물어본다":
                    "나는 서연에게 사진 동아리 외에 관심 있는 것이 있는지 물었다."
                    c "사진이 아니라면... 음, 별로 없어요."
                    c "그냥 혼자서 생각하거나 책 읽는 걸 좋아해요. 사람 많은 곳은 별로 안 좋아하는 편이고요."
                    "서연는 말을 하면서도 약간 망설이는 듯 보였다."
                    "그의 말에서 혼자만의 시간을 즐기는 사람이란 걸 느낄 수 있었다."
                    hide c_base
                    scene dongai
                    
                "서연의 모호한 태도에 대해 솔직히 묻는다":
                    "나는 서연에게 그의 모호한 태도가 궁금하다고 솔직히 물었다."
                    hide c_base
                    show c_lol
                    c "제가요? 그냥... 아직 익숙하지 않아서 그래요."
                    c "새로운 환경에서 너무 쉽게 나서는 게 어색하달까요. 아직 적응 중이에요."
                    "서연는 진솔하게 자신의 마음을 표현했다."
                    c "하지만 [pn] 같은 사람이 있다면 더 쉽게 적응할 수 있을지도 모르겠네요."
                    hide c_lol
                    scene dongai
            "서연는 내 질문에 담담하게 답하며 조금씩 마음을 열어가는 듯 보였다."
            "그와의 대화는 짧았지만, 다음 모임에서 또 볼 수 있을 거란 희망이 생겼다."

        
    "그녀와의 대화가 끝나고, 나는 복잡한 마음으로 동아리 방을 떠났다."
    "모든 것이 새롭고 설레는 대학 생활 속에서, 앞으로 어떤 이야기가 펼쳐질지 기대가 되는 마음으로 집으로 향했다."
    stop music fadeout 2.5
    scene black
    "..."
    ".."
    "."
    jump long_day_3





label long_day_3:
    $ scene = 3
    "다음날이 되었다"
    scene hclass
    play music "audio/bgm/base3_music.mp3"
    "학교에 모든 수업이 끝나고 동아리 모임으로 향했다"
    
    # 동아리 모임 시작
    scene dongai
    "오늘은 단체 사진을 찍는다고 해서 멤버들이 하나둘 동아리 방에 모여들었다."
    
    # 단체 사진 촬영 이벤트
    a "자, 다들 준비됐지? 단체 사진은 우리 동아리의 전통이야."
    b "맞아요. 매년 이렇게 사진을 찍어서 추억을 남기거든요."
    scene camera1
    "나는 멤버들과 함께 사진 촬영 준비를 했다. 카메라 앞에 서니 조금 긴장이 되었다."
    play sound "audio/sound/Storytelling.mp3"
    call open_camera_page#카메라 불러오기
    "찰칵! 카메라 셔터 소리와 함께 모두의 얼굴이 사진으로 남았다."
    scene dongai
    # 동아리 여행 공지
    show a_base
    a "그리고 중요한 공지 하나 더! 다음 주 동아리 여행 간다!"
    if danhan == 1:
        "저번에 들었던 단합 모임이다."
    b "우와, 여행이요? 어디로 가요?"
    a "이번엔 근교의 산으로 가기로 했어. 멋진 풍경 사진도 찍고 재미있게 놀자!"
    hide a_base
    "동아리 멤버들 사이에서 기대감이 가득한 목소리가 터져 나왔다."
    
    # 쇼핑 관련 이벤트 시작
    "모임이 끝난 후, 나는 집으로 가려던 참에 아린 선배가 다가왔다."
    show a_base at left
    a "[pn], 여행 전에 필요한 옷이나 준비물이 있으면 같이 사러 갈래?"
    
    menu:
        "제안을 수락한다":
            "나는 제안을 수락했다."
            $ a_love += 2
            a "좋아! 그럼 내일 백화점에서 만나자!"
            hide a_base 
            stop music fadeout 2.5
            jump long_a_date_shopping

        "제안을 거절한다":
            "나는 미안하다고 말하며 제안을 정중히 거절했다."
            a "아쉽지만 어쩔 수 없지. 그래도 준비 잘 해!"
            hide a_base 
            $ a_love -= 2
            stop music fadeout 2.5
            jump long_b_encounter

label long_a_date_shopping:
    # A와 쇼핑
    scene black
    "다음 날, 나는 선배와 함께 백화점으로 갔다."
    play music "audio/bgm/departmentstore.mp3"
    scene backha
    show a_base
    a "여기 정말 크다! 뭐부터 볼까?"
    "우리는 함께 옷가게를 돌아다니며 서로 어울리는 옷을 추천하기도 하고, 웃으며 시간을 보냈다."
    a "이거 한번 입어볼래?"
    menu:
        "선배가 추천한 옷을 입어본다":
            $ a_love += 1
            "나는 선배가 추천한 옷을 입어보기로 했다."
            a "와, 너한테 정말 잘 어울려! 완전 멋진데?"
            "선배의 칭찬에 조금 부끄러웠지만 기분이 나쁘진 않았다."

        "내가 선배에게 어울리는 옷을 추천한다":
            $ a_love += 2
            "나는 선배에게 어울릴 것 같은 옷을 추천했다."
            a "이거? 한번 입어볼게!"
            hide a_base
            "아린선배가 옷을 갈아입고 나오자, 마치 모델처럼 눈길을 끌었다."
            show a_backha at center
            a "어때? 괜찮아?"
            "나는 고개를 끄덕이며 칭찬했다."
            $ a_back = 1;
            hide a_backha

    "A와 함께한 쇼핑은 즐거웠고, 우리의 사이도 조금 더 가까워진 것 같았다."
    jump long_day_3_end

label long_b_encounter:
    stop music fadeout 2.5
    scene haha
    play music "audio/bgm/alley.mp3"
    # B와의 우연한 만남
    "오늘의 일과를 끝내고"
    "하교 도중, 나는 우연히 서현과 마주쳤다."
    show b_lol
    b "어? 너도 집에 가는 중이야?"
    "나는 고개를 끄덕였다. 그러자 서현이 제안했다."
    b "마침 잘 됐다! 나도 옷 좀 사려고 했는데, 같이 갈래?"
    
    menu:
        "제안을 수락한다":
            $ b_love += 3
            "나는 서현의 제안을 수락했다."
            b "좋아, 그럼 지금 가자!"   
            hide b_lol
            jump long_b_date_shopping

        "제안을 거절한다":
            $ b_love -= 2
            "나는 미안하다고 말하며 서현의 제안을 거절했다."
            b "아, 알겠어. 그럼 다음에 또 보자!"
            hide b_lol dissolve
            jump long_c_observation

label long_b_date_shopping:
    # B와 쇼핑
    stop music fadeout 2.5
    scene black
    "나는 서현과 함께 백화점으로 향했다."
    scene backha
    play music "audio/bgm/Bdepartmentstore.mp3"
    b "와, 여기는 언제 와도 신기해! 뭐부터 볼까?"
    "우리는 함께 여러 매장을 돌아다니며 쇼핑을 즐겼다."
    
    menu:
        "서현이 고른 옷을 칭찬한다":
            $ b_love += 2
            "나는 서현이 고른 옷을 보고 칭찬했다."
            b "정말? 나한테 어울려? 고마워!"
            "서현은 기뻐하며 옷을 구입했다."

        "내가 서현에게 어울리는 옷을 추천한다":
            $ b_love += 3
            "나는 서현에게 어울릴 것 같은 옷을 추천했다."
            show b_backha
            b "오, 이거 괜찮은데? 너 센스 좋다!"
            "서현은 내 추천을 받아들여 옷을 입어보고 만족스러워했다."
            $ b_back = 1;
            hide b_backha

    "서현과 함께한 쇼핑은 유쾌했고, 우리 사이도 더욱 가까워진 것 같았다."
    jump long_day_3_end

label long_c_observation:
    # C의 관찰 이벤트
    stop music fadeout 2.5
    scene hidehaha 
    play music "audio/bgm/C_alley"
    $ c_love += 5
    "나는 혼자 집으로 가는 길에 익숙한 시선을 느꼈다."
    "앞을 자세히보니, 멀리서 서연이 조용히 나를 지켜보고 있었다."
    "그는 눈이 마주치자 약간 당황한 듯 서둘러 자리를 떠났다."
    "그 모습이 묘하게 마음에 남았다."

    "서연이 나를 신경 쓰고 있다는 생각에, 괜히 가슴이 두근거렸다."
    jump long_day_3_end

label long_day_3_end:
    "그렇게 동아리 모임이 끝난 하루가 저물어갔다."
    stop music fadeout 2.5
    scene black
    "점점 더 흥미로운 일들이 일어날 것만 같았다."
    "이런저런 생각끝에 잠에 들었다."
    "..."
    ".."
    "."
    jump long_chapter_4




label long_chapter_4:
    $ scene = 4
    "다음 주가 되었다"
    # 여행 시작
    play music  "audio/bgm/travel.mp3"
    "오늘은 동아리 여행 날! 동아리 멤버들과 함께 봉고차에 탑승하여, 자연이 아름답기로 유명한 산으로 향했다."
    scene mount
    show bongo at left:
        xalign 0.0  # x축의 0.0은 화면의 왼쪽
        yalign 1.0  # 화면 중간에 표시
    "차 안에서는 모두 웃고 떠들며 여행의 시작을 기쁘게 맞이했다."

    # 대여한 봉고차
    "차가 산을 향해 달리는 동안 창밖으로 펼쳐지는 풍경이 아름다웠다."
    play sound "audio/sound/Car.mp3"
    show bongo:
        linear 4.0 xalign 1.0 
    "모두가 기분 좋게 웃으며 대화를 나누고 있었다."
    
    
    # 산에 도착
    hide bongo
    stop music fadeout 2.5
    play music "audio/bgm/Nature.mp3"
    scene realmount
    "도착한 산은 정말 아름다웠다. 푸른 숲과 맑은 공기가 나를 맞이했다."
    "우리는 다같이 산 정상으로 올라가기로 했다."

    # 산 정상까지 올라가는 길
    "산을 올라가면서 우리는 서로 중간중간 사진을 찍어주기도 하고, 재미있는 이야기를 나누기도 했다."
    "사진 찍을 때마다 누군가가 셔터를 누르고, 서로의 웃는 얼굴을 남겼다."
    if a_back == 1:
        show a_backha at left with dissolve
    else:
        show a_base at left with dissolve
    a "곧 정상이야 조금만 더 힘내!"
    
    if b_back == 1:
        show b_backha at right with dissolve:
            size (900,1100)
            yalign -1.0
    else:
        show b_base at right with dissolve
            
    b "얼른 올라가서 쉬자 ㅠㅠ"
    if b_back == 1:
        hide b_backha 
    else:
        hide b_base
        
    if a_back == 1:
        hide a_backha 
    else:
        hide a_base
    # 정상에서 단체 사진
    stop music fadeout 2.5
    scene highmount
    
    "우리는 마침내 산 정상에 도달했다."
    play music "audio/bgm/down.mp3"
    "탁 트인 풍경과 함께 우리는 기념사진을 찍자는 분위기였다."
    
    menu:
        "단체사진을 찍는다":
            "모두 사진찍을 준비를 했다."
            $ scene = "4-2"
            play sound "audio/sound/Storytelling.mp3"
            "찰칵 소리가 들렸다"
            call open_camera_page
            "단체 사진이 정말 마음에 들었다. 모두 함께 웃는 모습이 참 보기 좋았다."
            scene highmount
            "사진을 보고 나서 서로 웃으며 내려가기 시작했다."
            $ danchan = 1
        
        "무시하고 셀카를 찍는다":
            $ a_love -= 3
            $ b_love -= 2
            $ c_love += 3
            play sound "audio/sound/Storytelling.mp3"
            call open_camera_page#카메라 불러오기
            "내가 찍은 셀카가 잘 나온 것 같아 뿌듯해했다."
            "사진을 찍고 모두 기분 좋게 정상에서 내려왔다."
            
            

    # 산에서 내려가기
    "우리는 산에서 내려와 다 같이 밥을 먹으러 가기로 했다."
    "배가 고파진 우리는 근처 식당으로 향했다."

    scene restaurant
    "식당에서 우리는 맛있는 음식을 먹으며 즐거운 시간을 보냈다."
    if danchan == 1:
        "다들 여행을 만족스러워했다."
    else:
        "단체사진을 못 찍은걸 매우 아쉬워했지만,"
        "다들 여행을 만족스러워했다."

    # 숙소 도착
    scene suk
    
    "숙소에 도착한 우리는 각자 짐을 풀고 잠시 휴식을 취했다."
    stop music fadeout 2.5
    


    # C의 고백 이벤트 (C의 호감도가 높을 경우)
    if c_love > a_love and c_love > b_love:
        c "잠깐, 나랑 얘기 좀 할래?"
        play music "audio/bgm/c_music.mp3"
        "서연은 나를 조용히 불러 숙소 앞에서 나와 이야기를 나누었다."
        scene gii
        show c_shy
        c "사실, 오늘 너에게 고백하고 싶었어. 내가 너에게 느끼는 감정은 그냥 친구 이상의 거야."
        c "너도 나랑 같은 마음이었으면 좋겠어..."
        "그는 수줍게 고백했다. 나는 순간 마음이 두근거렸다."
        menu:
            "서연의 고백을 받아들인다":
                
                "나는 서연의 고백을 받아들였다."
                "서연는 정말 기쁜 표정으로 나를 바라보았다."
                hide c_shy
                show c_cute
                c "정말 고마워. 이제부터 우리 둘이 더 가까워지자!"
                hide c_cute
                $ c_cup = 1
            "서연의 고백을 거절한다":
                "나는 서연의 고백을 정중히 거절했다."
                stop music
                hide c_shy
                show c_sad
                c "알겠어, 네가 부담되지 않게 해줄게."
                "서연은 천생연분을 놓쳐"
                "울고있는 사람같았다."

    # A의 고백 이벤트 (A의 호감도가 높을 경우)
    elif a_love > b_love and a_love > c_love:
        a "잠깐 나와줄래? 숙소 앞에서 이야기하고 싶은 게 있어."
        "아린은 나를 숙소 앞에 불러 조용히 말했다."
        play music "audio/bgm/a_music.mp3"
        scene sukfront
        show a_shy
        a "사실 내가 네게 마음이 있었어. 우리가 동아리에서 친해지면서, 점점 네가 좋아졌어."
        a "이제 나의 마음을 알아줬으면 좋겠어."
        "아린은 고백을 하며 나를 바라봤다. 나는 조금 놀라웠지만 마음이 따뜻해졌다."
        menu:
            "아린의 고백을 받아들인다":
                "나는 아린의 고백을 받아들였다."
                a "정말?! 이제부터 우리 둘이 더 많이 함께 보내자!"
                $ a_cup = 1

            "아린의 고백을 거절한다":
                hide a_shy
                stop music
                "나는 아린의 고백을 거절했다."
                show a_sad
                a "알겠어. 부담 가지지 말고, 그래도 좋은 선후배로 계속 지내자!"
                "아린은 고백을 받아들일 수 없다는 내 말을 이해하고 대화를 마쳤다."

    # B의 고백 이벤트 (B의 호감도가 높을 경우)
    elif b_love > a_love and b_love > c_love:
        scene macdow
        play music "audio/bgm/b_music.mp3"
        show goback1:
            align (0.5, 0.2)
        b "나 오늘... 너에게 할 말이 있어."
        hide goback1
        show goback2:
            align (0.5, 0.2)
        b "카톡으로 할게."
        "서현은 나에게 카톡 메시지를 보내며 고백을 전했다."
        hide goback2
        show goback3:
            align (0.5, 0.2)
        b "사실, 나 너 좋아해."
        hide goback3
        show goback4:
            align (0.5, 0.2)
        b "네가 나에게 특별한 사람이라는 걸 알았어."
        "메시지로 고백을 전해온 서현의 고백을 받고 나는 마음이 흔들렸다."
        menu:
            "서현의 고백을 받아들인다":
                hide goback4
                show goback:
                    align (0.5, 0.2)
                "나는 서현의 고백을 받아들였다."
                hide goback
                show gobackwin:
                    align (0.5, 0.2)
                b "정말?? 이제부터 우리 사귀는거다!!"
                $ b_cup = 1
                hide gobackwin
            "서현의 고백을 거절한다":
                hide goback4
                show gobackv2:
                    align (0.5, 0.2)
                stop music
                "나는 서현의 고백을 거절했다."
                hide gobackv2
                show gobacklose:
                    align (0.5, 0.2)
                b "알겠어. 그래도 계속 친구로 잘 지내자"
                "서현은 내 거절을 아쉬워했다."
                hide gobacklose
    else:
        "아무 일이 일어나지않고"
        "서로 즐겁게 떠들며 해는 저물어갔다."

    # 샤워 후 잠
    stop music fadeout 2.5
    scene black
    "저녁이 되고, 우리는 각자 샤워를 하고 잠을 자러 갔다."
    "하루의 피로를 풀고, 곧 잠이 들었다."


    # 아침 일어남
    "다음 날 아침, 봉고차를 타고 학교로 돌아오는 길이었다."
    play music "audio/bgm/base4_music.mp3"
    "여행의 피로도 남아있지만, 마음은 한층 더 가까워진 동아리 멤버들과 함께여서 기뻤다."

    # 축제 설명
    scene chdongnone
    "학교에 도착한 후, 우리는 다가오는 축제에 대해 이야기를 나누었다."
    a "우리 동아리도 축제에서 인생네컷부스를 운영할거야! 다들 준비 잘 해."
    b "이번에는 어떤 활동을 할지 기대돼요"
    b "더 많은 사람들과 소통할 수 있을 것 같아서 좋아요!"
    
    # 해산
    stop music fadeout 2.5
    scene black
    "그렇게 각자는 집으로 돌아가게 되었다. 동아리 여행은 끝이 나고, 축제를 맞이할 준비를 했다."
    "..."
    ".."
    "."
    jump long_chapter_5







label long_chapter_5:
    $ scene = 5
    "다음날이 되었다"
    "오늘은 드디어 기다리던 축제날이다"
    play music "audio/bgm/festival.mp3"
    "기대감을 갖고 학교로 출발했다."

    # 학교에서 축제 준비
    
    "축제 준비가 한창이다. 학교의 각 부스에서 다양한 활동을 준비하고, 교정은 점점 축제 분위기로 물들어갔다."
    "동아리 멤버들은 각자 맡은 역할에 따라 분주하게 움직이고 있었다."
    
    # 주인공의 역할
    scene booo
    "나는 사진 동아리에서 메인 이벤트인 '인생네컷 촬영 부스'를 설치하는 일에 참여하게 되었다."

    show a_base at left with dissolve
    a "이 부스는 우리가 이번 축제의 메인인 만큼 신경 써야 해. 잘 부탁해!"
    
    show b_base at right with dissolve
    b "사진 찍으면서 다들 즐길 수 있는 부스야!"

    hide a_base
    hide b_base
    # 선택: 연인과 함께 부스를 운영하기
    if a_cup == 1:
        show a_base at left with dissolve
        "아린선배는 내 옆에서 웃으며 촬영을 돕는다."
        "사람들을 맞이하면서 함께 시간을 보내다 보니, 시간이 금방 지나갔다."
        "여자친구가 된 아린선배와 함께 하는 시간이 너무 즐거워, 나도 모르게 더 많은 사람들과 웃으며 대화했다."
        hide a_base
        
            
    elif b_cup == 1:
        show b_base at left with dissolve
        "서현는 내 옆에서 활발하게 손님들을 맞이하며 촬영을 도왔다."
        "자연스럽게 분위기가 밝아지며, 웃음소리가 끊이질 않았다."
        "서현과 함께 부스를 운영하며 우리는 점점 더 가까워지는 것 같았다."
        hide b_base

    elif c_cup == 1:
        show c_base at left with dissolve
        "서현은 차분하게 내 옆에서 촬영을 돕기 시작했다."
        "사람들 앞에 나서기보다는 뒤에서 꼼꼼하게 장비를 점검하며, 나를 세심히 도와주었다."
        "함께 대화를 나누며 조용히 시간을 보내는 동안, 평소에는 느끼지 못했던 서현의 따뜻한 면모를 알게 되었다."
        "그 순간만큼은 바쁜 부스 안에서도 두 사람만의 시간이 흐르는 것 같았다."
        hide c_base
        
        
    else:
        "다른사람과 함께 할 수는 없었지만, 혼자서 부스를 설치하고 운영하기로 했다."
        "그래도 사진을 찍는 동안 다들 즐거워하며 감사해했다. 나는 내가 하는 일에 자부심을 느꼈다."

    # 촬영 부스 운영 후, 마무리 촬영
    
    "부스를 끝내고 정리하던 도중"
    "마지막으로, 나는 오늘의 기억을 간직하기 위해 '인생네컷' 촬영을 하기로 했다."
    scene photo_booth
    a "얘들아 웃어!"
    b "김치!"
    c "ㄱ,김치"
    play sound "audio/sound/Storytelling.mp3"
    call open_camera_page
    "촬영을 마친 후, 사진을 보며 그동안의 추억이 떠올랐다. 부스에서 웃고 떠들던 시간, 그리고 동아리 친구들과의 따뜻한 순간들이 떠오른다."



    # 추억 회상
    scene black
    # END
    # if happy-page == 1:
    #     show page1
    # elif happy-page == 2:
    #     show page1
    # elif happy-page == 3:
    #     show page1
    # elif happy-page == 4:
    #     show page1
    # elif happy-page == 5:
    #     show page1
    # elif happy-page == 6:
    #     show page1


    # if heart-page == 1:
    #     show page1
    # elif heart-page == 2:
    #     show page2
    # elif heart-page == 3:
    #     show page3
    # elif heart-page == 4:
    #     show page4
    # elif heart-page == 5:
    #     show page5
    # elif heart-page == 6:
    #     show page6
    call all_picture
    "오늘의 축제도 끝이 나고, 나는 다시 일상으로 돌아갔다."
    "하지만 그 날의 추억은 항상 내 마음 속에 남아 있을 것이다."

    stop music fadeout 2.5
    return 