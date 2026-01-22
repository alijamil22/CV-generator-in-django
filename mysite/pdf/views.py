from django.shortcuts import render
from .models import Profile
import pdfkit
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        degree = request.POST.get("degree")
        school = request.POST.get("school")
        university = request.POST.get("university")
        summary = request.POST.get("summary")
        skills = request.POST.get("skills")
        previous_work = request.POST.get("previous_work")
        profile = Profile(name=name,email=email,phone=phone,degree=degree,school=school,university=university,summary=summary,skills=skills,previous_work=previous_work)
        profile.save()
    return render(request,'pdf/accept.html')
def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({"user_profile":user_profile})
    options={
        'page-size':'letter',
        'encoding':'utf-8'
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment;filename = "resume.pdf"'
    
    return response