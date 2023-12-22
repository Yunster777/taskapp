from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "taskapp"
urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path("previous/", views.TaskPreviousView.as_view(), name="previous"),
    path("task/", views.TaskCreateView.as_view(), name="create-task"),
    path("task/<int:task_id>/", views.TaskDetailView.as_view(), name="view-task"),
    path("task/<int:task_id>/delete/", views.index, name="delete-task"),
    path("task/<int:task_id>/item/", views.index, name="create-item"),
    path("task/<int:task_id>/item/<int:check_id>/", views.index, name="check-item"),
    path(
        "task/<int:task_id>/item/<int:check_id>/delete/",
        views.index,
        name="delete-item",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
