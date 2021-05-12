from django.conf.urls import url
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^professors$', views.ProfessorViewForGetAndPost),
    url(r'^professors/([0-9]+)$', views.ProfessorViewForPutAndDelete),
    url(r'^students$', views.StudentViewForGetAndPost),
    url(r'^students/([0-9]+)$', views.StudentViewForPutAndDelete),
    url(r'^classes$', views.ClassViewForGetAndPost),
    url(r'^classes/([0-9]+)$', views.ClassViewForPutAndDelete),
    url(r'^subjects$', views.SubjectViewForGetAndPost),
    url(r'^subjects/([0-9]+)$', views.SubjectViewForPutAndDelete),
    url(r'^notes$', views.NoteViewForGetAndPost),
    url(r'^notes/([0-9]+)$', views.NoteViewForPutAndDelete)
]