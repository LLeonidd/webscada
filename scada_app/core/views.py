from django.shortcuts import render
from django.http import JsonResponse


def main(request):
    content = {'title': 'Глвная страница'}
    return JsonResponse(content)
