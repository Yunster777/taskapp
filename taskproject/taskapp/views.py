from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.core.paginator import Paginator

from .models import Task, ChecklistItem


def index(request):
    context = {}
    return render(request, "pages/index.html", context)


class TaskListView(TemplateView):
    template_name = "pages/task_list.html"

    def get_context_data(self, **kwargs):
        tasks = Task.objects.filter(due__gte=timezone.now()).order_by("-due")
        paginator = Paginator(tasks, 4)
        page_number = self.request.GET.get("page", "1")
        paging = paginator.get_page(page_number)

        return {
            # "tasks": tasks,
            "paging": paging,
        }


class TaskCreateView(CreateView):
    model = Task
    fields = ["title", "type", "due"]
    template_name = "pages/task_create.html"
    success_url = "/"


class TaskPreviousView(ListView):
    model = Task
    template_name = "pages/task_previous_list.html"
    queryset = Task.objects.filter(due__lt=timezone.now()).order_by("-due")
    paginate_by = 4


class TaskDetailView(DetailView):
    model = Task
    template_name = "pages/task_detail_view.html"
    pk_url_kwarg = "task_id"  # primary key

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["checklists"] = ChecklistItem.objects.filter(task=self.object).all()
        return context
