from django.shortcuts import render,HttpResponse
from django.http import JsonResponse,HttpResponseBadRequest
import hashlib

dist1 = {
    'number':1,

    'title':'青蛙',

    'description':'这是一个关于青蛙的谜题',

    'prize':2,

    'enterFee':0.1,

    'status':'未揭秘',

    'people':0,

    'content':'content',

    'tip':'tip',

    'answer':'answer',
}

dist2 = {
    'number':2,

    'title':'海猫',

    'description':'海猫鸣泣之时，无人生还',

    'prize':3,

    'enterFee':0.15,

    'status':'已揭秘',

    'people':333,

    'content':'content',

    'tip':'tip',

    'answer':'answer',
}

data = [dist1,dist2]

def v_default(request):
    return render(request,'index.html')
def v_mainpage(request):
    json_data = []
    for dist in data:
        d = {
            'number':dist['number'],
            'title':dist['title'],
            'description':dist['description'],
            'prize':dist['prize'],
            'enterFee':dist['enterFee'],
            'status':dist['status'],
            'people':dist['people'],
        }
        json_data.append(d)
    return JsonResponse(json_data,safe=False)
    
def v_done(request):
    number = request.data.get('number')
    for i in data:
        if data['number'] == number:
            d = data
            break
    
    json_data = {
        'content':d['content'],

        'tip':d['tip'],

        'answer':d['answer'],
    }
    return JsonResponse(json_data)

def v_join(request):
    useraddress = request.data.get('userAddress')
    
    number = request.data.get('number')
    for i in data:
        if data['number'] == number:
            d = data
            break

    json_data = {
        'content':d['content'],

        'tip':d['tip'],

        'enterFee':d['enterFee'],
    }
    return JsonResponse(json_data)

def v_answer(request):
    useranswer = request.data.get('userAnswer')
    useraddress = request.data.get('userAddress')
    number = request.data.get('number')
    for i in data:
        if data['number'] == number:
            d = data
            break
    text = useraddress + d['answer']
    hash_hex = hashlib.sha256(text.encode('utf-8')).hexdigest()
    r = True if f'{hash_hex}' == useranswer else False

    json_data = {
        'response':r
    }
    return JsonResponse(json_data)

def v_create_rid(request):

    dist = {
        'number':request.data.get('number'),

        'title':request.data.get('title'),

        'description':request.data.get('description'),

        'prize':request.data.get('prize'),

        'enterFee':request.data.get('enterFee'),

        'status':request.data.get('status'),

        'people':0,

        'content':request.data.get('content'),

        'tip':request.data.get('tip'),

        'answer':request.data.get('answer'),        
    }
    data.append(dist)
    json_data = {
        'response':True
    }
    return JsonResponse(json_data)
