from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(1000)

    priority_queue.enqueue({"qtd_linhas": 4})
    assert len(priority_queue.high_priority) == 1

    priority_queue.enqueue({"qtd_linhas": 12})
    assert len(priority_queue.regular_priority) == 1

    priority_queue.enqueue({"qtd_linhas": 1})
    assert len(priority_queue.high_priority) == 2

    assert len(priority_queue) == 3

    assert priority_queue.search(0) == {"qtd_linhas": 4}
    assert priority_queue.search(1) == {"qtd_linhas": 1}
    assert priority_queue.search(2) == {"qtd_linhas": 12}

    priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 1
    assert len(priority_queue.regular_priority) == 1
    assert len(priority_queue) == 2

    priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 1
    assert len(priority_queue) == 1

    priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 0
    assert len(priority_queue) == 0
