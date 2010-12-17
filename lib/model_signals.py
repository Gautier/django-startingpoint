# python
import datetime

def update_modify_date(sender, instance, **kwargs):
    instance.modify_date = datetime.datetime.now()