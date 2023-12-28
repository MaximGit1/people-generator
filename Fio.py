man_name = ("Адам Алан Александр Алексей Андрей Антон Арсен Арсений Артем Артемий Ашот Богдан Борис Валерий Василий"
            " Виктор Виталий Владимир Владислав Всеволод Вячеслав Геворг Георгий Глеб Григорий Давид Даниил Данила Денис Дмитрий"
            " Егор Захар Игнат Игорь Илья Кирилл Константин Кузьма Лаврентий Лев Леонид Макар Максим Максимильян Марат Мариан Марк"
            " Марсель Мартин Матвей Мирослав Мухаммед Никита Николай Олег Осип Оскар Петр Расул Ринат Роберт Родион Роман Ростислав"
            " Руслан Семен Сергей Спартак Станислав Степан Стефан Тигран Тимофей Тимур Тихон Томас Федор Федот Феликс Филипп Хабиб"
            " Харитон Христофор Шамиль Эдвард Эдгар Эдмунд Эдуард Эльдар Эмиль Эрик Эрнест Юлиан Юлий Юрий Яков Ян Ярослав").split()

surname = ("Смирнов Иванов Кузнецов Соколов Попов Лебедев Козлов Новиков Морозов Петров Волков Соловьёв Васильев"
           " Зайцев Павлов Семёнов Голубев Виноградов Богданов Воробьёв Фёдоров Михайлов Беляев Тарасов Белов Комаров"
           " Орлов Киселёв Макаров Андреев Ковалёв Гусев Титов Кузьмин Кудрявцев Баранов Куликов Алексеев Степанов "
           "Яковлев Сорокин Сергеев Романов Захаров Борисов Королёв Герасимов Пономарёв Григорьев Лазарев Медведев"
           " Соболев Данилов Жуков Фролов Журавлёв Николаев Крылов Максимов Ефимов Денисов Громов Фомин Давыдов"
           " Мельников Щербаков Кудряшов Быков Зуев Суворов Панфилов Копылов Михеев Галкин Назаров Лобанов Лукин "
           "Беляков Потапов Некрасов Хохлов Жданов Наумов Кулагин Лапин Прохоров Нестеров Харитонов Агафонов"
           " Муравьёв Ларионов Федосеев Зимин Пахомов Шубин Игнатов Филатов Крюков Рогов Кулаков Терентьев Молчанов"
           " Владимиров Артемьев Гурьев Зиновьев Гришин Кононов Дементьев Ситников Симонов Мишин Фадеев"
           " Комиссаров Мамонтов Носов Гуляев Шаров Устинов Вишняков Евсеев Лаврентьев Брагин Константинов "
           "Корнилов Авдеев Зыков Бирюков Шарапов Никонов Щукин Дьячков Одинцов Сазонов Якушев Красильников"
           " Гордеев Самойлов Князев Беспалов Уваров Шашков Бобылёв Доронин Белозёров Рожков Самсонов Мясников "
           "Лихачёв Буров Сысоев Фомичёв Русаков Стрелков Гущин Тетерин Колобов Субботин Фокин Блохин Селиверстов "
           "Пестов Кондратьев Силин Меркушев Лыткин Туров Третьяк").split()

surname_exception = [  # indeclinable surnames
    'Третьяк',
]

women_name = ("Анастасия Анна Мария Елена Дарья Алина Ирина Екатерина Арина Полина Ольга Юлия Татьяна Наталья Виктория "
              "Елизавета Ксения Милана Вероника Алиса Валерия Александра Ульяна Кристина София Марина Светлана "
              "Варвара Софья Диана Яна Кира Ангелина Маргарита Ева Алёна Дарина Карина Василиса Олеся Аделина Оксана "
              "Таисия Надежда Евгения Элина Злата Есения Милена Вера Мирослава Галина Людмила Валентина Нина Эмилия "
              "Камилла Альбина Лилия Любовь Лариса").split()

ABC_REPLACE = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y',
    'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
    'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
}
