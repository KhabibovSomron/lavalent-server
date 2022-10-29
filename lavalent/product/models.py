from django.db import models

# Create your models here.
class Category(models.Model):
    """Категория"""
    title = models.CharField("Название", max_length=150)
    url = models.SlugField(max_length=160, unique=True)
    image = models.ImageField("Изображение", upload_to="images/category/")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Brand(models.Model):
    """Бренд"""
    title = models.CharField("Название", max_length=150)
    url = models.SlugField(max_length=160, unique=True)
    image = models.ImageField("Изображение", upload_to="images/brands/")
    category = models.ManyToManyField(Category, verbose_name="Категория")


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренд"


class KeyWord(models.Model):
    """Ключевые слова"""
    title = models.CharField("Название", max_length=120)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Ключевые слова"
        verbose_name_plural = "Ключевые слова"



class Product(models.Model):
    """Товар"""
    vendor_code = models.BigIntegerField("Артикул", default=0)
    material  = models.CharField("Материал", max_length=120, default="none")
    description = models.TextField("Описания товара")
    characteristic = models.TextField("Характеристики товара")
    price = models.IntegerField("Цена товара")
    poster = models.ImageField("Постер", upload_to="images/products/posters/", default="none")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, verbose_name="Бренд", on_delete=models.SET_NULL, null=True)
    keywords = models.ManyToManyField(KeyWord, verbose_name="Ключевые слова")
    

    def __str__(self) -> str:
        return f'{self.vendor_code}'

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE, default=1)
    image = models.ImageField("Изображение товара", upload_to=f"images/products/images/")

    def __str__(self) -> str:
        return f'{self.product}'

    class Meta:
        verbose_name = "Изображения товаров"
        verbose_name_plural = "Изображения товаров"


class ProductSize(models.Model):
    """Размер товара"""
    size = models.CharField("Размер", max_length=100)
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.size

    class Meta:
        verbose_name = "Размеры товаров"
        verbose_name_plural = "Размеры товаров"
