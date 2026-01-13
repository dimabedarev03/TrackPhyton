def find_common_participants(first_group, second_group, razd=','):
    first = first_group.split(razd)
    second = second_group.split(razd)

    common_participants = []
    for i in first:
        for j in second:
            if i == j:
                common_participants.append(i)
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, razd='|'))# TODO Провеьте работу функции с разделителем отличным от запятой
