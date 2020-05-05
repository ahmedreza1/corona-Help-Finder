from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import PermissionDenied

# Create your models here.
class State(models.Model):
	state = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{}'.format(self.state)

	class Meta:
		verbose_name_plural = 'states'


# The orginisation model.
class MyProfile(models.Model):
	name = models.CharField(max_length = 500)
	user = models.OneToOneField(to=User, on_delete=CASCADE)
	address = models.TextField(null=True, blank=True)
	gender = models.CharField(max_length=20, default="Male", choices=(("Male", 'Male'), ("Female", "Female"), ("LGBTQ", "LGBTQ")))
	phone_no = models.CharField(max_length=15, null=True, blank=True)
	description = models.CharField(max_length = 240, null=True, blank=True)
	pic = models.URLField(null=True, blank=True)
	donation_given = models.IntegerField(null=True, blank=True)
	donation_recived = models.IntegerField(null=True, blank=True)
	mail = models.URLField(null=True, blank=True)
	purpose = models.TextField(null=True, blank=True)

	def __str__(self):
		return "%s" % self.user

# The orginisation Work model.
class MyPost(models.Model):
	pic_one = models.URLField(null=True, blank=True)
	pic_two = models.URLField(null=True, blank=True)
	pic_three = models.URLField(null=True, blank=True)
	pic_four = models.URLField(null=True, blank=True)
	pic_five = models.URLField(null=True, blank=True)
	main_pic = models.URLField(null=True, blank=True)
	amount_spend = models.IntegerField(null=True, blank=True)
	total_donars = models.IntegerField(null=True, blank=True)
	donar_names = models.TextField(null=False, blank=False)
	title = models.CharField(max_length = 200)
	body = models.TextField(null=False, blank=False)
	short_description = models.CharField(max_length = 240)
	cr_date = models.DateTimeField(auto_now_add=True)
	uploaded_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, null=True, blank=True)
	def __str__(self):
		return "%s" % self.title


# The orginisation Bank Account Details model.
class MyPayment(models.Model):
	account_num = models.IntegerField(null=False, blank=False)
	bank_name = models.CharField(max_length = 240, null=False, blank=False)
	ifsc = models.CharField(max_length = 240, null=False, blank=False)
	beneficiary_name = models.CharField(max_length = 240, null=False, blank=False)
	author = models.ForeignKey(to=MyProfile, on_delete=CASCADE, null=True, blank=True)
	def __str__(self):
		return "%s" % self.account_num

# The Fake whatsapp forward model
class FakeCheck(models.Model):
	msg = models.TextField(null=False, blank=False)
	def __str__(self):
		return "%s" % self.msg