from django.db import models

# Create your models here.

class Person(models.Model):
    firstName_text = models.CharField(max_length=20)
    lastName_text = models.CharField(max_length=20)
    fullName_text = models.CharField(max_length=50)
    NickName_text = models.CharField(max_length=10)
    phone_field = models.CharField(max_length=15, null=True)
    image = models.ImageField(null=True)
    aboutMe = models.TextField(null=True)
    line = models.CharField(max_length=10)

    def __str__(self):
        return self.fullName_text

class Email(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    email_field = models.EmailField()

    def __str__(self):
        return self.email_field

class SocialContact(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20)
    link = models.URLField()

class WorkDuration(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    duration_field = models.CharField(max_length=50)

    def __str__(self):
        return self.email_field

class Work(models.Model):
    workDuration = models.ForeignKey(WorkDuration, on_delete=models.CASCADE)
    projectLink = models.URLField()
    description = models.TextField()




class FrontendSkill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill_text = models.CharField(max_length=30)

    def __str__(self):
        return self.skill_text

class BackendSkill(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill_text = models.CharField(max_length=30)

    def __str__(self):
        return self.skill_text

class ProgrammingLanguage(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill_text = models.CharField(max_length=30)

    def __str__(self):
        return self.skill_text


