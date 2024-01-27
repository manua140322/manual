from pickle import FALSE, TRUE
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db import migrations
# Подключаем модуль для работы с датой/веременем
from datetime import datetime, timedelta
# Поделючаем модуль генерации случайных чисел
import random

global dict_category
dict_category = {}
#global dict_teststask
#dict_teststask = {}

# Найти или Добавить Категорию
def get_category(apps, val):   
    # Поиск категории
    if val in dict_category.values():
        for k, v in dict_category.items():
            if v == val:
                return k    
    else:
        # Если такой категории нет то ее надо добавить
        Category = apps.get_model("guide", "Category")
        category = Category()
        category.title = val
        category.save()
        dict_category[category.id] = category.title
        return category.id

# Добавить Тестовое задание
def insert_teststask(apps, param_teststask):   
    Teststask = apps.get_model("guide", "Teststask")
    teststask = Teststask()
    teststask.category_id = param_teststask[0]
    teststask.title = param_teststask[1]
    teststask.details = param_teststask[2]
    teststask.minutes = param_teststask[3]
    teststask.limit = param_teststask[4]
    teststask.save()
    #dict_teststask[teststask.id] = teststask.title    
    return

# Добавить Вопрос к тестовому заданию
def insert_question(apps, param_question):   
    Question = apps.get_model("guide", "Question")
    question = Question()
    question.teststask_id = param_question[0]
    question.question = param_question[1]
    question.photo = param_question[2]
    question.reply1 = param_question[3]
    question.ok1 = param_question[4]
    question.reply2 = param_question[5]
    question.ok2 = param_question[6]
    question.reply3 = param_question[7]
    question.ok3 = param_question[8]
    question.reply4 = param_question[9]
    question.ok4 = param_question[10]
    question.reply5 = param_question[11]
    question.ok5 = param_question[12]
    question.save()

# Добавить Протокола
def insert_protocol(apps, param_task):   
    Protocol = apps.get_model("guide", "Protocol")
    protocol = Protocol()
    protocol.teststask_id = param_task[0]
    protocol.datep = param_task[1]
    protocol.result = param_task[2]
    protocol.details = param_task[3]
    protocol.user_id = param_task[4]
    protocol.comment = param_task[5]
    protocol.save()
    protocol.datep = param_task[1]
    protocol.save()
    return


def new_data(apps, schema_editor):
    # Суперпользователь id=1
    user = User.objects.create_superuser(username='root',
    email='manua140322@mail.ru',
    first_name='Суперпользователь', 
    last_name='',
    password='SsNn5678+-@')
    print("Суперпользователь создан")
    
    # Группа менеджеров
    managers = Group.objects.get_or_create(name = 'Managers')
    managers = Group.objects.get(name='Managers')
    print("Группа менеджеров создана")
    
    # Пользователь с ролью менеджера id=2
    user = User.objects.create_user(username='manager', password='Ss0066+-', email='manager@mail.ru', first_name='Менеджер',)
    managers.user_set.add(user)
    print("Менеджер добавлен в группу менеджеров")

    # Простые пользователи (заявители) id3-12
    user = User.objects.create_user(username='user1', password='Uu0066+-', email='user1@mail.ru', first_name='Дина', last_name='Мусина')
    user = User.objects.create_user(username='user2', password='Uu0066+-', email='user2@mail.ru', first_name='Адия', last_name='Жунусова')
    user = User.objects.create_user(username='user3', password='Uu0066+-', email='user3@mail.ru', first_name='Айнура', last_name='Кенина')
    user = User.objects.create_user(username='user4', password='Uu0066+-', email='user4@mail.ru', first_name='Рустем', last_name='Какимов')
    user = User.objects.create_user(username='user5', password='Uu0066+-', email='user5@mail.ru', first_name='Алишер', last_name='Кабдуалиев')
    user = User.objects.create_user(username='user6', password='Uu0066+-', email='user6@mail.ru', first_name='Бауржан', last_name='Арыкбаев')
    user = User.objects.create_user(username='user7', password='Uu0066+-', email='user7@mail.ru', first_name='Алишер', last_name='Танатаров')
    user = User.objects.create_user(username='user8', password='Uu0066+-', email='user8@mail.ru', first_name='Мерует', last_name='Искакова')
    user = User.objects.create_user(username='user9', password='Uu0066+-', email='user9@mail.ru', first_name='Ольга', last_name='Муравьева')
    user = User.objects.create_user(username='user10', password='Uu0066+-', email='user10@mail.ru', first_name='Ақжарқын', last_name='Сансызбаева')
    print("Созданы простые пользователи")

    #1 Тестовое задание parameters - (категория, название, описание, время, проходной %)
    parameters = [get_category(apps, "Параллельные запросы"),  "Вариант №1", """Вариант №1""", 20, 75]
    insert_teststask(apps, parameters)    
    parameters = [get_category(apps, "Параллельные запросы"),  "Вариант №2", """Вариант №2""", 20, 75]
    insert_teststask(apps, parameters)    
    parameters = [get_category(apps, "Параллельные запросы"),  "Вариант №3", """Вариант №3""", 20, 75]
    insert_teststask(apps, parameters)    
    parameters = [get_category(apps, "Параллельные запросы"),  "Вариант №4", """Вариант №4""", 20, 75]
    insert_teststask(apps, parameters)    
    parameters = [get_category(apps, "Параллельные запросы"),  "Вариант №5", """Вариант №5""", 20, 75]
    insert_teststask(apps, parameters)    
    print("Категории созданы")

    # Вопрос 1, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какая концепция позволяет выполнить несколько запросов к базе данных одновременно, чтобы ускорить обработку данных?""", None,
                  "a) индексы", False,
                  "b) транзакции", False,
                  "c) параллельные запросы", True,
                  "d) подзапросы", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 2, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """ Какие преимущества могут быть получены с использованием параллельных запросов в базе данных?""", None,
                  "a) уменьшение объема данных", False,
                  "b) улучшение производительности за счет одновременного выполнения запросов", True,
                  "c) увеличение времени блокировки данных", False,
                  "d) исключение несогласованности данных", False,
                  "", False]
    insert_question(apps, parameters)    
   
    # Вопрос 3, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """ Какой элемент базы данных позволяет оптимизировать параллельное выполнение запросов, учитывая структуру хранения данных?""", None,
                  "a) транзакции", False,
                  "b) ограничения целостности", False,
                  "c) индексы", True,
                  "d) представления", False,
                  "", False]
    insert_question(apps, parameters)    
   
    # Вопрос 4, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие типы запросов лучше всего подходят для параллельного выполнения в базе данных?""", None,
                  "a) запросы на выборку данных", True,
                  "b) запросы на вставку данных", False,
                  "c) запросы на удаление данных", False,
                  "d) запросы на обновление данных", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 5, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какой из следующих подходов используется для параллельного выполнения запросов в базе данных?""", None,
                  "a) магистральная шина", False,
                  "b) кластеризация", False,
                  "c) серийное выполнение", False,
                  "d) параллельная обработка", True,
                  "", False]
    insert_question(apps, parameters)    
   
    # Вопрос 6, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие из нижеперечисленных технологий могут поддерживать параллельные запросы в базах данных?""", None,
                  "a) MySQL", True,
                  "b) NoSQL", False,
                  "c) Oracle", False,
                  "d) все вышеперечисленные", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 7, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какой механизм позволяет избежать конфликтов при параллельном доступе к данным?""", None,
                  "a) оптимистическая блокировка", False,
                  "b) пессимистическая блокировка", False,
                  "c) сжатие данных", False,
                  "d) резервное копирование", True,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 8, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие из нижеперечисленных языков программирования могут поддерживать параллельные запросы?""", None,
                  "a) SQL", False,
                  "b) Python", True,
                  "c) Java", False,
                  "d) все вышеперечисленные", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 9, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие из следующих типов индексов могут повысить эффективность параллельных запросов?""", None,
                  "a) кластерные индексы", False,
                  "b) некластерные индексы", False,
                  "c) полнотекстовые индексы", False,
                  "d) географические индексы", True,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 10, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие виды задач могут быть решены с использованием параллельных запросов в базах данных?""", None,
                  "a) аналитические запросы", False,
                  "b) транзакционные запросы", False,
                  "c) обновление данных", False,
                  "d) все вышеперечисленные", True,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 11, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие из нижеперечисленных стратегий могут быть использованы для распределения данных в параллельных запросах?""", None,
                  "a) репликация данных", False,
                  "b) горизонтальное разделение данных", False,
                  "c) вертикальное разделение данных", True,
                  "d) все вышеперечисленные", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 12, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие плюсы приносит параллельное выполнение запросов в распределенных базах данных?""", None,
                  "a) уменьшение нагрузки на сеть", False,
                  "b) повышение отказоустойчивости", False,
                  "c) более эффективное использование ресурсов", False,
                  "d) все вышеперечисленные", True,
                  "", False]
    insert_question(apps, parameters)   

    # Вопрос 13, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие из следующих факторов могут ограничить эффективность параллельных запросов в базах данных?""", None,
                  "a) наличие большого объема данных", False,
                  "b) сложность запросов", False,
                  "c) отсутствие индексов", False,
                  "d) все вышеперечисленные", True,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 14, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие из нижеперечисленных операций поддерживаются при параллельных запросах на обновление данных?""", None,
                  "a) INSERT", False,
                  "b) DELETE", False,
                  "c) UPDATE", False,
                  "d) все вышеперечисленные", True,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 15, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие технологии могут использоваться для мониторинга и оптимизации параллельных запросов в базах данных?""", None,
                  "a) SQL Profiler", False,
                  "b) Query Execution Plan", False,
                  "c) Database Index Tuning Advisor", False,
                  "d) все вышеперечисленные", True,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 16, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [1,  """Какие из нижеперечисленных понятий связаны с параллельным выполнением запросов в базах данных?""", None,
                  "a) атомарность", False,
                  "b) изоляция", False,
                  "c) сериализация", False,
                  "d) параллелизм", True,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 17, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [2,  """Когда используют запрос на выборку?""", None,
                  "a) запрос определяет, какие записи или поля из одной или нескольких таблиц будут отображены при его выполнении", True,
                  "b) эти запросы создаются в тех случаях, когда предполагается выполнять этот запрос многократно, изменяя лишь условия отбора", False,
                  "c) этот запрос можно использовать для выполнения расчетов и поведения итогов из исходных таблиц;", False,
                  "d) этот запрос позволяет производить итоговые вычисления", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 18, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [2,  """На таблице имеется триггер INSTEAD OF UPDATE, который явно вызывает тот же самый оператор UPDATE, который вызвал срабатывание триггера. Что произойдет?""", None,
                  "a) операция обновления будет выполнена", True,
                  "b) зацикливание выполнения, вызванное рекурсивным выполнением триггера", False,
                  "c) сообщение об ошибке времени выполнения", False,
                  "d) триггер не может выполнять ту же самую операцию, которая привела к его срабатыванию. В результате – ошибка компиляции", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 19, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [2,  """Триггер INSTEAD OF INSERT создан на таблице, в которую вставляется строка, нарушающая ссылочную целостность. Что справедливо?""", None,
                  "a) триггер будет выполнен", True,
                  "b) триггер не отработает", False,
                  "c) будет получено сообщение об ошибке", False,
                  "d) триггер отработает, после чего будет выполнен откат транзакции", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 20, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [2,  """Таблица RATE имеет поля rate_id, id_del, value. Какой результат выполнения следующего запроса? DELETE FROM RATE where rate_id in (SELECT reate_id FROM RATE WHERE id_del=1 AND id_del=0""", None,
                  "a) запрос не выполнится", True,
                  "b) запрос выполниться, но не удалит ни одной записи;", False,
                  "c) запрос удалит из таблиц RATE все записи у которых поле id_del=1;", False,
                  "d) запрос удалит из таблиц RATE все записи;", False,
                  "", False]
    insert_question(apps, parameters) 

    # Вопрос 21, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [2,  """На одной и той же таблице имеются триггеры AFTER UPDATE и INSTEAD OF UPDATE. Причем триггер INSTEAD OF UPDATE исполняет оператор UPDATE на той же таблице. Что справедливо при обновлении триггерной таблицы?""", None,
                  "a) будет выполнен триггер INSTEAD OF UPDATE, обновление таблицы и триггер AFTER UPDATE", True,
                  "b) ни одно из перечисленного", False,
                  "c) триггер INSTEAD OF UPDATE будет выполняться в бесконечном цикле. Обновление таблицы и триггер AFTER UPDATE выполнены не будут", False,
                  "d) выполнение триггера INSTEAD OF UPDATE приведет к ошибке. Обновление таблицы и триггер AFTER UPDATE выполнены не будут", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 22, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [2,  """Имеется таблица Employee. Что будет результатом выполнения следующего запроса: SELECT firstName, lastName FROM Employee WHERE lastName BETWEEN 'A%' AND 'D%';""", None,
                  "a) будут отображаться все сотрудники, имеющие фамилии, начинающиеся с 'A' до 'D' по алфавиту, включая А и исключая D", True,
                  "b) выдаст ошибку, так как BETWEEN может использоваться только для чисел, а не для строк", False,
                  "c) будут отображаться все сотрудники, имеющие фамилии, начинающиеся с 'A' до 'D' по алфавиту", False,
                  "d) будут отображаться все сотрудники, имеющие фамилии, начинающиеся с 'A' до 'D' по алфавиту, исключая А и D", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 23, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [2,  """Существует несколько триггеров AFTER на одной таблице для одной операции. Что справедливо относительно порядка выполнения триггеров?""", None,
                  "a) можно указать только первый и последний триггер", True,
                  "b) не может быть несколько одинаковых триггеров на одной таблице", False,
                  "c) можно задать порядок выполнения всех таких триггеров", False,
                  "d) такие триггеры всегда выполняются в произвольном порядке", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 24, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [2,  """Если атрибуты X составляют потенциальный ключ отношения R:""", None,
                  "a) то любой атрибут отношения R функционально зависит от X", True,
                  "b) то любой атрибут отношения R не зависит от X", False,
                  "c) то нет атрибутов отношения R функционально зависимых от X", False,
                  "d) то любой атрибут отношения R потенциально зависит от X", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 25, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [2,  """Если потенциальный ключ отношения является простым:""", None,
                  "a) то отношение автоматически находится в 2НФ", True,
                  "b) то отношение может быть находится в 1НФ", False,
                  "c) то в отношения нет внешних ключей", False,
                  "d) то любой атрибут отношения определен на том же домене, что и потенциальный ключ", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 26, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [2,  """ Атрибуты, если ни один из них не является функционально зависимым от другого:""", None,
                  "a) взаимно независимыми", True,
                  "b) независимыми", False,
                  "c) сложными", False,
                  "d) простыми", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 27, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Отношения слабо нормализованы:""", None,
                  "a) в 1НФ", True,
                  "b) в 3НФ", False,
                  "c) в 4НФ", False,
                  "d) в 5НФ.", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 28, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Адекватность базы данных предметной области хуже:""", None,
                  "a) в 1НФ", True,
                  "b) в 3НФ", False,
                  "c) в 4НФ", False,
                  "d) в 5НФ", False,
                  "", False]
    insert_question(apps, parameters)  

    # Вопрос 29, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Легкость разработки и сопровождения базы данных сложнее:""", None,
                  "a) в 2НФ", True,
                  "b) в 3НФ", False,
                  "c) в 4НФ", False,
                  "d) в 5НФ", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 30, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Скорость выполнения вставки, обновления, удаления медленнее:""", None,
                  "a) в 2НФ", True,
                  "b) в 3НФ", False,
                  "c) в 4НФ", False,
                  "d) в 5НФ", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 31, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Скорость выполнения выборки данных быстрее:""", None,
                  "a) в 2НФ", True,
                  "b) в 3НФ", False,
                  "c) в 4НФ", False,
                  "d) в 5НФ", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 32, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Сильно нормализованные модели данных хорошо подходят для:""", None,
                  "a) OLTP-приложений", True,
                  "b) OLAP-приложений", False,
                  "c) систем поддержки принятия решений", False,
                  "d) хранилищ данных", False,
                  "", False]
    insert_question(apps, parameters)

    # Вопрос 33, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Корректность процедуры нормализации (декомпозиция без потери информации) доказывается теоремой:""", None,
                  "a) Хеза", True,
                  "b) Вирта", False,
                  "c) Шеннона", False,
                  "d) Кодда", False,
                  "", False]
    insert_question(apps, parameters)   

    # Вопрос 34, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Вид связи в явном виде не поддерживается в реляционных базах данных:""", None,
                  "a) «многие ко многим»", True,
                  "b) «один к одному»", False,
                  "c) «один ко многим»", False,
                  "d) «многие к одному»", False,
                  "", False]
    insert_question(apps, parameters) 

    # Вопрос 35, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Процесс обращения пользователя к  БД с целью ввода, получения или изменения информации в БД:""", None,
                  "a) запрос", True,
                  "b) транзакция", False,
                  "c) репликация", False,
                  "d) журнализация", False,
                  "", False]
    insert_question(apps, parameters)    
  
    # Вопрос 36, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Функция, вычисляющая сумму:""", None,
                  "a) SUM", True,
                  "b) AVG", False,
                  "c) COUNT", False,
                  "d) MIN", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 37, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Функция, вычисляющая среднее:""", None,
                  "a) AVG", True,
                  "b) COUNT", False,
                  "c) SUM", False,
                  "d) MIN", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 38, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Функция, вычисляющая максимальное значение:""", None,
                  "a) MAX", True,
                  "b) AVG", False,
                  "c) COUNT", False,
                  "d) SUM", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 39, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [3,  """Функция, вычисляющая количество:""", None,
                  "a) COUNT", True,
                  "b) AVG", False,
                  "c) SUM", False,
                  "d) MIN", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 40, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """По технологии обработки данных базы данных подразделяются на:""", None,
                  "a) распределенные и централизованные", True,
                  "b) с локальным и удаленным доступом", False,
                  "c) файл – сервер и клиент  - сервер", False,
                  "d) распределенные и с локальным доступом", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 41, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Действие выполняет метод Append:""", None,
                  "a) поиск данных в базе данных", True,
                  "b) добавление пустой записи в базу данных", False,
                  "c) просмотр записей в базе данных", False,
                  "d) создание файла базы данных", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 42, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Действие выполняет метод UpDate:""", None,
                  "a) просмотр записей в базе данных", True,
                  "b) поиск данных в базе данных", False,
                  "c) добавление пустой записи в базу данных", False,
                  "d) обновляет поля в записях базы данных", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 43, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """СУБД:""", None,
                  "a) система управления базами данных", True,
                  "b) система упаковки банка данных", False,
                  "c) система уплотнения базы данных", False,
                  "d) система управления блоком данных", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 44, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Тип моделей данных:""", None,
                  "a) реляционный", True,
                  "b) виртуальный", False,
                  "c) централизованный", False,
                  "d) целый", False,
                  "", False]
    insert_question(apps, parameters)   

    # Вопрос 45, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Команда DCL:""", None,
                  "a) GRANT", True,
                  "b) SELECT", False,
                  "c) CREATE DATABASE", False,
                  "d) DROP TABLE", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 46, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Файл с расширением .db:""", None,
                  "a) Paradox", True,
                  "b) Microsoft Access", False,
                  "c) InterBase", False,
                  "d) MS SQL", False,
                  "", False]
    insert_question(apps, parameters)  

    # Вопрос 47, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Расширение файла СУБД Microsoft Access:""", None,
                  "a) MDB", True,
                  "b) DBF", False,
                  "c) DB", False,
                  "d) GDB", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 48, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Расширение файла СУБД Paradox:""", None,
                  "a) DB", True,
                  "b) DBF", False,
                  "c) MDB", False,
                  "d) GDB", False,
                  "", False]
    insert_question(apps, parameters) 

    # Вопрос 49, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Режим таблицы используется для""", None,
                  "a) просмотра, добавления, удаления и редактирования данных в таблице", True,
                  "b) создания и изменения структуры таблицы", False,
                  "c) просмотра данных в таблице", False,
                  "d) создания таблицы и просмотра данных", False,
                  "", False]
    insert_question(apps, parameters)   

    # Вопрос 50, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Операция ALTER PROCEDURE:""", None,
                  "a) модифицировать сохраненную процедуру", True,
                  "b) модифицировать базу данных", False,
                  "c) модифицировать виртуальную таблицу", False,
                  "d) модифицировать таблицу", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 51, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Фильтрация данных""", None,
                  "a) фильтрация данных позволяет выбрать из БД только те записи, которые удовлетворяют некоторому условию", True,
                  "b) фильтрация данных предназначена для удаления лишних записей", False,
                  "c) фильтрация данных только сортирует данные по возрастанию", False,
                  "d) фильтрация данных только сортирует данные по убыванию", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 52, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [4,  """Операция DROP TABLE:""", None,
                  "a) удаляет таблицу", True,
                  "b) удаляет базу данных", False,
                  "c) удаляет виртуальную таблицу", False,
                  "d) удаляет индекс", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 53, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Из каких объектов может состоять БД MS Access?""", None,
                  "a) таблица, запрос, форма, отчет, макрос, модуль", True,
                  "b) только таблицы", False,
                  "c) запрос, форма, текстовый редактор", False,
                  "d) только запросы", False,
                  "", False]
    insert_question(apps, parameters)   

    # Вопрос 54, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Создание таблицы состоит из:""", None,
                  "a) определения структуры данных, ввода данных", True,
                  "b) ввода данных", False,
                  "c) определения структуры данных", False,
                  "d) с помощью линий нарисовать таблицу, ввод данных", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 55, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Определение структуры данных таблицы можно выполнить:""", None,
                  "a) в режиме таблицы, конструктора и с помощью Мастера таблиц", True,
                  "b) только в режиме таблицы", False,
                  "c) только в режиме конструктора", False,
                  "d) только с помощью Мастера таблиц", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 56, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Для чего предназначено поле типа счетчик?""", None,
                  "a) для хранения данных, значения которых не редактируются, а устанавливаются автоматически при добавлении каждой новой строки", True,
                  "b) для хранения любых данных", False,
                  "c) для хранения данных, значения которых не редактируются, а устанавливаются автоматически при перемещении курсора в любом направлении", False,
                  "d) для хранения данных, значения которых не редактируются, а устанавливаются автоматически при удалении каждой строки", False,
                  "", False]
    insert_question(apps, parameters)  

    # Вопрос 57, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """В каком режиме осуществляется ввод записей?""", None,
                  "a) в режиме таблиц", True,
                  "b) в режиме конструктора", False,
                  "c) с помощью Мастера таблиц", False,
                  "d) с помощью Мастера конструкторов", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 58, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Для каких целей используется форма?""", None,
                  "a) форма позволяет создавать пользовательский интерфейс для таблиц базы данных и  имеет преимущества для демонстрации данных в упорядоченном и привлекательном виде", True,
                  "b) без формы скрыты данные", False,
                  "c) без формы нельзя создать запросы", False,
                  "d) для демонстрации данных из нескольких таблиц в упорядоченном виде", False,
                  "", False]
    insert_question(apps, parameters)  

    # Вопрос 59, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Можно ли изменить порядок следования записей, например, по алфавиту?""", None,
                  "a) можно", True,
                  "b) нельзя", False,
                  "c) сортировать можно, но только текстовые", False,
                  "d) сортировать можно, но только по дате", False,
                  "", False]
    insert_question(apps, parameters)   

    # Вопрос 60, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Для каких целей используется фильтрация данных?""", None,
                  "a) фильтрация данных позволяет выбрать из БД только те записи, которые удовлетворяют некоторому условию", True,
                  "b) фильтрация данных предназначена для удаления лишних записей", False,
                  "c) фильтрация данных только сортирует данные по возрастанию", False,
                  "d) фильтрация данных только сортирует данные по убыванию", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 61, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """На основе какого объекта можно создать форму?""", None,
                  "a) форма строится на основе таблицы или запроса", True,
                  "b) форма строится только на основе таблицы", False,
                  "c) форма строится только на основе запроса", False,
                  "d) форма строится только на основе макроса", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 62, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Для чего предназначен «Ключ»?""", None,
                  "a) обеспечивает уникальность строк и препятствует вводу повторяющихся блоков данных", True,
                  "b) обеспечивает целостность строк", False,
                  "c) не препятствует вводу повторяющихся блоков данных", False,
                  "d) для обеспечения целостности данных", False,
                  "", False]
    insert_question(apps, parameters)   

    # Вопрос 63, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Для таблиц существуют """, None,
                  "a) два режима: режим конструктора и режим таблицы", True,
                  "b) один режим: режим конструктора ", False,
                  "c) один режим: режим таблицы.", False,
                  "d) три режима: режим конструктора и режим таблицы и режим проектирования.", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 64, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Режим конструктора используется для """, None,
                  "a) создания и изменения структуры таблицы", True,
                  "b) изменения записей таблицы", False,
                  "c) создания структуры таблицы", False,
                  "d) удаления структуры таблицы", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 65, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Режим таблицы применяется для """, None,
                  "a) просмотра, добавления, удаления и редактирования данных в таблице", True,
                  "b) создания и изменения структуры таблицы", False,
                  "c) просмотра данных в форме", False,
                  "d) создания запроса", False,
                  "", False]
    insert_question(apps, parameters) 

    # Вопрос 66, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """С помощью фильтра можно """, None,
                  "a) временно изолировать и просмотреть конкретный набор записей для работы с ним при отображении на экране открытой формы или таблицы", True,
                  "b) работать с конкретным набором удовлетворяющих заданным условиям записей из одной или нескольких таблиц базы данных", False,
                  "c) создать копию данных удовлетворяющих условиям фильтра в новой таблице базы данных Access", False,
                  "d) удалить конкретный набор записей для работы с ним при отображении на экране открытой формы или таблицы", False,
                  "", False]
    insert_question(apps, parameters)  

    # Вопрос 67, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Поименованная, целостная, единая система данных, организованная по определенным правилам, которые предусматривают общие принципы описания, хранения и обработки данных, называется""", None,
                  "a) базой данных", True,
                  "b) базой знаний ", False,
                  "c) реляционной базой данных", False,
                  "d) СУБД ", False,
                  "", False]
    insert_question(apps, parameters)  

    # Вопрос 68, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Отношение обычно имеет вид""", None,
                  "a) двумерной таблицы", True,
                  "b) столбца", False,
                  "c) n-мерной таблицы", False,
                  "d) трехмерной таблицы", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 69, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Атрибут или множество атрибутов, которое единственным образом  идентифицирует кортеж данного отношения, называется""", None,
                  "a) ключом", True,
                  "b) отношением", False,
                  "c) кортежем", False,
                  "d) доменом", False,
                  "", False]
    insert_question(apps, parameters)    

    # Вопрос 70, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Синонимами термина «Столбец» являются """, None,
                  "a) атрибут, поле", True,
                  "b) строка, запись", False,
                  "c) таблица, столбец, строка", False,
                  "d) таблица, файл", False,
                  "", False]
    insert_question(apps, parameters)  

    # Вопрос 71, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Считается, что развитие реляционной модели началось еще в """, None,
                  "a) 70-е годы", True,
                  "b) 50-е годы", False,
                  "c) 60-е годы", False,
                  "d) 80-е годы ", False,
                  "", False]
    insert_question(apps, parameters)  
    
    # Вопрос 72, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Структура данных, в которой каждый объект может иметь более одного господствующего узла, называется """, None,
                  "a) сетевой моделью", True,
                  "b) списком", False,
                  "c) реляционной моделью", False,
                  "d) иерархической моделью ", False,
                  "", False]
    insert_question(apps, parameters)    
    
    # Вопрос 73, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Структура данных в виде древовидной структуры называется""", None,
                  "a) иерархической моделью", True,
                  "b) списком", False,
                  "c) реляционной моделью", False,
                  "d) сетевой моделью", False,
                  "", False]
    insert_question(apps, parameters)   

    # Вопрос 74, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """По технологии обработки данных базы данных принято делить на:""", None,
                  "a) распределенные и централизованные", True,
                  "b) с локальным и удаленным доступом", False,
                  "c) файл – сервер и клиент  - сервер", False,
                  "d) распределенные и с локальным доступом", False,
                  "", False]
    insert_question(apps, parameters)   

    # Вопрос 75, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """По способу доступа к данным базы данных подразделяются на:""", None,
                  "a) с локальным и удаленным доступом", True,
                  "b) распределенные и централизованные", False,
                  "c) файл – сервер и клиент  - сервер", False,
                  "d) распределенные и с локальным доступом", False,
                  "", False]
    insert_question(apps, parameters) 

    # Вопрос 76, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    parameters = [5,  """Системы централизованнных баз данных с сетевым доступом подразделяются на:""", None,
                  "a) файл – сервер и клиент  - сервер", True,
                  "b) распределенные и централизованные", False,
                  "c) с локальным и удаленным доступом", False,
                  "d) распределенные и с локальным доступом", False,
                  "", False]
    insert_question(apps, parameters) 
    
    #insert_question(apps, parameters)    
    ## Вопрос 1, тестовое задание с id=1, parameters - (тестовое задание, вопрос, фото, ответ 1...5, правильный ответ 1...5)
    #parameters = [1,  """""", None,
    #              "", False,
    #              "", False,
    #              "", False,
    #              "", False,
    #              "", False]
    #insert_question(apps, parameters)    

    print("Тестовые задания созданы")

    #1 Протокол, parameters - (id тестового задания (от 1 до 6), дата, результат (%), детали выполнения задания, id пользователя (от 3-х до 12), комментарии преподавателя)
    parameters = [1,  datetime.now() - timedelta(days=7), 100.0, """Всего вопросов: 15. Всего отвечено: 15. Correctly answered: 15, (100.0 %). Тестовое задание выполнено
""", 3, "Отлично"]
    insert_protocol(apps, parameters)    

    

class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(new_data),
    ]
