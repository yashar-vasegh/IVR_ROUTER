from models import Route, Incoming
from django.http import HttpResponse

import requests
import os


def normalize(route, msg=''):
    # this is general response from router
    if route is None:
        return msg

    try:
        error, audio_file, end = msg.split(',')
    except:
        # if msg structure is not ',,,' then it should be a general message from service, return it intact
        return msg

    if error:
        error = os.path.join(route.sound_folders, error)
    if audio_file:
        audio_file = os.path.join(route.sound_folders, audio_file)
    return '%s,%s,%s' % (error, audio_file, end)


def route(request, call_state, phone_number, number):

    if call_state == 'start':
        # get route
        try:
            route_conf = Route.get_route(number)
        except Route.DoesNotExist:
            return HttpResponse(normalize(None, 'error,,'))

        # set new record for the incoming phone_number
        Incoming.start(route_conf, phone_number)
        # call related url
        response = requests.get(route_conf.get_url('start', phone_number=phone_number))

    elif call_state == 'normal':
        # get phone_number current route
        incoming = Incoming.get_record_current(phone_number)
        route_conf = incoming.route
        # call related url
        response = requests.get(incoming.route.get_url('normal', phone_number=phone_number, number=number))

    elif call_state == 'end':
        # get phone_number current route
        incoming = Incoming.get_record_current(phone_number)
        route_conf = incoming.route
        # end income
        incoming.end()
        # call related url
        response = requests.get(incoming.route.get_url('end', phone_number=phone_number, number=number))
    else:
        raise NotImplemented

    if response.status_code // 100 != 2:
        print response.text
        return HttpResponse(normalize(None, 'error,,'))
    else:
        return HttpResponse(normalize(route_conf, response.text))
