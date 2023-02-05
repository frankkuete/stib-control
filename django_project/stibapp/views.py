from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render

from stibapp.forms import UserForm, AdminForm, StationForm, LineForm, StationOrderForm, ControlForm
from stibapp.models import User, Admin, Station, Line, StationOrder, Control


# Create your views here.


def signin(request):
    if request.method == 'POST':
        pseudo = request.POST.get('pseudo')
        userpassword = request.POST.get('userpassword')
        if request.POST.get('isadmin') == 'True':
            isadmin = True
        else:
            isadmin = False
        code = request.POST.get('code')
        if pseudo and userpassword:
            if len(User.objects.filter(pseudo=pseudo)) >= 1:
                error = {'error': 'le pseudo est déja pris'}
                return render(request, 'stibapp/user_create.html', {'user_values': error})
            if isadmin:
                if code:
                    user = User.objects.create(
                        pseudo=pseudo, password=userpassword, isadmin=isadmin)
                    user.save()
                    admin = Admin.objects.create(pseudo=user, code=code)
                    admin.save()
                    return redirect('home')
                else:
                    error = {
                        'error': 'Pour etre Adminstrateur vous devez entrer un passcode'}
                    return render(request, 'stibapp/user_create.html', {'user_values': error})
            else:
                user = User.objects.create(
                    pseudo=pseudo, password=userpassword, isadmin=isadmin)
                user.save()
                return redirect('home')
    else:
        return render(request, 'stibapp/user_create.html')


def home(request):
    if request.method == 'POST':
        if request.POST.get('code'):
            pseudo = request.POST.get('adminpseudo')
            code = request.POST.get('code')
            user = User.objects.filter(pseudo=pseudo)
            if len(user) == 1:
                if len(Admin.objects.filter(pseudo=user[0]).filter(code=code)) == 1:
                    request.session["pseudo"] = pseudo
                    return redirect('dashboard')
                else:
                    error = {
                        'error': "les informations de connexion sont incorrectes "}
                    return render(request, 'stibapp/home.html', {'admin_values': error})
            else:
                error = {'error': "les informations de connexion sont incorrectes"}
                return render(request, 'stibapp/home.html', {'admin_values': error})
        else:
            pseudo = request.POST.get('pseudo')
            password = request.POST.get('password')
            if len(User.objects.filter(pseudo=pseudo).filter(password=password)) == 1:
                request.session["pseudo"] = pseudo
                return redirect('app')
            else:
                error = {'error': 'les informations de connexion sont incorrectes'}
                return render(request, 'stibapp/home.html', {'user_values': error})
    else:
        return render(request, 'stibapp/home.html')


def dashboard(request):
    sform = StationForm(request.POST)
    lform = LineForm(request.POST)
    oform = StationOrderForm(request.POST)
    blankforms = {'sform': StationForm(), 'lform': LineForm(),
                  'oform': StationOrderForm()}
    blankforms['lines'] = Line.objects.all()
    blankforms['stations'] = Station.objects.all()
    blankforms['stationorders'] = StationOrder.objects.order_by(
        'line', 'order').all()
    blankforms['pseudo'] = request.session['pseudo']
    if request.method == 'POST':
        if request.POST.get('station_name'):
            if len(Station.objects.filter(station_name=request.POST.get('station_name'))) == 1:
                blankforms['station_error_message'] = 'la station que vous essayé de creer existe déja'
                return render(request, 'stibapp/dashboard.html', blankforms)
            else:
                sform.save()
                blankforms['station_created'] = 'Station crée avec succès'
                return render(request, 'stibapp/dashboard.html', blankforms)
        elif request.POST.get('direction'):
            direction = request.POST.get('direction')
            number = request.POST.get('number')
            if len(Line.objects.filter(direction=direction).filter(number=number)) == 1:
                blankforms['line_error_message'] = 'la ligne que vous essayé de creer existe déja'
                return render(request, 'stibapp/dashboard.html', blankforms)
            else:
                lform.save()
                blankforms['line_created'] = 'ligne crée avec succès'
                return render(request, 'stibapp/dashboard.html', blankforms)
        else:
            line = Line.objects.filter(pk=request.POST.get('line'))
            station = Station.objects.filter(pk=request.POST.get('station'))
            stationorder = StationOrder.objects.filter(
                line=line[0]).filter(station=station[0])
            if len(stationorder) == 1:
                blankforms['stationorder_error_message'] = "la station que vous voulez enregistrer existe déja l'ordre sera simplement modifiée "
                StationOrderForm(request.POST, instance=stationorder[0]).save()
                return render(request, 'stibapp/dashboard.html', blankforms)
            else:
                oform.save()
                blankforms['station_order_created'] = 'Ordre de station ajouté'
                return render(request, 'stibapp/dashboard.html', blankforms)
    else:
        return render(request, 'stibapp/dashboard.html', blankforms)


def deletestation(request, id):
    station = Station.objects.get(pk=id)
    station.delete()
    return redirect('dashboard')


def deleteline(request, id):
    line = Line.objects.get(pk=id)
    line.delete()
    return redirect('dashboard')


def deletecontrol(request, id):
    control = Control.objects.get(pk=id)
    control.delete()
    return redirect('app')


def app(request):
    controls = Control.objects.all()
    cform = ControlForm()
    params = {'controls': controls, 'cform': cform,
              'pseudo': request.session['pseudo']}
    if request.method == 'POST':
        ControlForm(request.POST).save()
        return render(request, 'stibapp/application.html', params)
    else:
        return render(request, 'stibapp/application.html', params)
