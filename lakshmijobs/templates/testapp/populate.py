import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','lakshmijobs.settings')
import django
django.setup()
from fake import Faker
from testapp.models import HydJobs
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('project manager','team lead','software engineer','hr','associated engineer'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=fake.phonenumber()
        hyd_jobs_record= HydJobs.obects.get_or_create(
           date=fdate,
           company=fcompany,
           title=ftitle,
           address=faddress,
           email=femail,
           phonenumber=fphonenumber
        )
    n=int(input('enter number of records:'))
    populate(n)
    print(f'{n} records inserted successfully........')
