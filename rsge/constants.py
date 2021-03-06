# coding: utf-8

# TODO: gettext, dynamic loading by get_error_codes()
ERROR_CODES = {
    -1: {'type': 1, 'error_msg_ge': u'გაურკვეველი შეცდომა (გადაამოწმეთ თარიღების ფორმატი)',
         'error_msg_ru': u'Неизвестная ошибка'},
    -2: {'type': 2, 'error_msg_ge': u'ზოგადი შეცდომა (არამთელ რიცხვებს გამყოფად წერტილი უნდა ქონდეთ)',
         'error_msg_ru': u'Общая ошибка (в дробных числах знаком разделения должна быть точка)'},
    -100: {'type': 1, 'error_msg_ge': u'სერვისის მომხმარებელი ან პაროლი არასწორია',
           'error_msg_ru': u'Неправильный пользователь или пароль сервиса'},
    -101: {'type': 1, 'error_msg_ge': u'გამომწერის un_id განსხვავდება XML-ში მითითებული seler_un_id -ის გან',
           'error_msg_ru': u'un_id подписчика отличается от seler_un_id, указанного в XML (попытка работать с чужой накладной)'},
    -102: {'type': 1, 'error_msg_ge': u'შეცდომა მოხდა XML-ის პარსირებისას ან SELER_UN_ID ტეგი არ გაქვთ',
           'error_msg_ru': u'При разборе XML произошла ошибка, или отсутсвует SELER_UN_ID тег'},
    -103: {'type': 1, 'error_msg_ge': u'ზედნადების id არასწორია', 'error_msg_ru': u'Неправильный ID номер накладной'},
    -501: {'type': 5, 'error_msg_ge': u'ეს ავტომოანქანა უკვე გაფორმებულია',
           'error_msg_ru': u'Этот автомобиль уже оформлен'},
    -502: {'type': 5, 'error_msg_ge': u'ამ ავტომანქანაზე მფლობელის შეცვლის უფლება არ გაქვთ',
           'error_msg_ru': u'У Вас нет прав на изменения владельца этого автомобиля'},
    -503: {'type': 5, 'error_msg_ge': u'არასწორი შასის ნომერი', 'error_msg_ru': u'Неправильный номер шасси'},
    -504: {'type': 5, 'error_msg_ge': u'ახალი მფლობელის არასწორი კოდი',
           'error_msg_ru': u'Неправильный код нового владельца'},
    -505: {'type': 5, 'error_msg_ge': u'ამ ავტომანქანის წითელში გადაყვანის უფლება არ გაქვთ',
           'error_msg_ru': u'Нельзя передвинуть этот автомобиль в красный'},
    -506: {'type': 5, 'error_msg_ge': u'ამ ავტომანქანის მწვანეში გადაყვანის უფლება არ გაქვთ',
           'error_msg_ru': u'Нельзя передвинуть  этот автомобиль в зеленый'},
    -1001: {'type': 1, 'error_msg_ge': u'ზედნადების ტიპი არასწორია', 'error_msg_ru': u'Неправильный тип накладной'},
    -1002: {'type': 1, 'error_msg_ge': u'ტრანსპორტირების ტიპი არასწორია',
            'error_msg_ru': u'Неправильный вид транспортировки'},
    -1003: {'type': 1, 'error_msg_ge': u'მყიდველის სახელი აუცილებელია როცა მყიდველი უცხო ქვეყნის მოქალაქეა',
            'error_msg_ru': u'Имя покупателя обязательно, когда он является иностранным гражданином'},
    -1004: {'type': 1, 'error_msg_ge': u'მყიდველი აუცილებელია ყოველთვის გარდა შიდაგადაზიდვისას',
            'error_msg_ru': u'Покупатель обязателен всегда, исключая внутренние перевозоки'},
    -1005: {'type': 1, 'error_msg_ge': u'მყიდვევლი არ მოიძებნა (საქართველო)',
            'error_msg_ru': u'Покупатель не найден (Грузия)'},
    -1006: {'type': 1, 'error_msg_ge': u'მყიდვევლი ლიკვიდირებულია ან კოდი გაუქმებულია',
            'error_msg_ru': u'Покупатель ликвидирован или код отменен'},
    -1007: {'type': 1, 'error_msg_ge': u'ტრანსპორტირების დაწყების ადგილი(მისამართი) დიდია',
            'error_msg_ru': u'Большой стартовое место транспортировки (адрес)'},
    -1008: {'type': 1, 'error_msg_ge': u'მძღოლის პირადი ნომერი დიდია', 'error_msg_ru': u'Большой ID номер водителя'},
    -1009: {'type': 1, 'error_msg_ge': u'ტრანსპორტირების დაწყების ადგილი(მისამართი) აუცილებელია',
            'error_msg_ru': u'Стартовое место транспортировки (адрес) обязательно'},
    -1010: {'type': 1, 'error_msg_ge': u'ტრანსპორტირების დასრულების ადგილი(მისამართი) დიდია',
            'error_msg_ru': u'Большое место завершения транспортировки (адрес)'},
    -1011: {'type': 1, 'error_msg_ge': u'ტრანსპორტირების დასრულების ადგილი(მისამართი) აუცილებელია',
            'error_msg_ru': u'Конечный пункт транспортировки (адрес) обязателен'},
    -1012: {'type': 1, 'error_msg_ge': u'მძღოლი აუცილებელია ტრანსპორტირების ტიპის ყველა ზედნადებზე',
            'error_msg_ru': u'Водитель обязателен на всех видов транспортных накладных'},
    -1013: {'type': 1, 'error_msg_ge': u'მძღოლის სახელი აუცილებელია როდესაც მძღოლი უცხო ქვეყნის მოქალაქეა',
            'error_msg_ru': u'Имя водителя обязательно когда водитель гражданин другой страны'},
    -1014: {'type': 1, 'error_msg_ge': u'მძღოლის პირადი ნომერი არასწორია',
            'error_msg_ru': u'ID номер водителя неправильный'},
    -1015: {'type': 1, 'error_msg_ge': u'reception_info დიდია', 'error_msg_ru': u'Reception_info большое'},
    -1016: {'type': 1, 'error_msg_ge': u'receiver_info დიდია', 'error_msg_ru': u'Receiver_info большое'},
    -1017: {'type': 1, 'error_msg_ge': u'მიწოდების თარიღი მეტია მინდინარე თარიღზე',
            'error_msg_ru': u'Дата доставки превышает текущую дату'},
    -1018: {'type': 1, 'error_msg_ge': u'მიწოდების თარიღი ნაკლებია ტრანსპორტირების დაწყების თარიღზე',
            'error_msg_ru': u'Дата доставки меньше чем дата начала транспортировки'},
    -1019: {'type': 1, 'error_msg_ge': u'სტატუსი არასწორია', 'error_msg_ru': u'Неправильный статус'},
    -1020: {'type': 1, 'error_msg_ge': u'შეუნახავს ვერ წაშლი', 'error_msg_ru': u'Не удаляется без сохранения'},
    -1021: {'type': 1, 'error_msg_ge': u'შეუნახავს ვერ გააუქმებ', 'error_msg_ru': u'Не отменяется без сохранения'},
    -1022: {'type': 1, 'error_msg_ge': u'გამყიდველი ლიკვიდირებულია', 'error_msg_ru': u'Продавец ликвидирован'},
    -1023: {'type': 1, 'error_msg_ge': u'ქვეზედნადებისთვის მშობელი აუცილებელია',
            'error_msg_ru': u'Для поднакладной обязательна родительская накладная'},
    -1024: {'type': 1, 'error_msg_ge': u'მშობელი არ მოიძებნა ან მშობელი აქტივირებული არ არის',
            'error_msg_ru': u'Не найдена или не активированна родительная накладная'},
    -1025: {'type': 1, 'error_msg_ge': u'ქვე ზედნადები მარტო დისტრიბუციაზე იწერება',
            'error_msg_ru': u'Под накладная пишется только под дистрибуции'},
    -1026: {'type': 1, 'error_msg_ge': u'მანქანის ნომერი არასწორია', 'error_msg_ru': u'Неправильный номер автомобиля'},
    -1027: {'type': 1, 'error_msg_ge': u'დასრულებულის რედაქტირებას ვერ გააკეთებთ',
            'error_msg_ru': u'Нельзя завершить редактирование накладной'},
    -1028: {'type': 1, 'error_msg_ge': u'წაშლილ ზედნადებში ვერ დაარედაქტირებთ და ვერც წაშლით',
            'error_msg_ru': u'В удаленой накладной нельзя редактировать или удалять'},
    -1029: {'type': 1, 'error_msg_ge': u'გაუქმებულ ზედნადებში ვერ დაარედაქტირებთ და ვერც წაშლით',
            'error_msg_ru': u'В отменной накладной нельзя редактировать или удалять'},
    -1030: {'type': 1, 'error_msg_ge': u'მშობელ ზედნადებს ვერ გააუქმებთ თუ ქვე ზედნადები აქვს',
            'error_msg_ru': u'Нельзя отменить родительскую накладную если у нее есть поднакладная'},
    -1031: {'type': 1, 'error_msg_ge': u'გადაგზავნილს ვერ წაშლით',
            'error_msg_ru': u'Нельзя удалить отправленную накладную'},
    -1032: {'type': 1, 'error_msg_ge': u'ქვე ზედნადები ძირითადი ვერ გახდება',
            'error_msg_ru': u'Поднакладная не сможет стать основной накладной'},
    -1033: {'type': 1, 'error_msg_ge': u'გამოწერილ ზედნადებს ქვე ზედნადებად ვერ გადააკეთებ',
            'error_msg_ru': u'Нельзя переделать выписанную накладную в поднакладную '},
    -1034: {'type': 1, 'error_msg_ge': u'აქტივაციის თარიღი ნაკლებია შექმნის თარიღზე',
            'error_msg_ru': u'Дата активации меньше даты создания'},
    -1035: {'type': 1,
            'error_msg_ge': u'შიდაგადაზიდვის დროს მყიდველის საიდენტიფიკაციო კოდი ცარიელი ან გამყიდველის კოდი უნდა იყოს მითითებული',
            'error_msg_ru': u'Во время внутренних перевозок индетификационный код покупателя НЕ ДОЛЖЕН быть заполнен или нужно указать код продавца'},
    -1036: {'type': 1,
            'error_msg_ge': u'ტრანსპორტირების გარეშე შემთხვევაში დაწყების და დარულების ადგილი უნდა ემთხვეოდეს',
            'error_msg_ru': u'Исключая транспортировку, место старта и завершения перевозки должно совпадать'},
    -1037: {'type': 1, 'error_msg_ge': u'თუ ტრანსპორტირების ტიპი არის სხვა მიუთითეთ TRANS_TXT',
            'error_msg_ru': u'Если тип транспортировки другой, укажите TRANS_TXT'},
    -1038: {'type': 1, 'error_msg_ge': u'გადავადების (აქტივაციის) თარიღი არ უნდა აღემატებოდეს 3 დღეს',
            'error_msg_ru': u'Дата перенесения (активации) не должны превышать 3 дней'},
    -1039: {'type': 1, 'error_msg_ge': u'მყიდველი უნდა განსხვავდებოდეს გამყიდველისგან თუ შიდა გადაზიდვა არ არის',
            'error_msg_ru': u'Покупатель должен отличаться от продавца если это не внутренняя транспортировка'},
    -1040: {'type': 1, 'error_msg_ge': u'მანქანის ნომერი აუცილებელია', 'error_msg_ru': u'Номер автомобиля обязателен'},
    -1041: {'type': 1, 'error_msg_ge': u'მყიდველის სერვისის მომხმარებლის ID არასწორია',
            'error_msg_ru': u'ID пользователя сервера покупателя неправильный'},
    -1042: {'type': 1, 'error_msg_ge': u'ფაქტურაზე მიბმულ ზედნადებს ვერ დაარედაქტირებ',
            'error_msg_ru': u' прикрепленная к фактуре накладная не редактируется'},
    -1043: {'type': 1, 'error_msg_ge': u'თანხა აღემატება 1000000000-ს', 'error_msg_ru': u'Сумма превышает  1000000000'},
    -1045: {'type': 1, 'error_msg_ge': u'ცარიელ ზედნადებს ვერ გააქტიურებ',
            'error_msg_ru': u'Нельзя активировать пустую накладную'},
    -1046: {'type': 1, 'error_msg_ge': u'აქტიურ ზედნადებზე ზედნადების ტიპს ვერ შეცვლით',
            'error_msg_ru': u'Нельзя изменить тип  активированой накладной'},
    -1047: {'type': 1,
            'error_msg_ge': u'გამყიდველი და მყიდველი მხოლოდ შიდა გადაზიდვის დროს შეიძლება იყოს ერთი და იგივე',
            'error_msg_ru': u'Только при внутренней транспортировке допустимо совпадение покупателя и продавца '},
    -1048: {'type': 1, 'error_msg_ge': u'გადამზიდავის ს/ნ არასწორია', 'error_msg_ru': u'И/н перевозчика неправильный'},
    -1049: {'type': 1,
            'error_msg_ge': u'გადამზიდავის ს/ნ მნიშვნელობის მინიჭება, შეცვლა ან წაშლა შეგიძლიათ მხოლოდ "გადამზიდავთან გადაგზავნილი" სტატუსის ზედნადებზე',
            'error_msg_ru': u'Присвоение значения, смена или отмена и/н перевозчика возможна только в статусе "отправленный перевозчику" накладной'},
    -1050: {'type': 1, 'error_msg_ge': u'გადამზიდავის ს/ნ აუცილებელია', 'error_msg_ru': u'И/н перевозчика обязателен'},
    -1051: {'type': 1,
            'error_msg_ge': u'"გადამზიდავთან გადაგზავნილი" სტატუსის ზედნადებზე მძღლის მონაცემებს და ტრანსპორტირების ტიპს ვერ შეცვლით',
            'error_msg_ru': u'В статусе "отправленный перевозчику" накладной, данные водителя и тип транспортировки не подлежат изменению'},
    -1052: {'type': 1,
            'error_msg_ge': u'"გადამზიდავთან გადაგზავნილი" სტატუსის ზედნადებს თქვენ ვერ დაასრულებთ(ასრულებს გადამზიდავი კომპანია)',
            'error_msg_ru': u'Вы не сможете завершить накладную со статусом "отправленный перевозчику" (ее завершает компания по перевозу)'},
    -1053: {'type': 1, 'error_msg_ge': u'მძღოლის მონაცემებს და ტრანსპორტირების ტიპს ავსებს გადამზიდავი',
            'error_msg_ru': u'Данные водителя и тип транспортировки заполняет перевозчик'},
    -1054: {'type': 1, 'error_msg_ge': u'თქვენ არ ხართ ამ ზედნადების გადამზიდი',
            'error_msg_ru': u'Вы не перевозчик этой накладной'},
    -1055: {'type': 1, 'error_msg_ge': u'ხე/ტყის დოკუმენტი აუცილებელია',
            'error_msg_ru': u'Документ дерева/леса обязателен'},
    -1056: {'type': 1, 'error_msg_ge': u'ხე/ტყის დოკუმენტის ნომერი აუცილებელია',
            'error_msg_ru': u'Номер документа дерева/леса обязателен'},
    -1057: {'type': 1, 'error_msg_ge': u'ხე/ტყის დოკუმენტის თარიღი აუცილებელია',
            'error_msg_ru': u'Число документа дерева/леса обязательно'},
    -1058: {'type': 1, 'error_msg_ge': u'ზედნადების კატეგორიას შეცვლა შეიძლება მხოლოდ შენახულ ზედნადებზე',
            'error_msg_ru': u'Изменения категории допустимо только в сохранённых накладных'},
    -1059: {'type': 1, 'error_msg_ge': u'დასრულებულ ზედნადებზე ქვეზედნადებს ვერ გამოწერთ',
            'error_msg_ru': u'Вы не сможете выписать поднакладную  на  завершенную наклвдную'},
    -1060: {'type': 1, 'error_msg_ge': u'ზედნადების კატეგორია არასწორია',
            'error_msg_ru': u'Неправильная  категория накладной'},
    -1061: {'type': 1,
            'error_msg_ge': u'თქვენ გაქვთ წაუკითხავი აუცილებელი შეტყობინება (გაეცანით შეტყობინებას და შემდეგ შეგეძლებათ ზედნადების გამოწერა)',
            'error_msg_ru': u'У вас есть непрочитанное обязательное сообщение (ознакомьтесь с ним  и потом сможете выписывать накладную)'},
    -1062: {'type': 1,
            'error_msg_ge': u'გადამზიდი შეგიძლიათ გამოიყენოთ მხოლოდ ტრანსპორტირებით ან შიდაგადაზიდვის ტიპის ზედნადებებზე',
            'error_msg_ru': u'Перевозчик используется  только при транспортировке или во внутреперевозном типе накладной'},
    -1063: {'type': 1, 'error_msg_ge': u'კორექტირება შეუძლებელია, ვინაიდან დადასტურებულია საბაჟოს მიერ',
            'error_msg_ru': u'Корректировка невозможна так как утверждено таможней'},
    -1064: {'type': 1,
            'error_msg_ge': u'შექმნის თარიღის დიაპაზონის მითითება აუცილებელია და არ უნდა აღემატებოდეს 72 საათს',
            'error_msg_ru': u'Обязательно нужно  указать диапазон даты создания  и он не должен превышать 72 часов'},
    -2001: {'type': 2, 'error_msg_ge': u'პროდუქტის დასახელება დიდია', 'error_msg_ru': u'Длинное название продукта'},
    -2002: {'type': 2, 'error_msg_ge': u'vat_type არასწორია', 'error_msg_ru': u'Неправильный vat_type'},
    -2003: {'type': 2, 'error_msg_ge': u'unit_id არასწორია', 'error_msg_ru': u'Неправильный unit_id'},
    -2004: {'type': 2, 'error_msg_ge': u'unit_txt აუცილებელია როცა unit_id = 99',
            'error_msg_ru': u'Unit_txt обязателенo когда unit_id = 99'},
    -2005: {'type': 2, 'error_msg_ge': u'რაოდენობა 0-ზე მეტი უნდა', 'error_msg_ru': u'Количество должно быть больше 0'},
    -2006: {'type': 2, 'error_msg_ge': u'ქონების სტატუსი არასწორია', 'error_msg_ru': u'Неправильный статус имущества'},
    -2007: {'type': 2, 'error_msg_ge': u'price არის აუცილებელი გარდა შიდაგადაზიდვის',
            'error_msg_ru': u'Price обязателен всегда, исключая внутренние перевозоки'},
    -2008: {'type': 2, 'error_msg_ge': u'აქციზის ID არასწორია',
            'error_msg_ru': u'Неправильный ID номер акцизной марки'},
    -2009: {'type': 2, 'error_msg_ge': u'მშობელ ზედნადებში არ არის შესაბამისი საქონელი, საქონლის ერთეული ან შტრიხკოდი',
            'error_msg_ru': u'В родительской накладной нет соответствующего товара, единицы товара или штрихкода'},
    -2010: {'type': 2, 'error_msg_ge': u'საქონლის აქციზური კოდი ამ პერიოდს არ ეკუთვნის',
            'error_msg_ru': u'Акцизный код продукта не совпадает с этим периодом'},
    -3001: {'type': 3, 'error_msg_ge': u'ზედნადები არ მოიძებნა', 'error_msg_ru': u'Накладная не найдена'},
    -3002: {'type': 3, 'error_msg_ge': u'გამყიდველი არ არის დეკლარირებაში რეგისტრირებული',
            'error_msg_ru': u'Продавец не зарегистрирован в декларации'},
    -3003: {'type': 3, 'error_msg_ge': u'ზედნადები არ არის აქტივირებული',
            'error_msg_ru': u'Накладная не активированна'},
    -3004: {'type': 3, 'error_msg_ge': u'გამყიდველი არ არის დღგს გადამხდელი',
            'error_msg_ru': u'Продавец не оплачивает ндс'},
    -3005: {'type': 3,
            'error_msg_ge': u'მყიდველი გაუქმებულია/მყიდველი არ არის გადამხდელი ან რეგისრირებული არ არის დეკლარირებაში',
            'error_msg_ru': u'Покупатель отменен/покупатель не оплачивает или не зарегистрирован в декларации'},
    -3006: {'type': 3, 'error_msg_ge': u'ანგარიშფაქტურა და ზედნადები სხვადასხვა გადამხდელზეა გამოწერილი',
            'error_msg_ru': u'Счет-фактура и накладная выписана на имя на разных покупателей'},
    -3007: {'type': 1, 'error_msg_ge': u'ფაქტურაში საქონლის ჩამონათვალში მოხდა შეცდომა',
            'error_msg_ru': u'В фактуру перечисления товаров попала ошибка '},
    -3008: {'type': 1, 'error_msg_ge': u'ფაქტურის შენახვისას მოხდა შედომა',
            'error_msg_ru': u'Ошибка при сохранении фактуры'},
    -3009: {'type': 1, 'error_msg_ge': u'ფაქტურაში ზედნადებების ჩამონათვალში მოხდა შეცდომა',
            'error_msg_ru': u'Ошибка в фактуре в перечислении накладных'},
    -3010: {'type': 3, 'error_msg_ge': u'ანგარიშ-ფაქტურის შენახვა ვერ მოხერხდა',
            'error_msg_ru': u'Счет-фактура не сохранена'},
    -3011: {'type': 3, 'error_msg_ge': u'ანგარიშ-ფაქტურის კორექტირება ვერ მოხერხდა',
            'error_msg_ru': u'Не удалось корректировать счет-фактуру'},
    -3012: {'type': 3, 'error_msg_ge': u'ანგარიშ-ფაქტურის პროდუქციის შენახვა ვერ მოხერხდა',
            'error_msg_ru': u'Не удалось сохранить  продукцию счет-фактуры'},
    -3013: {'type': 3, 'error_msg_ge': u'ანგარიშ-ფაქტურის ზედნადებზე მიბმა ვერ განხორციელდა',
            'error_msg_ru': u'Не удалось прикрепить счет-фактуру к накладной'},
    -3014: {'type': 3, 'error_msg_ge': u'ანგარიშ-ფაქტურის სტატუსის შეცვლა ვერ მოხერხდა',
            'error_msg_ru': u'Не изменился статус счет-фактуры'},
    -3015: {'type': 3, 'error_msg_ge': u'ანგარიშ-ფაქტურის დადასტურება ვერ მოხერხდა',
            'error_msg_ru': u'Счет-фактура не подтверждена'},
    -3016: {'type': 3,
            'error_msg_ge': u'ანგარიშ-ფაქტურის შექმნა ვერ მოხერხდა რადგან ერთ-ერთ ზედნადებზე უკვე გამოწერილია ანგარიშ-ფაქტურა ან მოცემული ზედნადები გაუქმებულია',
            'error_msg_ru': u'Невозможно создать счет-фактуру, так как в одной из накладных уже выписанна счет-фактура или данная накладная ликвидированна'},
    -3017: {'type': 3, 'error_msg_ge': u'გადამხდელი არ არის რეგისტრირებული ელ-დეკლარირებაში',
            'error_msg_ru': u'Покупатель не зарегистрирован в электронной версии  декларации'},
    -3018: {'type': 3, 'error_msg_ge': u'მომხმარებელი არ არის დღგ-ს გადამხდელი',
            'error_msg_ru': u'Покупатель не оплачивает ндс'},
    -3019: {'type': 3, 'error_msg_ge': u'დიპლომატის შემთხვევაში დაბეგვრის ტიპი უნდა იყოს ნულოვანი',
            'error_msg_ru': u'Для дипломатов  тип налога является нулевым'},
    -3020: {'type': 3, 'error_msg_ge': u'ოპერაციის თარიღი არ უნდა აღემატებოდეს მიმდინარე თარიღს',
            'error_msg_ru': u'Дата операции не должна превышать текущую дату'},
    -3021: {'type': 3, 'error_msg_ge': u'თქვენი მომხმარებელი გაუქმებულია. არ გაქვთ გადაგზავნის უფლება',
            'error_msg_ru': u'Ваш аккаунт пользователя удален. У Вас нет прав на пересылку'},
    -3022: {'type': 3, 'error_msg_ge': u'ეს ფუნქცია დროებით გათიშულია',
            'error_msg_ru': u'Эта функция временно отключена'},
    -3023: {'type': 3, 'error_msg_ge': u'ამ პერიოდში დღგ-ს გადამხდელად არ იყავით რეგისტრირებული',
            'error_msg_ru': u'В этот период вы не были зарегистрированы платильщиком НДС'},
    -3024: {'type': 3, 'error_msg_ge': u'თქვენი ორგანიზაცია ლიკვიდირებული/გაუქმებულია',
            'error_msg_ru': u'Ваша организация ликвидированна/ закрыта'},
    -3025: {'type': 3, 'error_msg_ge': u'მყიდველის ორგანიზაცია ლიკვიდირებული/გაუქმებულია',
            'error_msg_ru': u'Организация покупателя ликвидирована'},
    -3026: {'type': 3, 'error_msg_ge': u'პროდუქცია ცარიელი ვერ იქნება',
            'error_msg_ru': u'Продукция не может быть пустой'},
    -4001: {'type': 1, 'error_msg_ge': u'შეცდომა მოხდა სასაქონლო მატერიალული ფასეულობების სიაში',
            'error_msg_ru': u'В список материальной ценности товара попала ошибка'},
    -4002: {'type': 1,
            'error_msg_ge': u'სატესტო კოდებიდან მხოლოდ სატესტოზე გამოწერეთ : სატესტო კოდებია :206322102,12345678910',
            'error_msg_ru': u'Из тестовых кодов выпишете только тестовой : тестовые коды : 206322102,12345678910'},
    -20012: {'type': 4, 'error_msg_ge': u'მოცემულ პერიოდში დეკლარირება არ გეკუთვნით',
             'error_msg_ru': u'В данном периоде декларация не нужна'},
    -20021: {'type': 4,
             'error_msg_ge': u'ხანდაზმულობის ვადის გასვლის გამო (საქართველოს საგადასახადო კოდექსი, მუხლი 4) ამ პერიოდის დეკლარაციის წარდგენა შეუძლებელია',
             'error_msg_ru': u'В связи с истечением срока действия (налоговый кодекс Грузии, статья 4) представление декларации этого периода невозможно '}
}

TRANSPORT_TYPE_VEHICLE = 1
TRANSPORT_TYPE_RAILWAY = 2
TRANSPORT_TYPE_AIR = 3
TRANSPORT_TYPE_OTHER = 4
TRANSPORT_TYPE_VEHICLE_FRGN = 6
TRANSPORT_TYPE_VEHICLE_CARRIER = 7

TRANSPORT_TYPES = {
    TRANSPORT_TYPE_VEHICLE: u"საავტომობილო",
    TRANSPORT_TYPE_RAILWAY: u"სარკინიგზო",
    TRANSPORT_TYPE_AIR: u"საავიაციო",
    TRANSPORT_TYPE_OTHER: u"სხვა",
    TRANSPORT_TYPE_VEHICLE_FRGN: u"საავტომობილო - უცხო ქვეყნის",
    TRANSPORT_TYPE_VEHICLE_CARRIER: u"გადამზიდავი - საავტომობილო"
}

WAYBILL_TYPE_INNER = 1
WAYBILL_TYPE_TRANSPORT = 2
WAYBILL_TYPE_NO_TRANSPORT = 3
WAYBILL_TYPE_DISTRIBUTION = 4
WAYBILL_TYPE_RETURN = 5
WAYBILL_TYPE_SUBWAYBILL = 6

WAYBILL_TYPES = {
    WAYBILL_TYPE_INNER: u"შიდა გადაზიდვა",
    WAYBILL_TYPE_TRANSPORT: u"ტრანსპორტირებით",
    WAYBILL_TYPE_NO_TRANSPORT: u"ტრანსპორტირების გარეშე",
    WAYBILL_TYPE_DISTRIBUTION: u"დისტრიბუცია",
    WAYBILL_TYPE_RETURN: u"უკან დაბრუნება",
    WAYBILL_TYPE_SUBWAYBILL: u"ქვე-ზედნადები",
}

WAYBILL_STATUS_SAVED = 0
WAYBILL_STATUS_ACTIVE = 1
WAYBILL_STATUS_CLOSED = 2
WAYBILL_STATUS_REVOKED = -2  # marked with "red flag" - after ref_waybill call

WAYBILL_CATEGORY_REGULAR = 0
WAYBILL_CATEGORY_WOOD = 1

COST_PAYER_BUYER = 1
COST_PAYER_SELLER = 2

TIN_FOREIGN = 0
TIN_CITIZEN = 1
