from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
def contact(request):
    print("Tipo de peticion: {}".format(request.method))
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name",'')
            email = request.POST.get("email",'')
            content = request.POST.get("content",'')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La caffetiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["duvandbz@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
            except:
                return redirect(reverse('contact')+'?fail')    
            return redirect(reverse('contact')+'?ok')# reverse nos devuelve la ruta a partir del name en el path() del archivo urls.py, esto para no escribir el texto crudo
    else:
        contact_form = ContactForm()
    return render(request,'contact/contact.html',{'form':contact_form})