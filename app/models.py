from django.db import models

from django.db import models

# User qismi
#
# Subject_CHOICES = (
#     ("1", "Ingliz"),
#     ("2", "Matematika"),
#     ("3", "Rus tili"),
#     ("4", "Python"),
#     ("5", "Java"),
#     ("6", "Frontend"),
# )
#
# Language_CHOICES = (
#     ("1", "Ingliz"),
#     ("2", "Matematika"),
#     ("3", "Rus tili"),
#     ("4", "Python"),
#     ("5", "Java"),
#     ("6", "Frontend"),
# )


class User(models.Model):
    class ChoiceLanguage(models.TextChoices):
        Ingliz = 'Ingliz'
        Rustili = 'Rustili'
        Python = 'Koreystili'
        Java = 'Yapontili'
        Matematika = 'Matematika'
        Fizlika = 'Fizika'
        Biologiya = 'Biologiya'
        Kimyo = 'Kimyo'
    class ChoiceSubject(models.TextChoices):
        Til = 'Til'
        Aniqfanlar = 'Aniq fanlar'
        Dasturlash = 'Dasturlash'
        Tabiyfanlar = 'Tabiy fanlar'
    image = models.ImageField(upload_to='image/')
    username =models.CharField(max_length=55)
    familiya = models.CharField(max_length=55)
    tugilgan_yil = models.DateTimeField()
    subject = models.CharField(max_length=25 ,choices= ChoiceSubject.choices, default=ChoiceSubject.Tabiyfanlar )
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=13)
    telegramORnumber = models.CharField(max_length=13)
    tajriba = models.CharField(max_length=20)
    qayerda_oqigan = models.CharField(max_length=55)
    language = models.CharField(max_length=25 ,choices= ChoiceLanguage.choices, default=ChoiceLanguage.Biologiya)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    resume = models.FileField(upload_to='resume/')
    sertificat = models.FileField(upload_to='resume/')
    address = models.CharField(max_length=155)
    descrption = models.TextField(max_length=1000)
