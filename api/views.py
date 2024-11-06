from django.shortcuts import render

# Initialize supabase client
from supabase import create_client, Client
from decouple import config


url: str = config("SUPABASE_URL")
key: str = config("SUPABASE_KEY")
supabase: Client = create_client(url, key)

#print(f'Printing {url}, {key}')
def index(request):
    response = supabase.table("user_profile").select("*").execute()
    context = {'response':response}
    #print(f'context data type: {type(context)}')
    return render(request, 'api/index.html', context)
