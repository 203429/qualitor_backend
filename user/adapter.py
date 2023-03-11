from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.id_role = data.get('id_role')
        user.id_project = data.get('id_project')
        user.is_superuser = data.get('is_superuser')
        user.save()
        return user