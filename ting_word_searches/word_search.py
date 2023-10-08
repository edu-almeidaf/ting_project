def verify_content(necessary_content, line, i):
    if necessary_content:
        return {
            "linha": i + 1,
            "conteudo": line
        }
    return {
        "linha": i + 1
    }


def get_ocurrences(word, instance, necessary_content):
    ocurrences = []
    for obj_to_verify in instance._data:
        search_ocurrences = []
        for i, line_content in enumerate(obj_to_verify["linhas_do_arquivo"]):
            if word.lower() in line_content.lower():
                search_ocurrences.append(
                    verify_content(necessary_content, line_content, i)
                )

        if len(search_ocurrences) > 0:
            data = {
                "palavra": word,
                "arquivo": obj_to_verify["nome_do_arquivo"],
                "ocorrencias": search_ocurrences
            }
            ocurrences.append(data)

    return ocurrences


def exists_word(word, instance):
    ocurrences = get_ocurrences(word, instance, False)
    return ocurrences


def search_by_word(word, instance):
    ocurrences = get_ocurrences(word, instance, True)
    return ocurrences
