from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from app.chatgpt.models import ChatgptAccount


class User(AbstractUser):
    model_limit = models.JSONField(default=list, verbose_name="Remark")
    remark = models.TextField(blank=True, verbose_name="Remark")
    isolated_session = models.BooleanField(default=True, verbose_name="Self-Session")
    gptcar_list = models.JSONField(default=list)
    expired_date = models.DateField(blank=True, null=True, verbose_name="Exp. Date")


class VisitLog(models.Model):
    # user = models.ForeignKey(User, db_constraint=False, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=150, verbose_name="Name")
    chatgpt_username = models.CharField(max_length=150, null=True, verbose_name="chatgpt")
    log_type = models.CharField(max_length=20, verbose_name="Login Type")
    created_at = models.IntegerField(verbose_name="Login Time")
    ip = models.GenericIPAddressField(verbose_name="Login IP")
    user_agent = models.TextField(verbose_name="User-Agent")

    @classmethod
    def save_data(cls, data):
        obj = cls.objects.create(**data)
        return obj
