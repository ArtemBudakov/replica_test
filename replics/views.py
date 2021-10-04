from django.http import HttpResponse
from russian_names import RussianNames

from .models import Worker


def create_workers(request):
    fio = RussianNames(count=10).get_batch()
    response = 'Поприветствуйте новых сотрудников:'
    for _ in range(10):
        worker = Worker(fio=fio[_])
        worker.save()
        response += f' {worker}'

    return HttpResponse(response)


def database_main(request):
    workers = Worker.objects.all()
    response = 'Workers info from main database:'
    for worker in workers:
        response += f' {worker}'
    return HttpResponse(response)


def database_replica(request):
    workers = Worker.objects.using('replica_1').all()
    response = 'Workers info from replica database:'
    for worker in workers:
        response += f' {worker}'
    return HttpResponse(response)
