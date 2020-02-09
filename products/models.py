from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=2083)


class ProductSala(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=2083)


class ProductEletronico(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=2083)


class ProductLimpeza(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=2083)


class ProductQuarto(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=2083)


class ProductBanheiro(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=2083)


class ProductCapacetes(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=2083)


class ProductAcampamento(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=2083)


class ProductCozinha(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.CharField(max_length=2083)