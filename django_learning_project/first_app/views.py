from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

course_dict = {
    "python": "PYTHON COURSE",
    "java" : "JAVA COURSE",
    "kotlin": "KOTLİN COURSE"
}


def index(request):
    return HttpResponse("this is first Django project and index")

def switch_num(request, num1):
    course_list = list(course_dict.keys())
    
    try:
        course = course_list[num1]
        page_to_go= reverse("course",args=[course])
        return HttpResponseRedirect(page_to_go)
    except:
        return HttpResponseNotFound("Not Found!!!!! TRY Again Later")


def course(request, item):
   # return HttpResponse(course_dict.get(item, "Not Found"))
    try:
        course = course_dict[item]
        return HttpResponse(course)
    except:
        return HttpResponseNotFound("Not Found!!!!! TRY Again Later")
        #raise Http404("Not Found!!!!! TRY Again Later")


def multiply_view(request, num1, num2):
    return HttpResponse(f"{num1} * {num2} = {num1 * num2}")

