from django.db import models

class TimeStampModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True # don't create table in DB
        

class Category(TimeStampModel):
    name=models.CharField(max_length=100)
    icon=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering=["name"]
    
        verbose_name="categories"
        verbose_name_plural="Categories" #add this line

class Tag(TimeStampModel):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(TimeStampModel):
    STATUS_CHOICES=[
        ("active","Active"),
        ("in_active","Inactive")
    ]

    title=models.CharField(max_length=200)
    content=models.TextField()
    featured_image=models.ImageField(upload_to="post_images/%Y/%m/%d",blank=False)
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES,default="active")
    views_count=models.PositiveBigIntegerField(default=0)
    published_at=models.DateTimeField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
class Advertisement(TimeStampModel):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="advertisements/%Y/%m/%d",blank=False)

    def __str__(self):
        return self.title
    
class Contact(TimeStampModel):
    message=models.TextField()
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=["created_at"] #Contact.objects.all()==> order_by("created_at")

class UserProfile(TimeStampModel):
    user=models.OneToOneField("auth.User",on_delete=models.CASCADE)
    image=models.ImageField(upload_to="user_images/%Y/%m/%d",blank=False)
    address=models.CharField(max_length=200)
    biography=models.TextField()

    def __str__(self):
        return self.user.username
    
class Comment(TimeStampModel):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    content= models.TextField()

    def __str__(self):
        return f"{self.content[:50]}|{self.user.username}"

# Post - Author
# 1 author can add M posts => M
# 1 post is associated to only 1 author => 1


# 1 category can have M posts => M
# 1 post is associated to only 1 category => 1



# Tag - Post
# 1 tag can have M posts => M
# 1 post can have M tags => M
## 1 - 1 Relationship
# 1 user can have 1 profile => 1
# 1 profile is associated to 1 user  => 1
# OneToOneField() => Can be used in Any Model


## 1 - M Relationship
# 1 user can post M post  => M
# 1 post is associated to only 1 user => 1
# In django use ForeignKey() => Must be used in Many side

# 1 category can have M posts => M
# 1 post is associated to only 1 category => 1


# 1 tag can have M posts => M
# 1 post can have M tags => M


## M - M Relationship
# 1 student can learn from M teachers => M
# 1 teacher can teach M students => M
# ManyToManyField() => Can be used in Any Model

# 1 post can contain M tag => M
# 1 tag can be used in M post => M

# 1 post can be associated to only 1 category => 1
# 1 category can contains M post => M