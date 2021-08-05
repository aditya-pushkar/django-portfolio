# EXTERNAL IMPORT
from django.shortcuts import render
from django.views.generic import ListView
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# INTERNAL IMPORT
from .models import Portfolio, TeckStack
from django.conf import settings


class Home(ListView):
    context_object_name = 'item'    
    template_name = 'home.html'
    queryset = Portfolio.objects.all()[:4]

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['tech'] = TeckStack.objects.all()
        return context
    

def aboutPage(request, template_name='about.html'):
    pass
    return render(request, template_name)


def projectsPage(request):
    projects = Portfolio.objects.all()
    context = {
        "projects":projects
    }
    return render(request, 'projects.html', context)


def sendEmail(request):

    if request.method == 'POST':

        template = render_to_string('email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['pushkaraditya916@gmail.com']
        )
        email.Fail_silently=False
        email.send()
    return render(request, 'email_sent.html')