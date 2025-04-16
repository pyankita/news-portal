from django.urls import path
from newspaper import views

urlpatterns = [
    path("",views.HomeView.as_view(),name="home"),
    path("post-list/",views.PostListView.as_view(),name="post-list"),
    path("post-by-category/<int:category_id>/",views.PostByCategoriesView.as_view(),name="post-by-category"),
    path("tag-list",views.TagListView.as_view(),name="tag-list"),
    path("about-us/",views.AboutUsView.as_view(),name="about-us"),
    path("contact/",views.ContactDetailView.as_view(),name="contact")

]