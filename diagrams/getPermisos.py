from diagrams import Diagram, Cluster
from diagrams.onprem.client import User
from diagrams.aws.security import IdentityAndAccessManagementIamAddOn
from diagrams.custom import Custom
from diagrams.aws.analytics import CloudsearchSearchDocuments, Cloudsearch
from diagrams.oci.governance import Audit

rutaImgUser = "./img/user.png"
rutaImgPermissions = "./img/permissions.png"
rutaImgWorkspace = "../img/workspace.jpg"
rutaImgError= "../img/error.png"

with Diagram("Proceso General de Obtención de Permisos", show=True, graph_attr={"bgcolor": "White"}):

    user = User("Usuario")
    with Cluster("Método 1", graph_attr={"bgcolor": "transparent"}):
        workspace_id = Custom("ID de Workspace", rutaImgWorkspace)
        email = Custom("Email", "../img/email.png")

    with Cluster("Método 2", graph_attr={"bgcolor": "transparent"}):
        api_key = Custom("API Key", "../img/llaveOk.jpg")


    param_error = Custom("Error: Parámetro faltante o inválido", rutaImgError)
    api_key_error = Custom("Error: API Key inválida", rutaImgError)
    verifi = Custom("Verificacion", "../img/validacion.png")
    role_search = Cloudsearch("Buscar Roles y Permisos")
    merge_permissions = CloudsearchSearchDocuments("Fusionar Permisos")
    result = Audit("Permisos")


    user >> [workspace_id, email] >> verifi
    user >> api_key >> verifi
    verifi >> role_search  >> merge_permissions >> result
    verifi >> api_key_error
    verifi >> param_error