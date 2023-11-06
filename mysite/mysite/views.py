from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the Text
    djtext = request.POST.get('text', 'default')
    
    # Get Check box values
    remove_punctuation = request.POST.get('removepunc', 'off')
    count_words = request.POST.get('count', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    upper = request.POST.get('Upper', 'off')
    newline_remover = request.POST.get('newline', 'off')
    lower = request.POST.get('lower', 'off')
    
    # Initialize variables to store results
    analyzed_text = djtext

    if remove_punctuation == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed_text = ''.join(char for char in analyzed_text if char not in punctuations)

    if count_words == "on":
        word_list = analyzed_text.split()
        word_count = len(word_list)
        analyzed_text = f"Word Count: {word_count}"

    if capitalize == "on":
        analyzed_text = analyzed_text.capitalize()

    if upper == "on":
        analyzed_text = analyzed_text.upper()

    if newline_remover == "on":
        analyzed_text = analyzed_text.replace(" ", "")

    if lower == "on":
        analyzed_text = analyzed_text.lower()

    if remove_punctuation == "off" and count_words == "off" and capitalize == "off" and upper == "off" and newline_remover == "off" and lower == "off":
        return HttpResponse("<h1> <strong> Please Select at least one option </strong> </h1>")
    
    result_dict = {'purpose': 'Result', 'analyzed_text': analyzed_text}
    return render(request, 'analyzed.html', result_dict)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')