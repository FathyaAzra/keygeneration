from django.shortcuts import render

from django.http import HttpResponse

def main(request):
    context = {}
    return HttpResponse(request, 'base/keygeneration.html', context