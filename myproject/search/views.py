from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank

from .models import UserMeta

@login_required(login_url="/users/login/")
def search_view(request):
    q = request.GET.get('q')

    if q:
        vector = SearchVector('user__username')
        query = SearchQuery(q)

        metadatas = UserMeta.objects.annotate(search=vector).filter(search=query)
    else:
        metadatas = UserMeta.objects.all()

    context = {'metadatas': metadatas}
    return render(request, 'search/search.html', context)