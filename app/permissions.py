from rest_framework import permissions

"""
nome startapp + nome da ação + nome do model = genero.view_genero
"""


'''
Grupo de perfil de acesso

- MASTER (view, add, delete e change)

- VIEW (view - todas tabelas) -> PADRÃO
- ADD (add - todas tabelas)
- DELETE (delete - todas tabelas)
- CHANGE (change - todas tabelas)
'''


class PermissaoAcessoUtil(permissions.BasePermission):

    def has_permission(self, request, view):

        try:

            nome_app = view.queryset.model._meta.app_label
            nome_acao = {
                "GET": "view",
                "POST": "add",
                "PUT": "change",
                "PATCH": "change",
                "DELETE": "delete",
                "OPTIONS": "view",
                "HEAD": "view",
            }.get(request.method, "")
            nome_model = view.queryset.model._meta.model_name

            permicao = f"{nome_app}.{nome_acao}_{nome_model}"

            if request.user.has_perm(permicao):
                return True

            return False

        except AttributeError:
            return None
