from .models import Profile

def searchProfiles(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    userprofiles = Profile.objects.filter(name__icontains=search_query)

    return userprofiles, search_query

