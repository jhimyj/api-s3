import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Nombre del bucket y del nuevo "directorio"
    bucket_name  = event['body']['bucket']  # Cambia esto por tu bucket
    directory_name  = event['body']['directory']   # Cambia esto por tu nuevo "directorio"

    try:
        # Crear un nuevo "directorio" subiendo un objeto vacío con la clave del "directorio"
        s3.put_object(Bucket=bucket_name, Key=directory_name+"/")

        return {
            'statusCode': 200,
            'body': f'El directorio {directory_name} creado exitosamente en el bucket {bucket_name}'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error al crear el directorio: {str(e)}'
        }
