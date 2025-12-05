from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Games(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    fake_price = models.PositiveIntegerField()
    game_id = models.CharField(max_length=50)
    genre = models.CharField(max_length=100)
    multi_tags = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="games")

    def __str__(self):
        return self.title