class AbstractNumirology:
  
    def template_method(self) -> None:
      self.channels()
      self.soul_lessons()
      self.birth_canal()
      self.final_value()
    
    def channels(self) -> None:
        pass
    
    def soul_lessons(self) -> None:
        pass
            
    def birth_canal(self) -> None:
        pass
        
    def final_value(self)-> None:
        pass
    
class Numirology(AbstractNumirology):
    """результат"""
    def __init__(self, date: str):
        self.date = date.split('-')
        self.purpose_personal = 0
        self.social_purpose = 0
        self.spiritual_purpose = 0
        self.manifestation_channel = 0
        self.channel_of_intuition = 0
        self.recurring_event_channel = 0
        self.soul_lesson = 0
        self.birth_canal1 = 0
        self.birth_canal2 = 0
        self.birth_canal3 = 0
        self.birth_canal4 = 0
        
    def channels(self) -> None:
        self.manifestation_channel = cannels_num(self.date[2])
        self.channel_of_intuition = cannels_num(self.date[1])
        self.recurring_event_channel = cannels_num(self.date[0])
        
    def soul_lessons(self) -> None:
        self.soul_lesson = cannels_num(
            soul_lesson_value(self.manifestation_channel, self.channel_of_intuition, self.recurring_event_channel))
            
    def birth_canal(self) -> None:
        self.birth_canal1 = cannels_num(str(self.manifestation_channel + self.channel_of_intuition))
        self.birth_canal2 = cannels_num(str(self.channel_of_intuition + self.recurring_event_channel))
        self.birth_canal3 = cannels_num(str(self.recurring_event_channel + self.soul_lesson))
        self.birth_canal4 = cannels_num(str(self.manifestation_channel + self.soul_lesson))
    
        
    def final_value(self) -> None:
        self.purpose_personal = cannels_num(
            soul_lesson_value(self.manifestation_channel, self.channel_of_intuition, self.recurring_event_channel,
                                   self.soul_lesson))
        self.social_purpose = cannels_num(
            soul_lesson_value(self.birth_canal1, self.birth_canal2, self.birth_canal3, self.birth_canal4))
        self.spiritual_purpose = cannels_num(str(self.purpose_personal + self.social_purpose))
        
    
def cannels_num(num: str) -> int:
    """если число больше 22 то мы суммируем десятки и еденицы"""
    if int(num) > 22:
        big_value = [int(i) for i in num]
        return sum(big_value)
    else:
        return int(num)
 
 
def soul_lesson_value(*agrs) -> str:
    """Сумма производного к-ва результатов методов"""
    soul_list = [i for i in agrs]
    return str(sum(soul_list))


if __name__ == "__main__":
    date = '28.05.1988'
    test = Numirology(date)
    test.template_method()
    print(test.purpose_personal)
    print(test.social_purpose)
    print(test.spiritual_purpose)
