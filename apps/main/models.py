from django.db import models
from django.conf import settings # 追加したよ
from django.contrib.auth import get_user, get_user_model

User = get_user_model()

class Article(models.Model):
    image = models.ImageField(upload_to='images/', default=None)
    food_name = models.CharField(max_length=200)
    restaurant_name = models.CharField(max_length=200, default='未入力')
    place = models.CharField(max_length=200, default='池袋')
    price = models.CharField(max_length=200, default=3000)
    review = models.PositiveIntegerField(blank=False, null=True, default=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    free_text = models.CharField(max_length=200, default='おいしかったです。')
    def __str__(self):
        return self.food_name