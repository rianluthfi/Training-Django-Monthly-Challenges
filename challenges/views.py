from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


# version 7
# adding html from templates
monthly_challenges = {
    "january" : "This is january",
    "february" : "This is february",
    "march" : "This is march",
    "april" : "This is april",
    "may" : "This is may",
    "june" : "This is june",
    "july" : "This is july",
    "august" : "This is august",
    "september" : "This is september",
    "october" : "This is october",
    "november" : "This is november",
    "december" : None
}

# index using render with parameter
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months" : months
    })

# def index(request):
#     list_items = ""
#     months = list(monthly_challenges.keys())

#     for month in months:
#         capitalized_month = month.capitalize()
#         month_path = reverse("month-challenge", args=[month])
#         list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

#     response_data = f"<ul>{list_items}</ul>"

#     # response_data = """
#     #     <ul>
#     #         <li><a href="/challenges/january">january</a></li>
#     #     </ul>
#     # """

#     return HttpResponse(response_data)


# using redirect
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month_name" : month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # implement page 404 using class Http404 > will find 404.html
        raise Http404()

        # implement page 404
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)

        # standard
        # return HttpResponseNotFound("<h1>This month is not supported!</h1>")

# version 6
# adding html
# monthly_challenges = {
#     "january" : "This is january",
#     "february" : "This is february",
#     "march" : "This is march",
#     "april" : "This is april",
#     "may" : "This is may",
#     "june" : "This is june",
#     "july" : "This is july",
#     "august" : "This is august",
#     "september" : "This is september",
#     "october" : "This is october",
#     "november" : "This is november",
#     "december" : "This is december"
# }

# def index(request):
#     list_items = ""
#     months = list(monthly_challenges.keys())

#     for month in months:
#         capitalized_month = month.capitalize()
#         month_path = reverse("month-challenge", args=[month])
#         list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

#     response_data = f"<ul>{list_items}</ul>"

    # response_data = """
    #     <ul>
    #         <li><a href="/challenges/january">january</a></li>
    #     </ul>
    # """

    return HttpResponse(response_data)


# using redirect
# def monthly_challenge_by_number(request, month):
#     months = list(monthly_challenges.keys())

#     if month > len(months):
#         return HttpResponseNotFound("Invalid Month")

#     redirect_month = months[month - 1]
#     redirect_path = reverse("month-challenge", args=[redirect_month]) #challenge/january
#     return HttpResponseRedirect(redirect_path)

# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenges[month]
#         response_data = f"<h1>{challenge_text}</h1>"
#         return HttpResponse(response_data)
#     except:
#         return HttpResponseNotFound("<h1>This month is not supported!</h1>")

# version 5
# using reverse
# monthly_challenges = {
#     "january" : "This is january",
#     "february" : "This is february",
#     "march" : "This is march",
# }

# using redirect
# def monthly_challenge_by_number(request, month):
#     months = list(monthly_challenges.keys())

#     if month > len(months):
#         return HttpResponseNotFound("Invalid Month")

#     redirect_month = months[month - 1]
#     redirect_path = reverse("month-challenge", args=[redirect_month]) #challenge/january
#     return HttpResponseRedirect(redirect_path)

# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenges[month]
#         return HttpResponse(challenge_text)
#     except:
#         return HttpResponseNotFound("This month is not supported!")
    
# version 4
# using dictionary
# monthly_challenges = {
#     "january" : "This is january",
#     "february" : "This is february",
#     "march" : "This is march",
# }

# # using redirect
# def monthly_challenge_by_number(request, month):
#     months = list(monthly_challenges.keys())

#     if month > len(months):
#         return HttpResponseNotFound("Invalid Month")

#     redirect_month = months[month - 1]
#     return HttpResponseRedirect("/challenges/" + redirect_month)

# def monthly_challenge(request, month):
#     try:
#         challenge_text = monthly_challenges[month]
#         return HttpResponse(challenge_text)
#     except:
#         return HttpResponseNotFound("This month is not supported!")
    

# version 3
# def monthly_challenge_by_number(request, month):
#     return HttpResponse(month)

# version 2
# def monthly_challenge(request, month):
#     challenge_text = None

#     if month == "january":
#         challenge_text = "This January"
#     elif month == "february":
#         challenge_text = "This February"
#     elif month == "march":
#         challenge_text == "This March"
#     else:
#         return HttpResponseNotFound("This month is not supported!")
#     return HttpResponse(challenge_text)

# version 1

# def january(request):
#     return HttpResponse("This January")

# def february(request):
#     return HttpResponse("This February")

# def march(request):
#     return HttpResponse("This march")

# def april(request):
#     return HttpResponse("This april")

# def may(request):
#     return HttpResponse("This may")

# def june(request):
#     return HttpResponse("This june")

# def july(request):
#     return HttpResponse("This july")

# def august(request):
#     return HttpResponse("This august")

# def september(request):
#     return HttpResponse("This september")

# def october(request):
#     return HttpResponse("This october")

# def november(request):
#     return HttpResponse("This november")

# def december(request):
#     return HttpResponse("This december")