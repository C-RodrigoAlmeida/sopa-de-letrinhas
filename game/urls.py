from django.urls import path
from game.views import WordCreateView, WordUpdateView, WordListView, WordDeleteView, WordDetailsView, JointCreateView, JointUpdateView, JointListView, JointDetailsView, JointDeleteView

app_name = "game"

urlpatterns = [
    path("words/", WordListView.as_view(), name="word_list"),
    path("words/registration/", WordCreateView.as_view(), name="word_registration"),
    path("words/<int:pk>/details/", WordDetailsView.as_view(), name="word_details"),
    path("words/<int:pk>/update/", WordUpdateView.as_view(), name="word_update"),
    path("words/<int:pk>/delete/", WordDeleteView.as_view(), name="word_delete"),

    path("joint/", JointListView.as_view(), name="joint_list"),
    path("joint/<int:pk>/update/", JointUpdateView.as_view(), name="joint_update"),
    path("joint/registration/", JointCreateView.as_view(), name="joint_registration"),
    path("joint/<int:pk>/details/", JointDetailsView.as_view(), name="joint_details"),
    path("joint/<int:pk>/delete/", JointDeleteView.as_view(), name="joint_delete"),
]