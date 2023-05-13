from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db import migrations

def new_tetstask(apps, schema_editor):
    user = User.objects.create_superuser(username='root', email='manua140322@mail.ru', password='SsNn5678+-@')
    managers = Group.objects.get_or_create(name = 'Managers')
    my_group = Group.objects.get(name='Managers')    
    my_group.user_set.add(user)
    print("Суперпользователь создан")

    user = User.objects.create_user(username='manager', password='Ss0066+-')
    my_group = Group.objects.get(name='Managers')    
    my_group.user_set.add(user)
    print("Менеджер создан")

    user = User.objects.create_user(username='user1', password='Uu0066+-')
    user = User.objects.create_user(username='user2', password='Uu0066+-')
    user = User.objects.create_user(username='user3', password='Uu0066+-')
    user = User.objects.create_user(username='user4', password='Uu0066+-')
    user = User.objects.create_user(username='user5', password='Uu0066+-')
    print("Пользователи созданы")

    Category = apps.get_model("guide", "Category")

    category = Category()
    category.id = 1
    category.title = 'Категория №1'   
    category.save()
    print("Категории созданы")

    Teststask = apps.get_model("guide", "Teststask")

    teststask = Teststask()
    teststask.id = 1
    teststask.category_id = 1
    teststask.title = '№1 нұсқа'
    teststask.details = '№1 нұсқа'
    teststask.minutes = 20
    teststask.limit = 75
    teststask.save()

    teststask = Teststask()
    teststask.id = 2
    teststask.category_id = 1
    teststask.title = '№2 нұсқа'
    teststask.details = '№2 нұсқа'
    teststask.minutes = 20
    teststask.limit = 75
    teststask.save()
    
    Question = apps.get_model("guide", "Question")

    question = Question()
    question.teststask_id = 1
    question.question = 'Компьютерлік графика – бұл'
    question.reply1 = 'ақпаратты өңдейтін ғылым'
    question.ok1 = False
    question.reply2 = 'геометриялық кескіндер қасиеттерін зерттейтін'
    question.ok2 = False
    question.reply3 = 'сурет салу барысында компьютер ресурстарын басқаратын ғылым'
    question.ok3 = False
    question.reply4 = 'математикалық формулаларға негізделген ғылым'
    question.ok4 = False
    question.reply5 = 'суреттерді өңдеу, салу тәсілдері мен әдістерін оқытатын ғылым'
    question.ok5 = True
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Компьютерлік графиканың негізгі бағыттары'
    question.reply1 = 'іскерлік, ғылыми, көркемдік және жарнамалық, инженерлік, web'
    question.ok1 = False
    question.reply2 = 'ғылыми, инженерлік, web'
    question.ok2 = False
    question.reply3 = 'іскерлік, ғылыми, тұрмыстық'
    question.ok3 = False
    question.reply4 = 'көркемдік және жарнамалық, инженерлік, нүктелік'
    question.ok4 = True
    question.reply5 = 'тұрмыстық, инженерлік, іскерлік'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Компьютерлік графиканың бейнелеу тәсіліне байланысты бөлінуі'
    question.reply1 = 'растрлық және фракталдық'
    question.ok1 = False
    question.reply2 = 'үш өлшемдік және векторлық'
    question.ok2 = False
    question.reply3 = 'растрлық, фракталдық және векторлық'
    question.ok3 = False
    question.reply4 = 'растрлық және үш өлшемді'
    question.ok4 = False
    question.reply5 = 'растрлық, векторлық, фракталдық және үш өлшемді'
    question.ok5 = True
    question.save()
  
    question = Question()
    question.teststask_id = 1
    question.question = 'Растрлық графиканың негізгі элементі'
    question.reply1 = 'сызық'
    question.ok1 = False
    question.reply2 = 'нүкте'
    question.ok2 = True
    question.reply3 = 'Сызық, доға, шеңбер және төртбұрыш сияқты геометриялық объектілер жинағынан тұратын кескіндер'
    question.ok3 = False
    question.reply4 = 'математикалық формула'
    question.ok4 = False
    question.reply5 = 'символ'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Фракталдық графиканың базалық элементі'
    question.reply1 = 'Математикалық формула'
    question.ok1 = False
    question.reply2 = 'Нүкте'
    question.ok2 = False
    question.reply3 = 'Сызық'
    question.ok3 = False
    question.reply4 = 'Кесінді'
    question.ok4 = False
    question.reply5 = 'Қисық'
    question.ok5 = True
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Векторлық кескіндер'
    question.reply1 = 'сурет, иллюстрациялық кескіндер'
    question.ok1 = False
    question.reply2 = 'Сызық, доға, шеңбер және төртбұрыш сияқты геометриялық объектілер жинағынан тұратын кескіндер'
    question.ok2 = True
    question.reply3 = 'Доға, ұзындық, фрагменттер'
    question.ok3 = False
    question.reply4 = 'Кесінді, қисық, канал, штамп'
    question.ok4 = False
    question.reply5 = 'Кескін, графика, үшінші тәртіпті қисықтар'
    question.ok5 = False
    question.save()
   
    # Вопросы 6-20 проставлен вариант 1, т.к. правильный ответ не известен
    
    question = Question()
    question.teststask_id = 1
    question.question = 'Векторлық кескіндермен жұмыс жасаудағы кемшілікті көрсетіңіз'
    question.reply1 = 'Кескінді жай ғана өзгерте салуға болмайтындығы'
    question.ok1 = True
    question.reply2 = 'Берілгендер көлемінің аздығы'
    question.ok2 = False
    question.reply3 = 'Кескін масштабын өзгерткенде кескін сапасын жоғалтатыны'
    question.ok3 = False
    question.reply4 = 'Растрлеу әдістерін қолданбау'
    question.ok4 = False
    question.reply5 = 'Дұрыс жауап берілмеген'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Растрлық кескіндеудің артықшылықтарын атаңыз'
    question.reply1 = 'Геометриялық кескіндерді салуға арналған'
    question.ok1 = True
    question.reply2 = 'Векторлық кескіндерді бейнелеуге арналған'
    question.ok2 = False
    question.reply3 = 'Растрлық кескіндерді масштабтауға арналған'
    question.ok3 = False
    question.reply4 = 'Растрлеу әдістерін қолдану'
    question.ok4 = False
    question.reply5 = 'Растрлық кескінді түзетуге, әдемілей түсуге, нүктелерді, қажет болмаса ішінара алып тастауға не қоюлатуға арналған'
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 1
    question.question = 'Растрлық кескіндеудің кемшілігін көрсетіңіз'
    question.reply1 = 'Геометриялық кескіндерді өзгерте алмайтындығы'
    question.ok1 = True
    question.reply2 = 'Кескін масштабын өзгерткенде кескін сапасын жоғалтатыны'
    question.ok2 = False
    question.reply3 = 'Растрлық бейнелердің өңделмеуі'
    question.ok3 = False
    question.reply4 = 'Объектілердің растрленбеуі'
    question.ok4 = False
    question.reply5 = 'Барлық жауап дұрыс'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Графикалық ақпараттың нүктелер түрінде ұсынылуын көрсетіңіз'
    question.reply1 = 'Векторлық түрде'
    question.ok1 = True
    question.reply2 = 'Фракталды түрде'
    question.ok2 = False
    question.reply3 = 'Растрлық түрде'
    question.ok3 = False
    question.reply4 = 'Сызық түрде'
    question.ok4 = False
    question.reply5 = 'Геометриялық кескіндер түрінде'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Растрлық графикада қолданылытын қосымша программалар'
    question.reply1 = 'Corel Photo, Adоbe РhotoShop, Photo Finish'
    question.ok1 = True
    question.reply2 = 'Corel Draw, Adobe Illustrator, FreeHand'
    question.ok2 = False
    question.reply3 = 'Corel Draw'
    question.ok3 = False
    question.reply4 = 'Adobe Illustrator'
    question.ok4 = False
    question.reply5 = 'Corel Photo'
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 1
    question.question = 'Компьютерлік графика кескіндерін құру әдісінің түрлерін көрсетіңіз'
    question.reply1 = 'Стохастикалық, геометриялық'
    question.ok1 = True
    question.reply2 = 'Векторлық, итерациялық'
    question.ok2 = False
    question.reply3 = 'Растрлық, векторлық және фракталдық'
    question.ok3 = False
    question.reply4 = 'Растрлеу, масштабтау'
    question.ok4 = False
    question.reply5 = 'Амплитудалы модуляция және жиелік модуляциясы'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Мүмкіндік дегеніміз'
    question.reply1 = 'пиксельдердің орналасу тығыздығы'
    question.ok1 = True
    question.reply2 = 'түстердің қанықтылығы'
    question.ok2 = False
    question.reply3 = 'сурет өлшемі'
    question.ok3 = False
    question.reply4 = 'ұзындық'
    question.ok4 = False
    question.reply5 = 'тереңдік'
    question.ok5 = False
    question.save()
  
    question = Question()
    question.teststask_id = 1
    question.question = 'Графикалық примитивтер'
    question.reply1 = 'доға'
    question.ok1 = True
    question.reply2 = 'полигондар (тіктөртбұрыш)'
    question.ok2 = False
    question.reply3 = 'нүкте'
    question.ok3 = False
    question.reply4 = 'түзу, қисық сызық'
    question.ok4 = False
    question.reply5 = 'барлық жауап дұрыс'
    question.ok5 = False
    question.save()
   
    question = Question()
    question.teststask_id = 1
    question.question = 'Графикалық примитивтер қолданылатын графика түрі'
    question.reply1 = 'растрлық'
    question.ok1 = True
    question.reply2 = 'ғылыми'
    question.ok2 = False
    question.reply3 = 'векторлық'
    question.ok3 = False
    question.reply4 = 'инженерлік'
    question.ok4 = False
    question.reply5 = 'барлық жауап дұрыс'
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 1
    question.question = 'Қандай бағдарламалар графикалық редакторлар деп аталады?'
    question.reply1 = 'мульфильмдер құруға арналған программалар'
    question.ok1 = True
    question.reply2 = 'суреттерді өңдеуге арналған программалар'
    question.ok2 = False
    question.reply3 = 'драйверлер'
    question.ok3 = False
    question.reply4 = 'ақпаратты өңдеу, тасымалдауды жүзеге асыратын программалар'
    question.ok4 = False
    question.reply5 = 'сурет салу кезінде компьютерді басқаратын программалар'
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 1
    question.question = 'Бейнеадаптер...'
    question.reply1 = 'монитордың жұмысын басқарады'
    question.ok1 = True
    question.reply2 = 'дисплей тереңдігі'
    question.ok2 = False
    question.reply3 = 'жедел есте сақтау құрылғысы'
    question.ok3 = False
    question.reply4 = 'графикалық ақпаратты интернетке орналастырады'
    question.ok4 = False
    question.reply5 = 'графикалық ақпаратты бейнежадына сақтайды'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Бейнеадаптердің негізгі бөліктеріне жатпайды'
    question.reply1 = 'жедел бейнежады'
    question.ok1 = True
    question.reply2 = 'бейнечип'
    question.ok2 = False
    question.reply3 = 'герцтегі қайталау жиілігі'
    question.ok3 = False
    question.reply4 = 'базалық енгізу шығару жүйесі'
    question.ok4 = False
    question.reply5 = 'ЦАТ'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 1
    question.question = 'Монитордың ажырату қабілеті мен қайталау жиілігі тәуелді'
    question.reply1 = 'бейнеадаптер мүмкіндігіне'
    question.ok1 = True
    question.reply2 = 'жедел есте сақтау құрылғысына'
    question.ok2 = False
    question.reply3 = 'дюймдегі диагональ өлшеміне'
    question.ok3 = False
    question.reply4 = 'пиксельдер санына'
    question.ok4 = False
    question.reply5 = 'экранның ауысу жиілігіне'
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 1
    question.question = 'Ахроматикалық түстерді белгілеңіз'
    question.reply1 = 'ақ, қара және қызыл'
    question.ok1 = True
    question.reply2 = 'ақ, қара'
    question.ok2 = False
    question.reply3 = 'ақ, қара және сұр'
    question.ok3 = False
    question.reply4 = 'ал қызыл, сары түстер'
    question.ok4 = False
    question.reply5 = 'сұр, қара, көк '
    question.ok5 = False
    question.save()

    # Конец сомнительного фрагмента
    
    question = Question()
    question.teststask_id = 1
    question.question = 'Динамикалық диапозон'
    question.reply1 = 'Суреттің ең ашық және ең көлеңкелі түстер арасындағы деңгейін анықтап алу. Мұны Изображение – Гистограмма арқылы орындауға болады.'
    question.ok1 = True
    question.reply2 = 'Егер сурет шамадан тыс көлеңкелі не ашық болып көрінсе, онда Гамма коррекциясын қолданамыз.'
    question.ok2 = False
    question.reply3 = 'Суретке түсіру кезінде жарықтандыру бір келкі болмауы не жарықтың дұрыс бағытталмауы.'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 2
    question.question = 'Гамма коррекция'
    question.reply1 = 'Суретке түсіру кезінде жарықтандыру бір келкі болмауы не жарықтың дұрыс бағытталмауы.'
    question.ok1 = False
    question.reply2 = 'Суреттің ең ашық және ең көлеңкелі түстер арасындағы деңгейін анықтап алу. Мұны Изображение – Гистограмма арқылы орындауға болады.'
    question.ok2 = False
    question.reply3 = 'Егер сурет шамадан тыс көлеңкелі не ашық болып көрінсе, онда Изображение – Коррекция – Кривые командасын қолданып, күңгірт тондарды ашықтау түске ендіреміз.'
    question.ok3 = True
    question.reply4 = 'Түс балансын жеке – жеке, күңгірт, орта және ашық тондар үшін орындауға '
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Artistic () филтрі –'
    question.reply1 = 'Традициялық көркем өнер саласындағы қолданылатын техникамен әдістердің әсерін беруге арналған.'
    question.ok1 = True
    question.reply2 = 'Анықтықты, түс өткірлігін жұмсарту мақсатында қолданылады.'
    question.ok2 = False
    question.reply3 = 'Экранға шығатын диалогтық терезеде уголь жолағына жылдамдық бағытын беретін бұрыш мәнін ендіру қажет. '
    question.ok3 = False
    question.reply4 = 'Штрихтеу әдісін қолданған көркем – сурет әсерін береді.'
    question.ok4 = False
    question.reply5 = 'Бейненің геометриялық бұзылу бойынша әсер қолданылады.'
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 2
    question.question = 'Blur (Размытое) филтрі –'
    question.reply1 = 'Жарықтандырудың түрлі әсерлерін, жұмсақ бұлттылық әсерін береді.'
    question.ok1 = False
    question.reply2 = 'Экранға шығатын диалогтық терезеде уголь жолағына жылдамдық бағытын беретін бұрыш мәнін ендіру қажет. '
    question.ok2 = False
    question.reply3 = 'Штрихтеу әдісін қолданған көркем – сурет әсерін береді.'
    question.ok3 = False
    question.reply4 = 'Бейненің геометриялық бұзылу бойынша әсер қолданылады.'
    question.ok4 = False
    question.reply5 = 'Анықтықты түс өткірлігін жұмсарту мақсатында қолданылады.'
    question.ok5 = True
    question.save()
    
    question = Question()
    question.teststask_id = 2
    question.question = 'Motion Blur (Размытое в движений) филтрі –'
    question.reply1 = 'Анықтықты түс өткірлігін жұмсарту мақсатында қолданылады.'
    question.ok1 = False
    question.reply2 = 'Жарықтандырудың түрлі әсерлерін, жұмсақ бұлттылық әсерін береді.'
    question.ok2 = False
    question.reply3 = 'Штрихтеу әдісін қолданған көркем – сурет әсерін береді.'
    question.ok3 = False
    question.reply4 = 'Жылдам жүру әсерін береді. Экранға шығатын диалогтық терезеде уголь жолағына жылдамдық бағытын беретін бұрыш мәнін ендіру қажет.'
    question.ok4 = True
    question.reply5 = 'Бейненің геометриялық бұзылу бойынша әсер қолданылады. '
    question.ok5 = False
    question.save()
  	 
    question = Question()
    question.teststask_id = 2
    question.question = 'Brush Strokes (штрихи) филтрі –'
    question.reply1 = 'Бейненің геометриялық бұзылу бойынша әсер қолданылады.'
    question.ok1 = False
    question.reply2 = 'Штрихтеу әдісін қолданған көркем – сурет әсерін береді.'
    question.ok2 = True
    question.reply3 = 'Жылдам жүру әсерін береді. Экранға шығатын диалогтық терезеде уголь жолағына жылдамдық бағытын беретін бұрыш мәнін ендіру қажет.'
    question.ok3 = False
    question.reply4 = 'Анықтықты түс өткірлігін жұмсарту мақсатында қолданылады.'
    question.ok4 = False
    question.reply5 = 'Жарықтандырудың түрлі әсерлерін, жұмсақ бұлттылық әсерін береді.'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Distort (Деформация) филтрі –'
    question.reply1 = 'Жылдам жүру әсерін береді. Экранға шығатын диалогтық терезеде уголь жолағына жылдамдық бағытын беретін бұрыш мәнін ендіру қажет.'
    question.ok1 = False
    question.reply2 = 'Бейненің геометриялық бұзылу бойынша әсер қолданылады.'
    question.ok2 = True
    question.reply3 = 'Анықтықты түс өткірлігін жұмсарту мақсатында қолданылады.'
    question.ok3 = False
    question.reply4 = 'Жарықтандырудың түрлі әсерлерін, жұмсақ бұлттылық әсерін береді.'
    question.ok4 = False
    question.reply5 = 'Штрихтеу әдісін қолданған көркем – сурет әсерін береді. '
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 2
    question.question = 'Render филтрі –'
    question.reply1 = 'Бейненің геометриялық бұзылу бойынша әсер қолданылады.'
    question.ok1 = False
    question.reply2 = 'Жылдам жүру әсерін береді. Экранға шығатын диалогтық терезеде уголь жолағына жылдамдық бағытын беретін бұрыш мәнін ендіру қажет.'
    question.ok2 = False
    question.reply3 = 'Анықтықты түс өткірлігін жұмсарту мақсатында қолданылады.'
    question.ok3 = False
    question.reply4 = 'Жарықтандырудың түрлі әсерлерін, жұмсақ бұлттылық әсерін береді.'
    question.ok4 = True
    question.reply5 = 'Штрихтеу әдісін қолданған көркем – сурет әсерін береді.'
    question.ok5 = False
    question.save()
   
    question = Question()
    question.teststask_id = 2
    question.question = 'Традициялық көркем өнер саласындағы қолданылатын техникамен әдістердің әсерін беруге арналған.'
    question.reply1 = 'Artistic'
    question.ok1 = True
    question.reply2 = 'Blur'
    question.ok2 = False
    question.reply3 = 'Motion Blur'
    question.ok3 = False
    question.reply4 = 'Brush Strokes'
    question.ok4 = False
    question.reply5 = 'Distort'
    question.ok5 = False
    question.save()
      
    question = Question()
    question.teststask_id = 2
    question.question = 'Анықтықты, түс өткірлігін жұмсарту мақсатында қолданылады.'
    question.reply1 = 'Blur'
    question.ok1 = True
    question.reply2 = 'Motion Blur'
    question.ok2 = False
    question.reply3 = 'Render'
    question.ok3 = False
    question.reply4 = 'Distort'
    question.ok4 = False
    question.reply5 = 'Brush Strokes'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Жылдам жүру әсерін береді. Экранға шығатын диалогтық терезеде уголь жолағына жылдамдық бағытын беретін бұрыш мәнін ендіру қажет.'
    question.reply1 = 'Artistic'
    question.ok1 = False
    question.reply2 = 'Blur'
    question.ok2 = False
    question.reply3 = 'Motion Blur'
    question.ok3 = True
    question.reply4 = 'Brush Strokes'
    question.ok4 = False
    question.reply5 = 'Distort'
    question.ok5 = False
    question.save()
  
    question = Question()
    question.teststask_id = 2
    question.question = 'Штрихтеу әдісін қолданған көркем – сурет әсерін береді. '
    question.reply1 = 'Artistic'
    question.ok1 = False
    question.reply2 = 'Blur'
    question.ok2 = False
    question.reply3 = 'Motion Blur'
    question.ok3 = False
    question.reply4 = 'Brush Strokes'
    question.ok4 = True
    question.reply5 = 'Distort'
    question.ok5 = False
    question.save()
  
    question = Question()
    question.teststask_id = 2
    question.question = 'Бейненің геометриялық бұзылуы бойынша әсер қолданылады.'
    question.reply1 = 'Artistic'
    question.ok1 = False
    question.reply2 = 'Blur'
    question.ok2 = False
    question.reply3 = 'Motion Blur'
    question.ok3 = False
    question.reply4 = 'Distort'
    question.ok4 = True
    question.reply5 = 'Brush Strokes '
    question.ok5 = False
    question.save()
      
    question = Question()
    question.teststask_id = 2
    question.question = 'Жарықтандырудың түрлі әсерлерін, жұмсақ бұлттылық әсерін береді.'
    question.reply1 = 'Artistic'
    question.ok1 = False
    question.reply2 = 'Blur'
    question.ok2 = False
    question.reply3 = 'Motion Blur '
    question.ok3 = False
    question.reply4 = 'Brush Strokes '
    question.ok4 = False
    question.reply5 = 'Render'
    question.ok5 = True
    question.save()
   
    question = Question()
    question.teststask_id = 2
    question.question = 'Графикалық редактордың текстпен жұмыс істеу мүмкіндіктері шектелген ба?'
    question.reply1 = 'жоқ'
    question.ok1 = False
    question.reply2 = 'иә'
    question.ok2 = True
    question.reply3 = 'әр кезде'
    question.ok3 = False
    question.reply4 = 'графикалық редактордың түріне қарай'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 2
    question.question = 'Текст теруде бас әріппен қолданылатын перне?'
    question.reply1 = 'Shift'
    question.ok1 = True
    question.reply2 = 'Ctrl'
    question.ok2 = False
    question.reply3 = 'Del'
    question.ok3 = False
    question.reply4 = 'Esc'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Текст блогын құру үшін пайдаланылатын аспап?'
    question.reply1 = 'Штамп'
    question.ok1 = False
    question.reply2 = 'Прямоугольник'
    question.ok2 = False
    question.reply3 = 'Текст'
    question.ok3 = True
    question.reply4 = 'Лассо'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
      
    question = Question()
    question.teststask_id = 2
    question.question = 'Текстті векторлық контурға айналдыру үшін қай команда қолданылады?'
    question.reply1 = 'Слой – Текст – Создать'
    question.ok1 = False
    question.reply2 = 'Слой – Абзац – Создать контур'
    question.ok2 = False
    question.reply3 = 'Слой – Шрифт – Создать контур'
    question.ok3 = False
    question.reply4 = 'Слой – Текст – Создать рабочий контур'
    question.ok4 = True
    question.reply5 = ''
    question.ok5 = False
    question.save()
   
    question = Question()
    question.teststask_id = 2
    question.question = 'Текст шрифті параметрлерін өзгерту үшін'
    question.reply1 = 'Текстік режимді белгілеу керек'
    question.ok1 = False
    question.reply2 = 'Тексттік қатарды белгілеу қажет'
    question.ok2 = True
    question.reply3 = 'Тексттік аспаптарды белгілеу'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Бейненің түс өткірлігін көбейту командасы'
    question.reply1 = 'Фильтр – Резкость'
    question.ok1 = True
    question.reply2 = 'Фильтр - Контрастность'
    question.ok2 = False
    question.reply3 = 'Фильтр - Аrtitic'
    question.ok3 = False
    question.reply4 = 'Фильтр – Размытие '
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
   
    question = Question()
    question.teststask_id = 2
    question.question = 'Көшіріліп қойылған аймақты үлкейтіп, кішірейту және орнын ауыстыру үшін қай команда қолданылады? '
    question.reply1 = 'Редактирование -> Трансформация'
    question.ok1 = True
    question.reply2 = 'Выделение -> Трансформация'
    question.ok2 = False
    question.reply3 = 'Редактирование -> Изменить'
    question.ok3 = False
    question.reply4 = 'Выделение -> Изменить'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 2
    question.question = 'Объектті фоннан бөліп алу үшін пайдаланылатын команда?'
    question.reply1 = 'Фильтр – Extract (Вычитание)'
    question.ok1 = True
    question.reply2 = 'Фильтр - Контрастность'
    question.ok2 = False
    question.reply3 = 'Фильтр - Аrtitic'
    question.ok3 = False
    question.reply4 = 'Фильтр – Размытие'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask_id = 2
    question.question = 'Векторлық аспапқа қай аспап жатады(Photoshop)?'
    question.reply1 = 'Ласса'
    question.ok1 = False
    question.reply2 = 'Кисть'
    question.ok2 = False
    question.reply3 = 'Кадрирование'
    question.ok3 = False
    question.reply4 = 'Свободное перо'
    question.ok4 = True
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask_id = 2
    question.question = 'Қабат мөлдірлігін қай жерден белгілейміз?'
    question.reply1 = 'Слои палитрасынан'
    question.ok1 = True
    question.reply2 = 'Қасиеттер панелінен'
    question.ok2 = False
    question.reply3 = 'Аспаптар панелінен'
    question.ok3 = False
    question.reply4 = ''
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    print("Тестовые задания созданы")

class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(new_tetstask),
    ]
