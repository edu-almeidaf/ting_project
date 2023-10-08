from ting_file_management.file_management import txt_importer
import sys


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
        sys.stdout.write(str(value_obj_to_return))


def remove(instance):
    if instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")

    obj_to_be_removed = instance.dequeue()
    file_path = obj_to_be_removed["nome_do_arquivo"]

    sys.stdout.write(f"Arquivo {file_path} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write("Posição inválida")
