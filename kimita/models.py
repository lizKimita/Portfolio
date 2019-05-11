from django.db import models

# Create your models here.
class languages(models.Model):
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.language

    def save_languages(self):
        self.save()

    def delete_languages(self):   
        languages.objects.filter().delete()



class User(models.Model):
    skills = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.skills

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    languages = models.ManyToManyField(languages)
    date = models.DateTimeField(auto_now_add = True)
    


    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    def delete_project(self):
        Project.objects.filter().delete()
    
    @classmethod
    def get_all(cls):
        projects = Project.objects.all()
        return projects

    class Meta:
        ordering = ['name']

