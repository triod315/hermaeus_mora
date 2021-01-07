from django.shortcuts import render
from django.http import JsonResponse
from .models import Dictionary

def post_list(request):
    dictionaries=Dictionary.objects.all()
    return render(request, 'ac_template.html', {'dictionaries':dictionaries})

def check_word(line,pattern,possible_letters):
    line=line[:-1]
    if len(pattern) != len(line):
        return False

    for char in line:
        if char not in possible_letters:
            return False

    for i in range(len(pattern)):
        if pattern[i]!='*' and pattern[i]!=line[i]:
            return False
    return True


def find_words(request):
    x=0
    template_word=request.GET['template_word']
    poss_letters=request.GET['poss_leters']
    isChecked=request.GET['isChecked']
    result=""

    # Using readline()
    file1 = open('hermaeus_mora/no_load/ukrainian', 'r',  encoding='utf-8')
    count = 0

    while True:
        count += 1

        # Get next line from file
        line = file1.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break

        if check_word(line,template_word,poss_letters):
            result+=line

    file1.close()

    result=str(count)+" words checked, possible words:\n\n"+result
    data = {
        'result' : result
    }
    return JsonResponse(data)