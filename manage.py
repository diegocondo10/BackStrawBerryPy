#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BackStrawBerryPy.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # try:
    #     client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
    #     client._request_signer.sign = (lambda *args, **kwargs: None)
    #     # s3 = boto3.resource(service_name='s3')
    #
    #     print("conexion exitosa")
    # except Exception as e:
    #     print(e)
    #     print("No se pudo realizar, revisa el codigo de conexion :v")

    main()
