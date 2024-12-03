from django.urls import path
from . import views


# version 5
# playing with html
urlpatterns = [
    path("", views.index), #/challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]

# version 4
# breakdown using reverse
# urlpatterns = [
#     path("<int:month>", views.monthly_challenge_by_number),
#     path("<str:month>", views.monthly_challenge, name="month-challenge")
# ]

# version 3
# breakdown path using function in view and add data_type
# urlpatterns = [
#     path("<int:month>", views.monthly_challenge_by_number),
#     path("<str:month>", views.monthly_challenge)
# ]

# version 2
# breakdown path using function in views
# urlpatterns = [
#     path("<month>", views.monthly_challenge)
# ]

# version 1
# breakdown path by views
# urlpatterns = [
#     path("january", views.january),
#     path("february", views.february),
#     path("march", views.march),
#     path("april", views.april),
#     path("may", views.may),
#     path("june", views.june),
#     path("july", views.july),
#     path("august", views.august),
#     path("september", views.september),
#     path("october", views.october),
#     path("november", views.november),
#     path("december", views.december)
# ]

