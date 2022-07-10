class Cal_numirology:
    """Калькулятор нумиролога"""

    def __init__(self, date):
        self.date = date.split('.')
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

    @staticmethod
    def big_values(num):
        """если число больше 22 то мы суммируем десятки и еденицы"""
        if int(num) > 22:
            big_value = [int(i) for i in num]
            return sum(big_value)
        else:
            return int(num)

    @staticmethod
    def soul_lesson_value(*agrs):
        """Сумма производного к-ва результатов методов"""
        soul_list = [i for i in agrs]
        return str(sum(soul_list))

    def channels(self):
        """канналы"""
        self.manifestation_channel = self.big_values(self.date[0])
        self.channel_of_intuition = self.big_values(self.date[1])
        self.recurring_event_channel = self.big_values(self.date[2])

    def soul_lessons(self):
        """урок души"""
        self.soul_lesson = self.big_values(
            self.soul_lesson_value(self.manifestation_channel, self.channel_of_intuition, self.recurring_event_channel))

    def birth_canal(self):
        """каналы рождения"""
        self.birth_canal1 = self.big_values(str(self.manifestation_channel + self.channel_of_intuition))
        self.birth_canal2 = self.big_values(str(self.channel_of_intuition + self.recurring_event_channel))
        self.birth_canal3 = self.big_values(str(self.recurring_event_channel + self.soul_lesson))
        self.birth_canal4 = self.big_values(str(self.manifestation_channel + self.soul_lesson))

    def final_value(self):
        """результат"""
        self.channels()
        self.soul_lessons()
        self.birth_canal()
        self.purpose_personal = self.big_values(
            self.soul_lesson_value(self.manifestation_channel, self.channel_of_intuition, self.recurring_event_channel,
                                   self.soul_lesson))
        self.social_purpose = self.big_values(
            self.soul_lesson_value(self.birth_canal1, self.birth_canal2, self.birth_canal3, self.birth_canal4))
        self.spiritual_purpose = self.big_values(str(self.purpose_personal + self.social_purpose))


if __name__ == "__main__":
    date = '28.05.1988'
    test = Cal_numirology(date)
    test.final_value()
    print(test.date)
    print(test.purpose_personal)
    print(test.social_purpose)
    print(test.spiritual_purpose)
