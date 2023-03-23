Структура journal.json
Данные представляют собой пары ключ-значение для следующих данных:
- ключ userId - значение cookie phpsessid для пользователя (криптостойкий ключ)
- значение pageNum - количество посещённых страниц (не включая страницы с эмоциональными картинками и опросы эмоций), всего 32

Страницы веб-приложения:
welcome страница
общий опрос и объяснение задачи
страница 1 с эмоциональной картинкой
опрос эмоций 1
тест 1
тест 2
тест 3
страница 2 с эмоциональной картинкой
опрос эмоций 2
тест 4
тест 5
тест 6
...
страница 10 с эмоциональной картинкой
опрос эмоций 10
тест 28
тест 29
тест 30
страница благодарности


Порядок эмоциональных старниц:
нейтральная - oasis_images/Acorns.jpg
положительная - oasis_images/Birthday.jpg
положительная - oasis_images/Cat.jpg
положительная - oasis_images/Chipmunk.jpg
положительная - oasis_images/Dog.jpg
нейтральная - oasis_images/Cups.jpg
отрицательная - oasis_images/Bored_pose.jpg
отрицательная - oasis_images/Depressed_pose.jpg
отрицательная - oasis_images/Baby.jpg
отрицательная - oasis_images/Fire.jpg


Опрос эмоций:
вопрос: Какие эмоции у вас вызвало просмотренное изображение?
варианты ответа:
1.Положительные
2.Скорее положительные
3.Нейтральные
4.Скорее отрицательные
5.Отрицательные
поведение: участник вписывает цифру от 1 до 5 в окно формы, на сервере оценки
1 и 2 конвертируются в 1 - положительные, 4 и 5 в 0 - отрицательные, 3 в 2 - нейтральные.
Нажатие кнопки продолжить перенаправляет участника на страницу с тестом.


Страницы с тестами:
1.figures/cub_cub_2.jpg, figures/cub_triangle_2.jpg, figures/triangle_cub_2.jpg
2.figures/cub_cub_4.jpg, figures/cub_triangle_4.jpg, figures/triangle_cub_4.jpg
3.figures/triangle_triangle_3.jpg, figures/cub_cub_3.jpg, figures/cub_triangle_3.jpg
4.figures/triangle_cub_2.jpg, figures/cub_triangle_2.jpg, figures/cub_cub_2.jpg
5.figures/triangle_triangle_4.jpg, figures/triangle_cub_4.jpg, figures/cub_cub_4.jpg
6.figures/cub_cub_3.jpg, figures/cub_triangle_3.jpg, figures/triangle_triangle_3.jpg
7.figures/cub_triangle_2.jpg, figures/cub_cub_2.jpg, figures/triangle_cub_2.jpg
8.figures/cub_cub_4.jpg, figures/triangle_triangle_4.jpg, figures/cub_triangle_4.jpg
9.figures/cub_cub_3.jpg, figures/triangle_triangle_3.jpg, figures/cub_triangle_3.jpg
10.figures/cub_cub_2.jpg, figures/triangle_cub_2.jpg, figures/triangle_triangle_2.jpg
11.figures/triangle_triangle_2.jpg, figures/triangle_cub_2.jpg, figures/cub_triangle_2.jpg
12.figures/cub_triangle_4.jpg, figures/triangle_triangle_4.jpg, figures/cub_cub_4.jpg
13.figures/cub_triangle_2.jpg, figures/triangle_triangle_2.jpg, figures/triangle_cub_2.jpg
14.figures/triangle_cub_4.jpg, figures/cub_cub_4.jpg, figures/triangle_triangle_4.jpg
15.figures/cub_cub_4.jpg, figures/cub_triangle_4.jpg, figures/triangle_triangle_4.jpg
16.figures/triangle_triangle_2.jpg, figures/cub_cub_2.jpg, figures/cub_triangle_2.jpg
17.figures/triangle_triangle_4.jpg, figures/cub_cub_4.jpg, figures/cub_triangle_4.jpg
18.figures/triangle_cub_4.jpg, figures/cub_triangle_4.jpg, figures/triangle_triangle_4.jpg
19.figures/triangle_triangle_3.jpg, figures/triangle_cub_3.jpg, figures/cub_cub_3.jpg
20.figures/triangle_triangle_2.jpg, figures/cub_triangle_2.jpg, figures/cub_cub_2.jpg
21.figures/cub_cub_3.jpg, figures/triangle_cub_3.jpg, figures/cub_triangle_3.jpg
22.figures/cub_triangle_4.jpg, figures/triangle_triangle_4.jpg, figures/triangle_cub_4.jpg
23.figures/triangle_cub_2.jpg, figures/cub_cub_2.jpg, figures/triangle_triangle_2.jpg
24.figures/triangle_cub_3.jpg, figures/triangle_triangle_3.jpg, figures/cub_cub_3.jpg
25.figures/triangle_cub_2.jpg, figures/triangle_triangle_2.jpg, figures/cub_triangle_2.jpg
26.figures/cub_cub_4.jpg, figures/triangle_cub_4.jpg, figures/cub_triangle_4.jpg
27.figures/cub_triangle_3.jpg, figures/triangle_cub_3.jpg, figures/cub_cub_3.jpg
28.figures/cub_cub_2.jpg, figures/triangle_cub_2.jpg, figures/cub_triangle_2.jpg
29.figures/triangle_triangle_3.jpg, figures/cub_cub_3.jpg, figures/cub_triangle_3.jpg
30.figures/cub_triangle_3.jpg, figures/cub_cub_3.jpg, figures/triangle_cub_3.jpg
