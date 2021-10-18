from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=254,
                              unique=True,
                              verbose_name='Эл. почта')
    username = models.CharField(max_length=150,
                                blank=False,
                                unique=True,
                                verbose_name='Логин')
    first_name = models.CharField(max_length=150,
                                  blank=False,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=150,
                                 blank=False,
                                 verbose_name='Фамилия')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email


class Follow(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='follower',
                             verbose_name='Подписчик')
    following = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='following',
                                  verbose_name='Автор рецепта')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            ),
            # models.CheckConstraint(
            #    check=~models.Q(user_id=models.F('following_id')),
            #    name='follower_is_not_following',
            # ),
        ]

        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
