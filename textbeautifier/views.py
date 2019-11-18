# by Akram

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# def about(request):
#     return HttpResponse("about Page <br> <a href='/'>Home</a>")

# def contact(request):
#     return HttpResponse("contact Page <br> <a href='/about'>Go To About</a>")

def analyze(request):
    getText = request.POST.get('textValue', 'default')
    getCaps = request.POST.get('textCaps', 'off')
    getPunc = request.POST.get('removePunc', 'off')
    getExtra = request.POST.get('removeExtra', 'off')
    getLine = request.POST.get('removeNewline', 'off')

    if getCaps == 'on':
        getText = analyzeText = getText.upper()
    
    if getPunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzeText = ''
        for char in getText:
            if char not in punctuations:
                analyzeText = analyzeText + char
        getText = analyzeText

    if getExtra == 'on':
        analyzeText = ''
        for index, char in enumerate(getText):
            if not ( getText[index]==' ' and getText[index+1]==' ' ):
                analyzeText = analyzeText + char
        getText = analyzeText

    if getLine == 'on':
        # analyzeText = getText.replace('\n', ' ')
        analyzeText = ''
        for char in getText:
            if char !='\n' and char !='\r':
                analyzeText = analyzeText + char
        getText = analyzeText
    
    if(getCaps=='on' or getPunc == 'on' or getExtra == 'on' or getLine == 'on'):
        analyzeText = analyzeText
    else:
        analyzeText = getText
        
    params = {'purpose': 'Analyze Text', 'analyzeText': analyzeText }
    return render(request, 'analyze.html', params)