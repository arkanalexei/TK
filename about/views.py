from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from about.forms import FeedbackForm
from about.models import Feedback
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
import json 

@csrf_exempt
def get_data(request):
    all_feedback_groups = Feedback.objects.all()

    all_feedback_list = []
    for group in all_feedback_groups:
        group_dict = {
                "id" : int(group.pk),
                "name": group.name,
                "message":group.message,
                "star":group.star,
        }
        all_feedback_list.append(group_dict)
    
    # Serialize query set to json
    data = json.dumps(all_feedback_list)

    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def about_us(request):
    feedbacks = Feedback.objects.all().order_by("-created_at")[:4]
    feedbacksAll = Feedback.objects.filter(user_id = request.user.id)
    context = {'feedbacks':feedbacks,'feedbacksAll':feedbacksAll}

    # create object of form
    form = FeedbackForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        data = form.save(commit=False) #bisa return object
        try :
            data.user_id = User.objects.get(id=request.user.id)
        except:
            return HttpResponseRedirect("/about/")

        data.save()
        if request.method == 'POST':
          return HttpResponseRedirect("/about/")
  
    context['form']= form
    return render(request, "about.html", context)

def edit_feedback(request):
  print(request)
  if (request.method == "POST"):
    id = request.POST.get("id")
    message = request.POST.get("message")
    star = request.POST.get("star")
      
    feedback = Feedback.objects.get(id=id)
    feedback.message = message
    feedback.star = star
    feedback.save()

  return HttpResponseRedirect("/about/")

def delete_feedback(request):
    if (request.method == "POST"):
        id = request.POST.get("id")
        Feedback.objects.filter(id=id).delete()
    return HttpResponseRedirect("/about/")

def show_xml(request):
    data = Feedback.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Feedback.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Feedback.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Feedback.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
