from django.db import models

# Create your models here.


class userInfo(models.Model):
    userId = models.IntegerField()
    userName = models.CharField(max_length=30)
    userIdentity = models.IntegerField()
    userPassword = models.CharField(max_length=20, default="123456")
    userSex = models.CharField(max_length=10)
    userEduBack = models.CharField(max_length=10)
    userTechPost = models.CharField(max_length=10,default="讲师")


class taskInfo(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=50)
    task_category = models.CharField(max_length=50)
    task_rank = models.CharField(max_length=50)
    principle_id = models.IntegerField()
    if_ratify = models.IntegerField(default=0)


class budget(models.Model):
    task_id = models.IntegerField()
    b1_1 = models.CharField(max_length=10,default=0)
    b1_2 = models.CharField(max_length=10,default=0)
    b1_3 = models.CharField(max_length=10,default=0)
    b2 = models.CharField(max_length=10,default=0)
    b3 = models.CharField(max_length=10,default=0)
    b4 = models.CharField(max_length=10,default=0)
    b5 = models.CharField(max_length=10,default=0)
    b6 = models.CharField(max_length=10,default=0)
    b7 = models.CharField(max_length=10,default=0)
    b8 = models.CharField(max_length=10,default=0)
    b9 = models.CharField(max_length=10,default=0)
    total = models.CharField(max_length=10)
    remaining = models.CharField(max_length=10)


class budget_out(models.Model):
    task_id = models.IntegerField()
    user_id = models.IntegerField()
    number = models.CharField(max_length=10)
    to_credit_card = models.CharField(max_length=20)
    type = models.CharField(max_length=10)


class task_user(models.Model):
    task_id = models.IntegerField()
    user_id = models.IntegerField()
    order = models.IntegerField()
    class Meta:
        unique_together = ["task_id", "user_id"]


class message(models.Model):
    sender = models.IntegerField()
    receiver = models.IntegerField()
    content = models.TextField()


class teacher_student(models.Model):
    teacher = models.IntegerField()
    student = models.IntegerField()
    class Meta:
        unique_together = ["teacher", "student"]


class property(models.Model):
    proposer = models.IntegerField()
    purchase_time = models.CharField(max_length=30)
    property_name = models.CharField(max_length=30)
    scrap_time = models.CharField(max_length=30, null=True)
    status = models.IntegerField()
    price = models.CharField(max_length=10,default=0)
    task_id = models.IntegerField()


class purchase(models.Model):
    proposer = models.IntegerField()
    property_name = models.CharField(max_length=30)
    detail_info = models.TextField()
    price = models.CharField(max_length=10)
    if_ratify = models.IntegerField()
    task_id = models.IntegerField()


class JournalArticle(models.Model):
    title = models.CharField(max_length=50)
    author_id = models.IntegerField()
    journal_name = models.CharField(max_length=50)
    publish_time = models.CharField(max_length=20)
    roll_num = models.IntegerField()
    start_end_page = models.CharField(max_length=20)
    task_id = models.IntegerField()


class Patent(models.Model):
    patent_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    patent_num = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    apply_for_time = models.CharField(max_length=50)
    take_effect_time = models.CharField(max_length=50)
    task_id = models.IntegerField()
    author_id = models.IntegerField()


class ConferenceArticle(models.Model):
    article_title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    confer_name = models.CharField(max_length=50)
    confer_time = models.CharField(max_length=50)
    publish_time = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    task_id = models.IntegerField()
    author_id = models.IntegerField()


class AcademicMonograph(models.Model):
    title = models.CharField(max_length=50)
    author_id = models.IntegerField()
    editor = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    publish_time = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    task_id = models.IntegerField()


class SoftwarePatent(models.Model):
    name = models.CharField(max_length=50)
    author_id = models.IntegerField()
    register_num = models.CharField(max_length=50)
    method = models.CharField(max_length=50)
    finish_time = models.CharField(max_length=50)
    task_id = models.IntegerField()