from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

def teste(request):
    return HttpResponse('Minha segunda view')

def perfil(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        jsonList = []
        req = requests.get('https://api.github.com/users/'+username)
        content = req.content.decode('utf-8', 'strict')
        jsonList.append(json.loads(content))
        userData = {}
        for data in jsonList:
            userData['nome'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['blog']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'app/perfil.html', {'data': parsedData})
    #return HttpResponse(parsedData)
    