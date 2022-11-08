from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
month_dict = {
    "January": 'January is the first month of the year in the Julian and Gregorian calendars .'
               'And the first of seven months to have a length of 31 days.',
    "February": 'One of the famous facts about February is that it is the shortest month of the year.',
    "March": 'The word March comes from the Roman Martius.',
    "April": 'Its name probably derives from the Latin aperire (“to open”).',
    "May": 'May is known as a month of transition. If you live in the northern hemisphere,'
           'the fresh cold winds are gone, and the rains of early spring.',
    "June": 'The June birth flower is the Rose and the Honeysuckle.',
    "July": 'July is the warmest month in the Northern Hemisphere on average.',
    "August": 'August It is the last of the summer months.',
    "September": 'Many kids begin the school year during this month.',
    "October ": 'The leaves of trees often begin to change their colors during this month.',
    "November": 'November is late autumn in the northern hemisphere '
                'where there’s a distinct chill in the air, the winds may have picked up,'
                'and the trees are steadily losing their leave.',
    "December": 'December often marks the beginning of rain, snow, and cold weather.'
}


def months(request, months):
    months_all = month_dict.get(months, None)
    if months_all:
        return HttpResponse(months_all)
    else:
        return HttpResponseNotFound(f'{months} не существует')

# def index(request, seasons):
#     if seasons == 'winter':
#         return HttpResponse('Зима – чудесное, сказочное время года.'
#                             'Это не просто мороз и холод, а приход зимы — это снег.'
#                             'Зимняя природа погружена в сладкий сон.')
#     elif seasons == 'autumn':
#         return HttpResponse('Осень – это самая прекрасная пора.'
#                             'Листья деревьев меняют свою окраску.'
#                             'Шуршит опавшая листва, как бы прощаясь с ушедшим летом.')
#     elif seasons == 'summer':
#         return HttpResponse('Летом становится по-настоящему тепло и солнечно.'
#                             'Лето - самое лучшее время для путешествий.')
#     elif seasons == 'spring':
#         return HttpResponse('Весна – не просто одно из времен года, это новая жизнь.'
#                             'Волшебная пора, когда оживает природа.'
#                             'Время прекрасного настроения, улыбок.')
#     else:
#         return HttpResponseNotFound('Данного времени года не существует!')
#


# def season(request):
#     return HttpResponse('winter, autumn, summer, spring')
#
# def winter(request):
#     return HttpResponse('Зима – чудесное, сказочное время года.'
#                         'Это не просто мороз и холод, а приход зимы — это снег.'
#                         'Зимняя природа погружена в сладкий сон.')
#
# def autumn(request):
#     return HttpResponse('Осень – это самая прекрасная пора.'
#                         'Листья деревьев меняют свою окраску.'
#                         'Шуршит опавшая листва, как бы прощаясь с ушедшим летом.')
#
# def summer(request):
#     return HttpResponse('Летом становится по-настоящему тепло и солнечно.'
#                         'Лето - самое лучшее время для путешествий.')
#
# def spring(request):
#     return HttpResponse('Весна – не просто одно из времен года, это новая жизнь.'
#                         'Волшебная пора, когда оживает природа.'
#                         'Время прекрасного настроения, улыбок.')
