from colorfield.fields import ColorField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=200,
                            null=False,
                            blank=False,
                            verbose_name='Название')
    measurement_unit = models.CharField(max_length=200,
                                        null=False,
                                        blank=False,
                                        verbose_name='Единица измерения')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200,
                            unique=True,
                            null=False,
                            blank=False,
                            verbose_name='Название')
    color = ColorField(max_length=7,
                       unique=True,
                       null=False,
                       blank=False,
                       verbose_name='Цвет')
    slug = models.CharField(max_length=200,
                            unique=True,
                            null=False,
                            blank=False,
                            verbose_name='Слаг')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200,
                            blank=False,
                            null=False,
                            verbose_name='Название')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='recipes',
                               verbose_name='Автор рецепта')
    text = models.TextField(blank=False,
                            null=False,
                            verbose_name='Содержание рецепта')
    tags = models.ManyToManyField(Tag,
                                  through='RecipeTags',
                                  verbose_name='Теги')
    ingredients = models.ManyToManyField(Ingredient,
                                         through='RecipeIngredients',
                                         verbose_name='Ингредиенты')
    cooking_time = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='Время приготовления'
    )
    image = models.ImageField(upload_to='api_recipes/back_media/',
                              blank=False,
                              null=False,
                              verbose_name='Иллюстрация блюда')

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.PROTECT,
                                   verbose_name='Ингредиент для рецепта')
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)],
                                         verbose_name='Количество')

    class Meta:
        verbose_name = 'Ингредиенты для рецепта'
        verbose_name_plural = 'Ингридиенты для рецепта'

    def __str__(self):
        return f'{self.recipe} - {self.ingredient} - {self.amount}'


class RecipeTags(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    tag = models.ForeignKey(Tag,
                            on_delete=models.CASCADE,
                            verbose_name='Тег для рецепта')

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.recipe} - {self.tag}'


class Favorite(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='favorite',
                             verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='in_favorite',
                               verbose_name='Рецепт')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'recipe'],
                       name='unique_recipe_in_favorite')]
        ordering = ('-id',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingList(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='shopping_list',
                             verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               verbose_name='Рецепт')

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'recipe'],
                       name='unique_recipe_in_shopping_list')]
        ordering = ('-id',)
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
