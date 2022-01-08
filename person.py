class Person:
    def __init__(self, language):
        self.language = language

    def hello(self):
        if self.language == "ko":
            print("안녕")
        elif self.language == "en":
            print("hey")



def hello(language):
    if language == "ko":
        print("안녕")
    elif language == "en":
        print("hey")

jihyun = Person("ko")
jihyun.hello()

eunjae = Person("en")
eunjae.hello()

hello("en")


for (i, num) in enumerate([3,8,6,10]):
    print(i, num)