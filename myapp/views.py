from django.shortcuts import render
import pickle
import numpy as np
from .models import ContactMessage
import requests
# Load model and scaler
model = pickle.load(open('myapp/model.pkl', 'rb'))
scaler = pickle.load(open('myapp/standscaler.pkl', 'rb'))

# Optional: integer-to-crop mapping (only needed if your model predicts integers)
crop_dict = {
    1: 'Rice', 2: 'Maize', 3: 'Jute', 4: 'Cotton', 5: 'Coconut',
    6: 'Papaya', 7: 'Orange', 8: 'Apple', 9: 'Muskmelon', 10: 'Watermelon',
    11: 'Grapes', 12: 'Mango', 13: 'Banana', 14: 'Pomegranate', 15: 'Lentil',
    16: 'Blackgram', 17: 'Mungbean', 18: 'Mothbeans', 19: 'Pigeonpeas',
    20: 'Kidneybeans', 21: 'Chickpea', 22: 'Coffee'
}

def home(request):
    if request.method == 'POST':
        try:
            # Read input values
            N = float(request.POST['N'])
            P = float(request.POST['P'])
            K = float(request.POST['K'])
            temperature = float(request.POST['temperature'])
            humidity = float(request.POST['humidity'])
            ph = float(request.POST['ph'])
            rainfall = float(request.POST['rainfall'])

            # Prepare data for prediction
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            data = scaler.transform(data)

            # Make prediction
            prediction_raw = model.predict(data)[0]

            # Handle both integer or string predictions
            if isinstance(prediction_raw, int):
                prediction = crop_dict.get(prediction_raw, "Prediction not found")
            else:
                prediction = str(prediction_raw)

        except Exception as e:
            prediction = f"Error: {e}"

        return render(request, 'index.html', {'result': prediction})

    return render(request, 'index.html')
from django.shortcuts import get_object_or_404
from .models import Crop

def crop_detail(request, crop_name):
    crop = get_object_or_404(Crop, name__iexact=crop_name)
    return render(request, 'crop_detail.html', {'crop': crop})

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print(name, email, message)  # later store or email

    return render(request, "contact.html")

def contact(request):
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        success = True

    return render(request, "contact.html", {"success": success})


from django.http import JsonResponse

def get_weather(request):
    city = "Hyderabad"
    api_key = "b16bfa33241f6e08eebcccdfc7f895ca"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()

    weather = {
        "temperature": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "rainfall": response.get("rain", {}).get("1h", 0)
    }

    return JsonResponse(weather)