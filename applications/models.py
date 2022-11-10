from django.db import models

class Application(models.Model):

    application_url = models.URLField()
    date_applied = models.DateField()
    date_logged = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'users.User', related_name='applications', on_delete=models.CASCADE)    
    notes = models.TextField(max_length=250)

    APPLIED = 'Applied'
    INTERVIEWED = 'Interviewed'
    REJECTED = 'Rejected'
    STATUS_CHOICES = [
        (APPLIED, 'Applied'),
        (INTERVIEWED, 'Interviewed'),
        (REJECTED, 'Rejected')
    ]

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0]
    )

    def __str__(self):
        return f"{self.owner} logged this application on {self.date_logged}. This url was logged with it: {self.application_link}."

    class Meta:
        ordering = ['-date_logged']


class Company(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.SlugField(max_length=15).blank = True
    address = models.CharField(max_length=100).blank = True
    website = models.CharField(max_length=100).blank = True

    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact(models.Model):
    title = models.CharField(max_length=100).blank = True
    name = models.CharField(max_length=100).blank = True
    phone_number = models.SlugField(max_length=15).blank = True
    email = models.EmailField(max_length=100).blank = True
    notes = models.TextField(max_length=250).blank = True

    def __str__(self):
        if self.title and self.name:
            return f'Point of contact: {self.name}, {self.title}.'
        elif self.title and not self.name:
            return f'Point of contact: {self.title}.'
        elif self.name and not self.title:
            return f'Point of contact: {self.name}.'
        else:
            return f'No Point of Contact found!"'

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
