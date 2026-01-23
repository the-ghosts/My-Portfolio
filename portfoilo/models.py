from django.db import models


class MyProject(models.Model):
    title = models.CharField(max_length=200) # e.g. "Road Traffic Offence System"
    description = models.TextField() # Why you built it and what it does
    image = models.ImageField(upload_to='portfolio_image/') # A screenshot
    github_link = models.URLField(max_length=500) # Link to your code
    live_demo_link = models.URLField(blank=True, null=True) # Link to the website (if live)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

# Create your models here.
