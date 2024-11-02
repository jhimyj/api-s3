import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Configura el nombre del bucket y el directorio
    bucket_name = event['body']['bucket']  # Cambia esto por tu bucket
    directory_name = event['body']['directory']   # Cambia esto por tu "directorio"
    file_name =  event['body']['name']    # Cambia esto por el nombre del archivo que deseas subir
    base64_content = event['body']['base_64']    # Coloca aquí tu string en base64 del archivo

    try:
        # Decodificar el contenido de base64
        file_content = base64.b64decode(base64_content)

        # Subir el archivo decodificado al "directorio"
        s3.put_object(Bucket=bucket_name, Key=directory_name +"/"+ file_name, Body=file_content)

        return {
            'statusCode': 200,
            'body': f'Archivo {file_name} subido exitosamente en {directory_name} del bucket {bucket_name}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error al subir el archivo: {str(e)}'
        }
