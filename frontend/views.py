from django.shortcuts import render,HttpResponse
from django.http import JsonResponse,HttpResponseBadRequest

def v_default(request):
    return render(request,'index.html')
def v_mainpage(request):
    dist1 = {
        'number':1,

        'title':'青蛙',

        'description':'这是一个关于青蛙的谜题',

        'prize':2,

        'enterFee':0.1,

        'status':'未揭秘',

        'people':0,
    }

    dist2 = {
        'number':2,

        'title':'海猫',

        'description':'海猫鸣泣之时，无人生还',

        'prize':3,

        'enterFee':0.15,

        'status':'已揭秘',

        'people':333,
    }

    data = [dist1,dist2]
    return JsonResponse(data,safe=False)
    
def v_done(request):
    data = {
        'content':'content',

        'tip':'tip',

        'answer':'answer',
    }
    return JsonResponse(data)

def v_join(request):
    useraddress = request.POST.get('userAddress')
    data = {
        'content':'content',

        'tip':'tip',

        'enterFee':'enterFee',
    }
    return JsonResponse(data)

def v_answer(request):
    useranswer = request.POST.get('userAnswer')
    data = {
        'response':False
    }
    return JsonResponse(data)

def v_create_rid(request):
    '''
    data = {
        'title':'title',
        'content':'content',
        'answer':'answer',
        'tip':'tip',
        'description':'description',
        'prize':1,
        'enterFee':1
    }
    '''
    data = {
        'response':False
    }
    return JsonResponse(data)
'''
def create_riddle(request):
    return HttpResponse('hi')

def create_riddle(request):
    return HttpResponse('hi')
'''