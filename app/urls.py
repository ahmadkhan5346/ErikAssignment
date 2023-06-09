from django.urls import path
from app.views import FileUploadApiView, DataExportApiView
from app.views import DataApiView, RetrieveDataApiView


urlpatterns = [
    path("file-upload/", FileUploadApiView.as_view()),
    path("data-validation/", DataApiView.as_view()),
    path("retrieve-data/", RetrieveDataApiView.as_view()),
    path('data-export/', DataExportApiView.as_view()),
]
