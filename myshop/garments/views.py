from django.shortcuts import render,redirect

# from garments.models import formalshirts
from garments.form import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse



def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def formalshirts(request):
    lst = FormalShirt.objects.all()
    return render(request,'formalshirts.html',{'lst':lst})

lst = []
price = []
def cart(request,num):
    item = FormalShirt.objects.get(id=num)
    lst.append(item)
    price.append(item.price)
    return render(request,'cart.html',{'lst':lst,'t_price':sum(price)})

def contactus(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        subject = 'Hello from my garments shope.com'
        name = request.POST.get('contact_name')
        message = 'This is your message:'+request.POST.get('contact_message')
        from_email = settings.EMAIL_HOST_USER
        user_eamil=request.POST.get('contact_emial')
        to_list=[user_eamil,settings.EMAIL_HOST_USER]
        send_mail(subject,name+message,from_email,to_list,fail_silently=False)
        return HttpResponseRedirect('thankyou')
        return render(request,'contactus.html',{'form':form})

def thankyou(request):
    response=HttpResponse()
    response.write('<h2>Thanks For Contacting Garments</h2>')
    response.write('<h3>WE just send you a mail</h3>')
    return response