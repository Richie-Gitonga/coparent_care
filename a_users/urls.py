from django.urls import path
from a_users.views import (
    profile_view,
    profile_edit_view,
    childinfo_edit_view,
    education_edit_view,
    profile_settings_view,
    profile_emailchange,
    profile_emailverify,
    profile_delete_view
)

urlpatterns = [
    path('', profile_view, name="profile"),
    path('edit/', profile_edit_view, name="profile-edit"),
    path('onboarding/', profile_edit_view, name="profile-onboarding"),
    path('childinfo/edit/', childinfo_edit_view, name='edit_childinfo'),
    path('education/edit/<int:id>/', education_edit_view, name='edit_education'),
    path('settings/', profile_settings_view, name="profile-settings"),
    path('emailchange/', profile_emailchange, name="profile-emailchange"),
    path('emailverify/', profile_emailverify, name="profile-emailverify"),
    path('delete/', profile_delete_view, name="profile-delete"),
]