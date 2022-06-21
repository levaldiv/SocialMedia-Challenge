from django.db import models
from django.contrib.auth import get_user_model
import uuid # unique id
from datetime import datetime

# retrieving the model of the currently authenticated user
User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #foreign key that will link to the modal
    id_user = models.IntegerField() #id of the user with the profile
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blankuser.jpeg') #specifing where to upload the img
    location = models.CharField(max_length=100, blank=True)

    # this will show the username in the admin panel 
    def __str__(self):
        return self.user.username

# Creating the post fucntion
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4) # iddentification of each of tthe objects
    user = models.CharField(max_length=100) # username of post owner
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

# Creating the like function
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# Follow / unfollow
class FollowerCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user