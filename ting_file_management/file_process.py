from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    is_file_exists = False

    for obj in instance._data:
        if obj["nome_do_arquivo"] == path_file:
            is_file_exists = True
            break

    value_obj_to_return = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }

    if not is_file_exists:
        instance.enqueue(value_obj_to_return)
        print(value_obj_to_return)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
