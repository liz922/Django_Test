# from django.http import HttpResponse
# from django.template import Context
# from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    current_date = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render_to_response('dateapp/current_datetime.html', locals())

def hours_ahead(request, offset):
    hour_offset = int(offset)
    next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)
    return render_to_response('dateapp/hours_ahead.html', locals())
