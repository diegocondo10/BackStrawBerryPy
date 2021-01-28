def concat_if_exist(*args, delimiter=' '):
    return delimiter.join([arg for arg in args if arg is not None and arg != ''])
    # return ''.join([''])
