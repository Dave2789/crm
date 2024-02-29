import re
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .utils import download_emails, check_imap_connection, check_smtp_connection

class CustomPagination(PageNumberPagination):
    page_size = 10  # Define el tamaño de página predeterminado
    page_size_query_param = 'page_size'  # Parámetro para permitir que los usuarios especifiquen el tamaño de página

class EmailList(APIView):
    pagination_class = CustomPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name = 'page',
                in_ = openapi.IN_QUERY,
                required = True,
                type = openapi.TYPE_STRING,
                description = "página para filtrar"
            ),
            openapi.Parameter(
                name = 'page_size',
                in_ = openapi.IN_QUERY,
                required = True,
                type = openapi.TYPE_STRING,
                description = "Tamaño de página filtrar"
            )
        ]
    )

    def get(self, request):
        # Obtener el número de página y el tamaño de página de la solicitud
        page = int(request.query_params.get('page', 1))
        size = int(request.query_params.get('page_size', self.pagination_class.page_size))
        
        # Calcular los índices inicial y final de los correos electrónicos a descargar
        start_index = (page - 1) * size
        end_index = page * size
        
        # Descargar los correos electrónicos relevantes para la página actual
        emails = download_emails(username='cursos1@abrevius.com', password='D.Cursos1.2023', imap_server='mail.abrevius.com', start_index=start_index, end_index=end_index)
        paginated_emails = emails[start_index:end_index]  # Aplicar paginación
        
        # Realizar la paginación de los correos electrónicos
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(paginated_emails, request)
        
        return paginator.get_paginated_response(result_page)
    
'''class CheckImapConexion(APIView):
    # Ejemplo de uso
    imap_server = 'mail.abrevius.com'
    imap_port = 993
    smtp_server = 'mail.abrevius.com'
    smtp_port = 465
    username = 'cursos1@abrevius.com'
    password = 'D.Cursos1.2023'

    if check_imap_connection(username, password, imap_server, imap_port):
        print("Conexión IMAP exitosa")
    else:
        print("Error al conectar al servidor IMAP")

    if check_smtp_connection(username, password, smtp_server, smtp_port):
        print("Conexión SMTP exitosa")
    else:
        print("Error al conectar al servidor SMTP")'''
