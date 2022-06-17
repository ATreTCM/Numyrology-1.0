date = '24.12.2018'


def user_date(date):
    return date.split('.')


listy = user_date(date)


def cannels(listy):
    """"""
    if int(listy) > 22:
        big_value = []
        for i in listy:
            big_value.append(int(i))
        return sum(big_value)
    else:
        return int(listy)


def soul_lesson_value(manifestation_channel, channel_of_intuition, recurring_event_channel):
    """"""
    soul_list = []
    soul_list.append(manifestation_channel)
    soul_list.append(channel_of_intuition)
    soul_list.append(recurring_event_channel)
    return str(sum(soul_list))


def soul_lesson_valu(a, b, c, d):
    """"""
    soul_list = []
    soul_list.append(a)
    soul_list.append(b)
    soul_list.append(c)
    soul_list.append(d)
    return str(sum(soul_list))


manifestation_channel = cannels(listy[0])
channel_of_intuition = cannels(listy[1])
recurring_event_channel = cannels(listy[2])
soul_lesson = cannels(soul_lesson_value(manifestation_channel, channel_of_intuition, recurring_event_channel))
birth_canal1 = cannels(str(manifestation_channel + channel_of_intuition))
birth_canal2 = cannels(str(channel_of_intuition + recurring_event_channel))
birth_canal3 = cannels(str(recurring_event_channel + soul_lesson))
birth_canal4 = cannels(str(manifestation_channel + soul_lesson))

purpose_personal = cannels(
soul_lesson_valu(manifestation_channel, channel_of_intuition, recurring_event_channel, soul_lesson))
social_purpose = cannels(soul_lesson_valu(birth_canal1, birth_canal2, birth_canal3, birth_canal4))
spiritual_purpose = cannels(str(purpose_personal + social_purpose))

print(purpose_personal, social_purpose, spiritual_purpose)
print(birth_canal2)
