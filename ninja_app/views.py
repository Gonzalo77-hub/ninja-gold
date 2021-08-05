from django.shortcuts import redirect, render, HttpResponse
import random
def index(request):
    return render(request, 'index2.html')



def money(request):
    if not request.session['list']:
        request.session['list'] = []
    if 'cont' in request.session:
        if request.POST['ninja'] == 'Farm':
            a =random.randint(10,20)
            request.session['cont'] += a
            diccionario = { 'texto': f'¡¡¡Ganaste {a} monedas de oro!!!', 'color': 'verde' }
            request.session['list'].append(diccionario)
        if request.POST['ninja'] == 'Cave':
            a = random.randint(5,10)
            request.session['cont'] += a
            diccionario = { 'texto': f'¡¡¡Ganaste {a} monedas de oro!!!', 'color': 'verde' }
            request.session['list'].append(diccionario)
        if request.POST['ninja'] == 'House':
            a = random.randint(2,5)
            request.session['cont'] += a
            diccionario = { 'texto': f'¡¡¡Ganaste {a} monedas de oro!!!', 'color': 'verde' }
            request.session['list'].append(diccionario)
        if request.POST['ninja'] == 'Casino':
            a = random.randint(1,2)
            if a == 1:
                b = random.randint(50,60)
                request.session['cont'] += b
                diccionario = { 'texto': f'¡¡¡Ganaste {b} monedas de oro!!!', 'color': 'verde' }
                request.session['list'].append(diccionario)
            else:
                b = random.randint(50,60)
                request.session['cont'] -= b
                diccionario = { 'texto': f'¡¡¡Perdiste {b} monedas de oro!!!', 'color': 'rojo' }
                request.session['list'].append(diccionario)

    else:
        request.session['cont'] = 0
    return redirect("/")

def restaurar(request):
    request.session['cont']=0
    request.session['list'] = []
    return redirect("/")