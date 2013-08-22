# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.utils import simplejson


def event_serializer(events):
    """
    serialize event model
    """
    objects_body = []

    for event in events:
        field = {
            "id": event.pk,
            "title": event.title,
            "url": event.url,
            "class": event.css_class,
            "start": event.start_timestamp,
            "end": event.end_timestamp
        }
        objects_body.append(field)
    objects_head = {"success": 1}
    objects_head["result"] = objects_body
    return simplejson.dumps(objects_head, encoding='utf-8')
