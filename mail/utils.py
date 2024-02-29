import re
import imaplib
import smtplib
import email
from email.header import decode_header

def download_emails(username, password, imap_server, start_index, end_index):
    try:
        # Conexión al servidor IMAP
        imap_port = 993
        imap = imaplib.IMAP4_SSL(imap_server, imap_port)
        #imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(username, password)

        # Seleccionar la bandeja de entrada (inbox)
        imap.select('inbox')

        # Buscar correos electrónicos
        status, messages = imap.search(None, 'ALL')
        message_ids = messages[0].split()

        # Lista para almacenar los correos electrónicos
        emails = []

        # Iterar sobre los correos electrónicos
        for message_id in message_ids[start_index:end_index]:
            status, msg_data = imap.fetch(message_id, '(RFC822)')
            raw_email = msg_data[0][1]
            email_message = email.message_from_bytes(raw_email)

            # Procesar el correo electrónico
            #subject = decode_header(email_message['Subject'])[0][0]
            body = ""

            # Procesar el correo electrónico
            subject_bytes = email_message['Subject']
            if isinstance(subject_bytes, bytes):
                subject = decode_header(subject_bytes)[0][0]
                subject = subject.decode('utf-8', errors='ignore') if isinstance(subject, bytes) else subject
            else:
                subject = subject_bytes

            # Manejo del contenido del correo electrónico
            if email_message.is_multipart():
                # Si el correo electrónico es multipart (tiene partes múltiples, como texto y archivos adjuntos)
                for part in email_message.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))

                    if "attachment" not in content_disposition:
                        # Si no es un archivo adjunto, extraemos el contenido del cuerpo del correo electrónico
                        payload = part.get_payload(decode=True)
                        if payload is not None:
                            body += payload.decode('utf-8', errors='ignore')

            else:
                # Si el correo electrónico es de texto plano
                payload = email_message.get_payload(decode=True)
                if payload is not None:
                    body = payload.decode('utf-8', errors='ignore')
                    
            texto_plano = remove_html_tags(body)
            emails.append({'subject': subject, 'body': texto_plano})

        # Cerrar conexión
        imap.close()
        imap.logout()

        return emails
    except Exception as e:
        print("Error al descargar correos electrónicos:", e)
        return []
    
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def check_imap_connection(username, password, imap_server, imap_port):
    try:
        # Intenta conectarte al servidor IMAP
        imap = imaplib.IMAP4_SSL(imap_server, imap_port)
        imap.login(username, password)
        imap.logout()
        return True  # La conexión fue exitosa
    except Exception as e:
        print("Error al conectar al servidor IMAP:", e)
        return False  # La conexión falló

def check_smtp_connection(username, password, smtp_server, smtp_port):
    try:
        # Intenta conectarte al servidor SMTP
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()  # Si el servidor SMTP requiere TLS/SSL
        smtp.login(username, password)
        smtp.quit()
        return True  # La conexión fue exitosa
    except Exception as e:
        print("Error al conectar al servidor SMTP:", e)
        return False  # La conexión falló

