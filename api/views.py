from django.shortcuts import render
#from django.http import HttpResponse
# Initialize supabase client
from supabase import create_client, Client
from decouple import config


url: str = config("SUPABASE_URL")
key: str = config("SUPABASE_KEY")
supabase: Client = create_client(url, key)
#print(f'Printing {url}, {key}')


def index(request):
    response = supabase.table("user_profile").select("email, job_preferences").execute()
    # Access only the data part of the response
    data = response.data  # This will exclude the count metadata entirely
    for i,j in enumerate(data):
        print(i,j)
    context = {'response': data}
    #print(f'context data type: {type(context)}')
    return render(request, 'api/index.html', context)
