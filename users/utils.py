from .models import Profile
from django.db.models import Q

def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    userprofiles = Profile.objects.filter(Q(name__icontains=search_query) | Q(username__icontains=search_query))

    return userprofiles, search_query

