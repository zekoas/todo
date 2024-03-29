from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (
    TaskList,
    TaskDetail,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    CustomLoginViews,
    RegisterPage,
    TaskReorder,
)

urlpatterns = [
    path("register/", RegisterPage.as_view(), name="register"),
    path("login/", CustomLoginViews.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("task/<int:pk>", TaskDetail.as_view(), name="task"),
    path("", TaskList.as_view(), name="tasks"),
    path("create/", TaskCreate.as_view(), name="create"),
    path("update/<int:pk>", TaskUpdate.as_view(), name="update"),
    path("delete/<int:pk>", TaskDelete.as_view(), name="delete"),
    path("task-reorder/", TaskReorder.as_view(), name="task-reorder"),
]
