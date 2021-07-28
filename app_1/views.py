from datetime import datetime, timedelta

from django.shortcuts import render


def home_page(request):
    today = datetime.today()
    t = timedelta((2 + today.weekday()) % 7)
    start_of_the_week = today + t
    end_of_the_week = start_of_the_week + timedelta(days=6)
    return render(request, 'index.html',
                  {'start_of_the_week': start_of_the_week.strftime('%Y-%m-%d'), 'end_of_the_week': end_of_the_week.strftime('%Y-%m-%d')},
                  status=200)
