from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.utils.dateparse import parse_date
from .models import UserMeta

@login_required(login_url="/users/login/")
def search_view(request):
    # Get search and filter parameters from request
    q = request.GET.get("q", "")  # General search query
    username_contains = request.GET.get("username_contains", "")
    questions_contains = request.GET.get("questions_contains", "")
    session_info_contains = request.GET.get("session_info_contains", "")
    created_at_min = request.GET.get("created_at_min", "")
    created_at_max = request.GET.get("created_at_max", "")
    updated_at_min = request.GET.get("updated_at_min", "")
    updated_at_max = request.GET.get("updated_at_max", "")

    # Start with all UserMeta objects
    metadatas = UserMeta.objects.all()

    # Apply full-text search if query is provided
    if q:
        vector = SearchVector("user__username", "questions", "session_info")
        query = SearchQuery(q)

        metadatas = metadatas.annotate(
            rank=SearchRank(vector, query)
        ).filter(rank__gte=0.001).order_by("-rank")

    # Apply additional filters
    if username_contains:
        metadatas = metadatas.filter(user__username__icontains=username_contains)
    if questions_contains:
        metadatas = metadatas.filter(questions__icontains=questions_contains)
    if session_info_contains:
        metadatas = metadatas.filter(session_info__icontains=session_info_contains)

    # Apply date range filters
    if created_at_min:
        metadatas = metadatas.filter(created_at__gte=parse_date(created_at_min))
    if created_at_max:
        metadatas = metadatas.filter(created_at__lte=parse_date(created_at_max))
    if updated_at_min:
        metadatas = metadatas.filter(updated_at__gte=parse_date(updated_at_min))
    if updated_at_max:
        metadatas = metadatas.filter(updated_at__lte=parse_date(updated_at_max))

    # Context to send to template
    context = {
        "metadatas": metadatas,
        "query": q,
        "username_contains": username_contains,
        "questions_contains": questions_contains,
        "session_info_contains": session_info_contains,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
    }

    return render(request, "search/search.html", context)
