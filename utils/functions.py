import io
from datetime import date

from docxtpl import DocxTemplate

NUMEROS_ORDINARIOS = {
    '1': 'PRIMERO',
    '2': 'SEGUNDO',
    '3': 'TERCERO',
    '4': 'CUARTO',
    '5': 'QUINTO',
    '6': 'SEXTO',
    '7': 'SÉPTIMO',
    '8': 'OCTAVO',
    '9': 'NOVENO',
    '10': 'DÉCIMO',
}


def concat_if_exist(*args, delimiter=' '):
    return delimiter.join([arg for arg in args if arg is not None and arg != ''])


def create_docx(file, context) -> DocxTemplate:
    tpl = DocxTemplate(file)
    tpl.render(context)
    return tpl


def create_docx_bytes(file, context) -> io.BytesIO:
    docx = create_docx(file, context)
    file_stream = io.BytesIO()
    docx.save(file_stream)
    file_stream.seek(0)
    return file_stream


def docx_to_bytes(tpl):
    file_stream = io.BytesIO()
    tpl.save(file_stream)
    file_stream.seek(0)
    return file_stream


def get_edad(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def get_ordinal_num(numero):
    return NUMEROS_ORDINARIOS.get(f'{numero}')
