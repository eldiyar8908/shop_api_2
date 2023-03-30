from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def products_count(self):
        return self.product_set.count()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=200)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    @property
    def rating(self):
        list1 = [review.stars for review in self.review_set.all()]
        list2 = [review.text for review in self.review_set.all()]
        return round(sum(list1) / len(list1)), list2


    def __str__(self):
        return self.title


class Review(models.Model):
    CHOICES = ((i, '* ' * i) for i in range(1, 6))
    text = models.TextField(blank=True, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return self.text




