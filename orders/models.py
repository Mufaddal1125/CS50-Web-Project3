from django.db import models


# Create your models here.
class RegularPizza(models.Model):
    cheese = models.CharField(max_length=50)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f'Cheese: {self.cheese}, small: {self.small}, Large: {self.large}'


class SicilianPizza(models.Model):
    cheese = models.CharField(max_length=50)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f'Cheese: {self.cheese}, small: {self.small}, Large: {self.large}'


class Toppings(models.Model):
    toppings = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.toppings}'


class Subs(models.Model):
    subs = models.CharField(max_length=50)
    small = models.FloatField()
    large = models.FloatField()

    def __str__(self):
        return f'Cheese: {self.subs}, small: {self.small}, Large: {self.large}'


class Pasta(models.Model):
    pasta = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return f'{self.pasta} {self.price}'


class Salads(models.Model):
    salad = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return f'{self.salad} {self.price}'


class DinnerPlatters(models.Model):
    dinnerPlatters = models.CharField(max_length=50)
    small = models.IntegerField()
    large = models.IntegerField()

    def __str__(self):
        return f'Cheese: {self.dinnerPlatters}, small: {self.small}, Large: {self.large}'


class Users(models.Model):
    userName = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    emailAddress = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.userName}, {self.emailAddress}, {self.firstName}, {self.lastName}'
