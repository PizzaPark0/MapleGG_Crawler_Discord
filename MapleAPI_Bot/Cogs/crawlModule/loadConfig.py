import os

class Config:
    def __init__(self):
        with open(f"{os.path.abspath(os.path.dirname(__file__))}\\config.txt", "r", encoding="utf-8") as f:
            self.bot_token = f.readline().split(':')[1].strip()
            self.c_prefix = f.readline().split(':')[1].strip()
            self.api_key = f.readline().split(':')[1].strip()
            self.commandName1 = f.readline().split(':')[1].strip() #이름변경 커맨드
            self.nameFormat = f.readline().split(':')[1].strip() #이름형식

if __name__ == "__main__":
    c = Config()