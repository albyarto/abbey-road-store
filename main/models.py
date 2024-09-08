from django.db import models

# Create your models here.
class AttributeEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5