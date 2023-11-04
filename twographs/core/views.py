from django.shortcuts import render
from django.http import HttpResponse
import core.backend as backend

def index(request):
    graphs = [
        {
            "title": "Where do we see them?",
            "text": "UFO sightings frequency can be seen on this map. From the chart, we can see that most sightings are within major population centers, with California being an outlier at nearly double the sightings as compared to the next most frequent state.",
            "id": 1
        },
        {
            "title": "What are people saying about them?",
            "text": "Based on all survey responses that contained comments, we can see what the most common descriptors were.",
            "id": 2
        }
    ]
    return render(request, 'index.html', {"graphs": graphs})

def api(request):
    params = request.GET.dict()
    graph = int(params.get('graph'))
    fig = backend.get_data(graph).to_html(include_plotlyjs='cdn', full_html=False)
    return HttpResponse(fig)
