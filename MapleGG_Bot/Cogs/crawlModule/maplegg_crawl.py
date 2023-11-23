import requests
from bs4 import BeautifulSoup as bs

class MapleGG_Crawler:
    def __init__(self):
        pass

    def searchNickname(self, nickname): #닉네임을 입력받아 메이플지지에 검색
        res = requests.get(f"https://maple.gg/u/{nickname}")
        return self.__getUserData(res.text)

    def __getUserData(self, res_page): #BeautifulSoup로 html파싱
        soup = bs(res_page, "html.parser") #BeutifulSoup

        user_info1 = soup.select("ul.user-summary-list > li.user-summary-item") #서버명, 레벨, 직업, 인기도
        user_info2 = soup.select("div.character-card-popular > span") #길드, 월드랭킹, 전체랭킹
        user_info3 = soup.select("ul.character-card-additional > li.character-card-additional-item") #무릉도장, 유니온, 더시드
        user_name = soup.select("div[class=\"character-card-name\"]")

        if not user_info1: return 0 #비어있으면=없는 사람이면 0 반환

        user_data = {
            "nickname" : user_name[0].text,
            "server" : user_info1[0].text,
            "level" : user_info1[1].text.split('(')[0].strip('Lv.'),
            "char_class" : user_info1[2].text,
            "popularity" : user_info1[3].text.split()[1],
            "guild" : user_info2[0].text,
            "world_rank" : user_info2[1].text if user_info2[0].text!="(없음)" else "(정보없음)",
            "total_rank" : user_info2[2].text.strip('()') if user_info2[0].text!="(없음)" else "(정보없음)",
            "MuLung_floor" : user_info3[0].text.split()[2] if len(user_info3[0].text.split())>2 else "(정보없음)",
            "union_rank" : user_info3[1].text.split()[1],
            "union_level" : user_info3[1].text.split()[3].strip('Lv.') if len(user_info3[1].text.split())>2 else "(정보없음)",
            "Seed_floor" : user_info3[2].text.split()[2] if len(user_info3[2].text.split())>2 else "(정보없음)"
        }

        return user_data

if __name__=="__main__":
    cc = MapleGG_Crawler()
    print(cc.searchNickname("깜시랑"))