from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        print(f'-----------------{user}-------------------------')
        user.save()
        list_projects=data.get('id_project')
        if list_projects !=None and len(list_projects) >0:
            for project in list_projects:
                user.id_project.add(project)
        list_roles=data.get('id_role')
        if list_roles != None and len(list_roles) >0 :
            for rol in list_roles:
                user.id_role.add(rol) 
        return user