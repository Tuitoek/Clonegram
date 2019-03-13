from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User)
    dpicture = models.ImageField(upload_to='prophotos/')
    username=models.CharField(max_length = 20)
    bio=models.CharField(max_length = 250)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self):
        self.update()

    @classmethod
    def search_by_username(cls, search_term):
        users=cls.objects.filter(user__username__icontains = searchterm)
        return users

class Image(models.Model):
    user = models.OneToOneField(User)
    image_name=models.CharField(max_length = 20)
    image_caption=models.CharField(max_length = 1000)
    likes=models.CharField(max_length = 1000)
    comments=models.CharField(max_length = 250)
    username=models.ForeignKey(Profile)
    image_path=models.ImageField(upload_to = 'images/')
    pub_date=models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering=['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self):
        self.update()
