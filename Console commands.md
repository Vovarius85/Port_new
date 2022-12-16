# News_Portal
Console commands
1. Создаем двух пользователей:
>>> from news.models import *
>>> User.objects.create(username = "Иван Петров")
>>> User.objects.create(username = "Екатерина Рогова")
2. Создаем две модели объекта Author, связанные с пользователями.
>>> Author.objects.create(user = User(id = 1))
>>> Author.objects.create(user = User(id = 2))
3. Добавляем 4 категории в модель Category
>>> Category.objects.create(name_category = International)
>>> Category.objects.create(name_category = Opinion)
>>> Category.objects.create(name_category = Politics)
>>> Category.objects.create(name_category = Health)
4. Добавляем 2 статьи и 1 новость
>>> from news.posts_and_news import *
>>> Post.objects.create(author = Author(1), type_of_post = article, title = title1, text = text1)
>>> Post.objects.create(author = Author(1), type_of_post = article, title = title2, text = text2)
>>> Post.objects.create(author = Author(2), type_of_post = news, title = title3, text = text3) 
5. Присваиваем категории статьям и новостям(первой новости присвоено 2 категории, другим по одной)
Первый способ:
>>> PostCategory.objects.create(post=Post(id=1), category=Category(id=1))
>>> PostCategory.objects.create(post=Post(id=1), category=Category(id=3))
>>> PostCategory.objects.create(post=Post(id=2), category=Category(id=1))
>>> PostCategory.objects.create(post=Post(id=3), category=Category(id=4))
Второй способ (как в учебном материале)
>>> p1 = Category.objects.all()[1] – Записываем в переменную нужную категорию
>>> post1 = Post.objects.get(id=1) – Записываем в переменную нужный пост
>>> post1.post_category.add(p1) – присваиваем посту категорию
6. Создаем комментарии к постам
>>> comment1 = Comment.objects.create(user = User(id=1), post = Post(id=1), text_comment = 'Интересно')
>>> comment2 = Comment.objects.create(user = User(id=1), post = Post(id=2), text_comment = 'Очень мало фактуры, статья плохая')
>>> comment3 = Comment.objects.create(user = User(id=1), post = Post(id=3), text_comment = 'Удивительая новость')
>>> comment4 = Comment.objects.create(user = User(id=2), post = Post(id=1), text_comment = 'Это великолепно')
>>> comment5 = Comment.objects.create(user = User(id=2), post = Post(id=2), text_comment = 'НАДО ЕЩЕ')
>>> comment6 = Comment.objects.create(user = User(id=2), post = Post(id=3), text_comment = 'Неожиданно')
>>> comment7 = Comment.objects.create(user = User(id=2), post = Post(id=3), text_comment = 'Последний комментарий')
7. Применяем функции like() и dislike() к новостям и комментариям
Первый вариант
>>> comment1.dislike()
>>> comment2.like()
>>> comment2.like()
>>> comment3.dislike()
>>> comment3.dislike()
>>> comment4.like()
>>> comment4.like()
>>> comment4.like()
>>> comment4.like()
>>> comment5.like()
>>> comment6.like()
>>> comment6.like()
>>> comment7.dislike()
Второй вариант
>>> Post.objects.get(pk=1).like()
>>> Post.objects.get(pk=1).like()
>>> Post.objects.get(pk=2).dislike()
>>> Post.objects.get(pk=3).like()
8. Обновляем рейтинг пользователей
>>> Author.objects.get(pk=1).update_rating()
>>> Author.objects.get(pk=2).update_rating()
9. Выводим имя и рейтинг лучшего пользователя сортировкой и возвращая поля первого объекта
>>>  Author.objects.all().values('user__username', 'rating_author').order_by('-rating_author').first()
10. Выводим дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
bestpost1=Post.objects.all().order_by('-rating_post').first()
bestpost1.preview
11. Выводим все комментарии к лучшей статье(дата, пользователь, рейтинг, текст)
comment_all_to_best_post=Comment.objects.filter(post= bestpost1).values('time_in', 'user__username', 'rating_comment', 'text_comment')
comment_all_to_best_post
