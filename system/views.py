from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import SensorData
import requests
# Create your views here.

# def homepage(request):
#     return render(request,'index.html')

def fetch_data(request):
    url = "https://api.waziup.io/api/v2/devices/kofikofi"
    response = requests.get(url)


    data = response.json()
    sensors = data['sensors']

    # humidity
    humidity = sensors[0]['quantity_kind'] #1st data
    sensor_values = sensors[0]['value']

    hum_value = sensor_values['value'] #2nd data
    hum_date = sensor_values['timestamp'] #3rd data

    # temprature

    temprature = sensors[1]['quantity_kind'] #1st data
    sensor_values = sensors[1]['value']

    temp_value = round(sensor_values['value']) #2nd data
    temp_date = sensor_values['timestamp'] #3rd data

    # air quality
    Air = sensors[2]['quantity_kind'] #1st data
    sensor_values = sensors[2]['value']

    Air_value = sensor_values['value'] #2nd data
    Air_date = sensor_values['timestamp'] #3rd data


    #  Air qaulity
    context1 = {
    'Air':Air,
    'Air_value':Air_value,
    'Air_date':Air_date,
    }

     # noise level

    #  temprature
    context3 = {
    'temp':temprature,
    'temp_value':temp_value,
    'temp_date':temp_date,
    }

    # humidity
    context4 = {
    'humidity':humidity,
    'hum_value':hum_value,
    'hum_date':hum_date,
    }



    context={**context1,**context3,**context4}

    return render(request, 'sensor-data.html', context)




# def store_data(request):


def store_data(request):
    url = "https://api.waziup.io/api/v2/devices/kofikofi"

    # Make the HTTP GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract the device ID
        device_id = data.get("id", "Unknown")

        # Check if "sensors" data exists
        if "sensors" in data:
            for sensor in data["sensors"]:
                sensor_id = sensor.get("id", "Unknown")
                sensor_name = sensor.get("name", "Unknown")
                value = sensor.get("value", None)
                timestamp = sensor.get("timestamp", None)

                # Store parsed data in the database
                SensorData.objects.create(
                    device_id=device_id,
                    sensor_id=sensor_id,
                    sensor_name=sensor_name,
                    value=value,
                    timestamp=timestamp
                )
                sensor_data = SensorData.objects.all()
                context = {'sensor_data': sensor_data}

        return render(request, 'sensor-data.html',context)
    else:
        return render(request, 'layout.html', {"error": "Failed to fetch data"})









#----register
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'form':form}
    return render (request, 'register.html', context=context)

# ---------- Authentication starts
#-- Login
def my_login(request):
    form = LoginForm()
    if request.method =='POST':
        LoginForm(request, data=request.POST)

        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("fetch-data")

    context = {'loginform':form}
    return render(request, 'login.html',context=context)

#-- User logout
def user_logout(request):
    auth.logout(request)

    return redirect("login")

#------------- Authentication ends
