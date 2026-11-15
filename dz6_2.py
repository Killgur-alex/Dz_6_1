# переписываем первую часть задания сюда, чтобы все работало без костылей
# КОММЕНТАРИИ ПО РЕШЕНИЮ ЛУЧШЕ СМОТРЕТЬ В ПЕРВОЙ ЧАСТИ

purchases = {}

file = open("purchase_log.txt", "r", encoding="utf-8")

next(file) 

for line in file:
    line = line.strip().strip('{}')
    if line:
        small_line = line.split(',')

        user_id = ""
        category = ""

        for item in small_line:
            key, value = item.split(":")
            key = key.strip().strip('"')
            value = value.strip().strip('"')

            if key == "user_id":
                user_id = value
            elif key == "category":
                category = value

        purchases[user_id] = category

file.close()


# Переходим ко второй части задания.

visit_file = open("visit_log.csv", "r", encoding="utf-8")
funnel_file = open("funnel.csv", "w", encoding="utf-8")

funnel_file.write("user_id,source,category\n")
next(visit_file)

for line in visit_file:
    row = line.strip().split(",")
    user_id = row[0]

    if user_id in purchases:
        category = purchases[user_id]
        funnel_file.write(f"{line.strip()},{category}\n")

visit_file.close()
funnel_file.close()

check_file = open("funnel.csv", "r", encoding="utf-8")
for _ in range(3):
    print(check_file.readline().strip())
check_file.close()