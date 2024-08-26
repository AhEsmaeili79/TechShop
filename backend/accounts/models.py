from django.db import models
from django.contrib.auth.models import AbstractUser

# Date Shamsi
from django.utils import timezone
from persiantools.jdatetime import JalaliDate
import pytz

def get_persian_datetime():
    # Define the timezone for Iran
    iran_tz = pytz.timezone('Asia/Tehran')
    
    # Get the current time in UTC and convert it to Iran's timezone
    now = timezone.now().astimezone(iran_tz)
    
    # Convert to Jalali date
    persian_date = JalaliDate(now).strftime('%Y-%m-%d')
    
    # Format time in Iran's timezone
    persian_time = now.strftime('%H:%M:%S')
    
    return persian_date, persian_time

persian_date = get_persian_datetime()

# Create your models here.
class CustomUser(AbstractUser):
    Roles = (
        ('admin', 'admin'),
        ('seller', 'seller'),
        ('customer', 'customer'),
    )

    profile_image = models.ImageField(upload_to='photos/%Y/%m/%d/' ,blank=True)
    phonenumber = models.CharField(max_length=11)
    date_birth = models.DateField(blank=True,default=persian_date)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=20,blank=True)
    street = models.CharField(max_length=30,blank=True)
    floor = models.IntegerField(blank=True)
    apartment = models.IntegerField(blank=True)
    role = models.CharField(choices=Roles,default='customer',blank=False)
    zip_code = models.IntegerField(blank=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    register_date = models.DateField(default=persian_date,blank=False)
    additional_information = models.TextField(blank=True)

    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # changed related_name
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # changed related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return f'{self.username}'