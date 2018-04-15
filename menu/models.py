from django.db import models


class Menu(models.Model):
    Types = ((1, 'Горячее'),
             (2, 'Супы'),
              (3, 'Закуски'),
               (4, 'Салаты'),
                (5, 'Выпечки'),
                  (6, 'Напитки'))
    name = models.CharField("Название", max_length=30)
    img = models.ImageField("Фото", upload_to='images/')
    price = models.IntegerField("Цена")
    type = models.IntegerField("Тип еды", choices=Types)
    weight = models.CharField("Вес", max_length=10)
    about = models.TextField("Подробности")

    def __str__(self):
        return self.name
