import io
from datetime import date

from docxtpl import DocxTemplate


def concat_if_exist(*args, delimiter=' '):
    return delimiter.join([arg for arg in args if arg is not None and arg != ''])
    # return ''.join([''])


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
