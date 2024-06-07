from django.db import models


class ProductReview(models.Model):
    POSITIVE = 'Positive'
    NEGATIVE = 'Negative'
    REVIEW_CHOICES = [
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative')
    ]

    user_email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='reviews/images/', blank=True, null=True)
    description = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    review_type = models.CharField(max_length=8, choices=REVIEW_CHOICES)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'Review by {self.user_email} with rating {self.rating}'