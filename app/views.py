import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from django.shortcuts import render

from django.http import HttpResponse
import pandas_profiling
from pydantic_settings import BaseSettings


def index(request):
    return render(request, 'app/index.html')

def load_data(request):
    if request.method == 'POST':
        csv_path = request.POST.get('csv_path')
        try:
            df = pd.read_csv(csv_path)
            request.session['df'] = df.to_json()
            return render(request, 'app/functions.html')
        except Exception as e:
            return render(request, 'app/index.html', {'error': str(e)})
    return render(request, 'app/index.html')

def explore_data(request):
    df = pd.read_json(request.session.get('df'))
    head = df.head().to_html()
    tail = df.tail().to_html()
    # info = df.info().to_html()
    describe = df.describe().to_html()
    context = {'head': head, 'tail': tail,'describe': describe}
    return render(request, 'app/explore_data.html', context)

def explore_more(request):
    df = pd.read_json(request.session.get('df'))
    head = df.head().to_html()
    tail = df.tail().to_html()
    # info = df.info().to_html()
    describe = df.describe().to_html()
    context = {'head': head, 'tail': tail,'describe': describe}
    return render(request, 'app/explore_more.html', context)


def explore_more(request):
    if 'df' in request.session:
        df = pd.read_json(request.session.get('df'))
        profile_report = df.profile_report()
        html = profile_report.to_html()
        return HttpResponse(html)
    else:
        return render(request, 'app/explore_data.html', {'error': 'No data loaded.'})