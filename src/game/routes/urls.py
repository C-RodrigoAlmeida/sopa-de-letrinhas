from django.urls import path, include

urlpatterns = [
    path("joint/", include("src.game.routes.joint_urls")),
    path("word/", include("src.game.routes.word_urls")),
]