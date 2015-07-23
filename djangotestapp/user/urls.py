from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from djangotestapp.user.views.login import LoginView
from djangotestapp.user.views.sign_up import SignUpView
from djangotestapp.user.views.account import AccountView
from djangotestapp.user.views.logout import LogoutView
from djangotestapp.user.views.profile import ProfileView
from djangotestapp.user.views.edit_profile import EditProfileView
from djangotestapp.user.views.user_search import UserSearchView
from djangoproject.decoratorts import is_logged_in


urlpatterns = [
    url(r'^$', is_logged_in(LoginView.as_view()), name='index'),
    url(r'^sign_up/$', is_logged_in(SignUpView.as_view()), name='sign_up'),
    url(r'^account/$', login_required(AccountView.as_view()), name='account'),
    url(r'^logout/$', login_required(LogoutView.as_view()), name='logout'),
    url(r'^profile/$', login_required(ProfileView.as_view()), name='profile'),
    url(r'^edit-profile/$', login_required(EditProfileView.as_view()), name='edit_profile'),
    url(r'^user-search/$', login_required(UserSearchView.as_view()), name='user_search'),
    ]