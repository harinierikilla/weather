import requests
from django.shortcuts import render

def weather_view(request):
    weather_data = {}
    if request.method == "POST":
        city = request.POST.get('city')
        api_key = '4857d3e15e06544b6e240e311e0acbc4'  # Replace with your actual API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"error": "City not found."}
    return render(request, 'myapp/weather.html', {'weather_data': weather_data})
