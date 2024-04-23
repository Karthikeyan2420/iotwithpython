from django.shortcuts import render

# led_control_app/views.py
from django.http import HttpResponse
from pyfirmata import Arduino

# Initialize Arduino board
board = Arduino('COM3')  # Adjust the port accordingly
led_pin = 12  # Assuming the LED is connected to pin 12
board.digital[led_pin].mode = 1  # Set pin mode to OUTPUT

def turn_on(request):
    board.digital[led_pin].write(1)
    return HttpResponse("LED is ON")

def turn_off(request):
    board.digital[led_pin].write(0)
    return HttpResponse("LED is OFF")

def index(request):
    return render(request,"index.html")




