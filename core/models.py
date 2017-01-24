from django.db import models

import datetime


class Route(models.Model):
    name = models.CharField(max_length=10, unique=True)
    code = models.PositiveSmallIntegerField(unique=True)
    start_url = models.CharField(max_length=255)
    normal_url = models.CharField(max_length=255)
    end_url = models.CharField(max_length=255)
    sound_folders = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.name)

    @classmethod
    def get_route(cls, code):
        return Route.objects.get(code=code)

    def get_url(self, call_state, **kwargs):
        if call_state == 'start':
            result = self.start_url.format(**kwargs)

        elif call_state == 'normal':
            result = self.normal_url.format(**kwargs)

        elif call_state == 'end':
            result = self.end_url.format(**kwargs)
        return result


class Incoming(models.Model):
    phone_number = models.CharField(max_length=20)
    route = models.ForeignKey(Route)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.phone_number

    @classmethod
    def get_record_current(cls, phone_number):
        return cls.objects.filter(phone_number=phone_number).last()

    @classmethod
    def start(cls, route, phone_number):
        record = cls.objects.create(phone_number=phone_number, route=route)
        return record

    def end(self):
        self.date_end = datetime.datetime.now()
        self.save()
