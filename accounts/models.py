from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    class Roles(models.TextChoices):
        Admin='ADMIN','Admin'
        Customer = "CUSTOMER", "Customer"
        Employee="EMPLOYEE", "Employee"
    roles=models.CharField(max_length=255,choices=Roles.choices,default=Roles.Employee)
    
    def __str__(self):
        return self.username
    
    class job_titles(models.TextChoices):
        backend='BACKEND','Backend'
        frontend='FRONTEND','Frontend'
        fullstack='FULLSTACK','Fullstack'
        devops='DEVOPS','Devops'
        QA_Engineer='QA_ENGINEER','QA Engineer'
        UX_UI_Designer='UX/UI_DESIGNER','UX/UI Designer'
        product_manager='PRODUCT_MANAGER','Product Manager'        
        project_manager='PROJECT_MANAGER','Project Manager'
        data_scientist='DATA_SCIENTIST','Data Scientist'
        technical_lead='TECHNICAL_LEAD','Technical Lead'
        client='CLIENT','Client'
    job_title = models.CharField(max_length=255,choices=job_titles.choices,blank=True,null=True)
    