from django.shortcuts import render, redirect
from .models import Contact, Ahmedabad, Gandhinagar
from .forms import Cform, Bform
import yagmail, time, requests, json
from boltiot import Bolt

def home(request):
    a =  Cform(request.POST)
    if a.is_valid():
        b = request.POST.copy()
        name = b.get("Name")
        email = b.get("Email")
        sub = b.get("Subject")
        message = b.get("Contents")
        msg = "This is a computer generated mail. Please do not reply."
        cont = "Greetings from SPark!!\n\nDear "+ name + ",\nThank you for visiting our website and to contact us. Here is the attached copy of your message that you sent us:\n"+message+"\n\nTeam SPark,\nGEC, GN\n\n"+msg
        yagmail.SMTP("info.spark.gecgn@gmail.com").send(to=email, subject=sub, contents=cont)
        a.save()
    return render(request, 'home.html', {'key': a})

def availability(request):
    a = Ahmedabad.objects.all()
    b = Gandhinagar.objects.all()
    return render(request, 'places.html', {'keya': a, 'keyg': b})

def booking(request):
    api_key = "9b21f2d6-b8b2-4d59-9892-442b41b97b20"
    bolt_id = "BOLT10922204"
    status_list = ['Available', 'Occupied', 'Booked']
    status = 0
    p_sen = Bolt(api_key, bolt_id)
    if p_sen.isOnline():
        mode = True
        In = p_sen.digitalRead('0')
        if In[11] == "0": status = 1
        else: status = 0
    context = {}
    context['mode'] = mode
    context['status'] = status_list[status]
    return render(request, 'test.html', context)

def book_form(request):
    a = Bform(request.POST)
    if a.is_valid():
        b = request.POST.copy()
        name = b.get("Name")
        num = b.get("Mobile_no")
        msg = "Hey"+name+"\nThanks for booking a parking wslot with us! \nHope u had pleasant expierience."
        URL = 'https://www.sms4india.com/api/v1/sendCampaign'
        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
                'apikey':apiKey,
                'secret':secretKey,
                'usetype':useType,
                'phone': phoneNo,
                'message':textMessage,
                'senderid':senderId
            }
            return requests.post(reqUrl, req_params)
        response = sendPostRequest(URL, 'F6CTY5C61BUR61G6U8ZVRKX6KX4K6OMD', '0B3KXL4OZ3KI4967', 'stage', num, 'SMSIND', msg )
        a.response = response
        a.save()
    return render(request, 'form.html', {'key': a})

def data(request):
    b = Contact.objects.all()
    return render(request, 'data.html', {'key': b})

def delete_data(request, id):
    b = Contact.objects.get(id=id)
    b.delete()
    return redirect('/data/')
