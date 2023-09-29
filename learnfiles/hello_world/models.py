from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
# Create your models here.


class Info(models.Model):
    GENDER_CHOICE = (
        ("male", "آقا"),
        ("female", "خانم"),
    )
    
    STATUS_CHOICE =(
        ("draft", "آماده انتشار"),
        ("create" , "ساخته شده"),
        ("published" , ("انتشار یافته"))
    )
    
    first_name = models.CharField(max_length=100, null=False , verbose_name = "نام")
    last_name = models.CharField(max_length=100, null=False , verbose_name = " نام خانوادگی")
    age = models.IntegerField(verbose_name = "سن")
    username = models.CharField(max_length=12 , verbose_name = "نام کاربری")
    gender = models.CharField(choices=GENDER_CHOICE , verbose_name = "جنسیت")
    created = jmodels.jDateTimeField(auto_now_add=True , verbose_name = "ساخته شده")
    publish = jmodels.jDateTimeField(default=timezone.now , verbose_name = " انتشار یافته در")
    status = models.CharField(choices = STATUS_CHOICE , default="draft" , verbose_name = "وضعیت")


    class Meta():
        verbose_name = "مشخصات"
        verbose_name_plural = " تمام مشخصات"
    # def __str__(self):
    #     return "object hay ma  (username={}  ,  first name  = {}  , age= {} )".format(self.username, self.f_name, self.age)

    def __str__(self):
        return ("First name is \n %s and age is %d " % (self.first_name, self.age))
    
    
 
