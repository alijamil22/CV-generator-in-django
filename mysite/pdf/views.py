from django.shortcuts import render
from .models import Profile
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
    return render(request,"pdf/resume.html",{"user_profile":user_profile})