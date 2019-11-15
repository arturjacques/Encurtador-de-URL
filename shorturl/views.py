from django.http import HttpResponse
import funcoes


def view_1(request):
    funcoes.add_visita('1')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_2(request):
    funcoes.add_visita('2')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://google.com
<meta http-equiv="refresh" content="0; URL='http://google.com'"/>
</h1>
    """)
    
def view_3(request):
    funcoes.add_visita('3')
    return HttpResponse("""
<h1>
301 Redirect <br>
Location:http://pudim.com
<meta http-equiv="refresh" content="0; URL='http://pudim.com'"/>
</h1>
    """)
    