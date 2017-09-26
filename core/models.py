from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_1 = PhoneNumberField()
    phone_2 = PhoneNumberField(blank=True)
    office_cood_x = models.DecimalField(max_digits=7, decimal_places=4)
    office_cood_y = models.DecimalField(max_digits=7, decimal_places=4)
    
    def __str__(self):
        return self.user.first_name

class TowingCo(models.Model):
    company_name = models.CharField(max_length=255)
    phone_1 = PhoneNumberField()
    phone_2 = PhoneNumberField(blank=True)
    
    def __str__(self):
        return self.company_name
    
class TowingVehicle(models.Model):
    towco = models.ForeignKey(TowingCo, on_delete=models.PROTECT)
    mobile_1 = PhoneNumberField()
    mobile_2 = PhoneNumberField(blank=True)
    loc_cood_x = models.DecimalField(max_digits=7, decimal_places=4)
    loc_cood_y = models.DecimalField(max_digits=7, decimal_places=4)
    
    def __str__(self):
        return self.user.first_name
    

class SparesDealer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_1 = PhoneNumberField()
    phone_2 = PhoneNumberField(blank=True)
    
    def __str__(self):
        return self.user.first_name

class CabCo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_1 = PhoneNumberField()
    phone_2 = PhoneNumberField(blank=True)
    
    def __str__(self):
        return self.user.first_name

class Requester(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_cood_x = models.DecimalField(max_digits=7, decimal_places=4)
    home_cood_y = models.DecimalField(max_digits=7, decimal_places=4)
    mobile_1 = PhoneNumberField()
    mobile_2 = PhoneNumberField(blank=True)

    def __str__(self):
        return self.user.first_name
    
##########################

class QuerySession(models.Model):
    requester = models.ForeignKey(Requester, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=255)
    service_code = models.CharField(max_length=255)
    status = models.BooleanField(default=True) #active or ended
    loc_cood_x = models.DecimalField(max_digits=7, decimal_places=4)
    loc_cood_y = models.DecimalField(max_digits=7, decimal_places=4)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.session_id
    

class Query(models.Model):
    session = models.ForeignKey(QuerySession, on_delete=models.CASCADE)
    request = models.TextField()
    reply = models.TextField()
    seq_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s, %s"%(self.session, self.seq_id)
    