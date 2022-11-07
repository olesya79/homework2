from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def season(request):
    return HttpResponse('winter, autumn, summer, spring')

def winter(request):
    return HttpResponse('Зима – чудесное, сказочное время года.'
                        'Это не просто мороз и холод, а приход зимы — это снег.'
                        'Зимняя природа погружена в сладкий сон.')

def autumn(request):
    return HttpResponse('Осень – это самая прекрасная пора.'
                        'Листья деревьев меняют свою окраску.'
                        'Шуршит опавшая листва, как бы прощаясь с ушедшим летом.')

def summer(request):
    return HttpResponse('Летом становится по-настоящему тепло и солнечно.'
                        'Лето - самое лучшее время для путешествий.')

def spring(request):
    return HttpResponse('Весна – не просто одно из времен года, это новая жизнь.'
                        'Волшебная пора, когда оживает природа.'
                        'Время прекрасного настроения, улыбок.')
