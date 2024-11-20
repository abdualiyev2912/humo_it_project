from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="portfolio_images/")


class Developer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    skills = models.CharField(max_length=255)
    image = models.ImageField(upload_to="dev_images/", null=True, blank=True)
    experience = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}: {self.content[:50]}..."
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    

class New(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="news_images/")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='news_articles')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
