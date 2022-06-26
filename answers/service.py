date = '28.05.1988'


class Cal_numirology:

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

    def cannels(self, num):
        """"""
        if int(num) > 22:
            big_value = []
            for i in num:
                big_value.append(int(i))
            return sum(big_value)
        else:
            return int(num)

    def soul_lesson_value(self, *agrs):
        """"""
        soul_list = []
        for i in agrs:
            soul_list.append(i)
        return str(sum(soul_list))

    def channels(self):
        self.manifestation_channel = self.cannels(self.date[0])
        self.channel_of_intuition = self.cannels(self.date[1])
        self.recurring_event_channel = self.cannels(self.date[2])

    def soul_lessons(self):
        self.soul_lesson = self.cannels(
            self.soul_lesson_value(self.manifestation_channel, self.channel_of_intuition, self.recurring_event_channel))

    def birth_canal(self):
        self.birth_canal1 = self.cannels(str(self.manifestation_channel + self.channel_of_intuition))
        self.birth_canal2 = self.cannels(str(self.channel_of_intuition + self.recurring_event_channel))
        self.birth_canal3 = self.cannels(str(self.recurring_event_channel + self.soul_lesson))
        self.birth_canal4 = self.cannels(str(self.manifestation_channel + self.soul_lesson))

    def final_value(self):
        self.purpose_personal = self.cannels(
            self.soul_lesson_value(self.manifestation_channel, self.channel_of_intuition, self.recurring_event_channel,
                                   self.soul_lesson))
        self.social_purpose = self.cannels(
            self.soul_lesson_value(self.birth_canal1, self.birth_canal2, self.birth_canal3, self.birth_canal4))
        self.spiritual_purpose = self.cannels(str(self.purpose_personal + self.social_purpose))


if __name__ == "__main__":
    test = Cal_numirology(date)
    test.channels()
    test.soul_lessons()
    test.birth_canal()
    test.final_value()
    print(test.date)
    print(test.purpose_personal)
    print(test.social_purpose)
    print(test.spiritual_purpose)
