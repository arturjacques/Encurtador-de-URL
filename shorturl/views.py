from django.http import HttpResponse

def oi_view(request):
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:
<meta http-equiv="refresh" content="0; URL='https://www.youtube.com/watch?v=F5mRW0jo-U4'"/>
</h1>
    """)
    