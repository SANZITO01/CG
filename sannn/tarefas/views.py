from django.shortcuts import render
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm
def lista_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('-id')
    form = TarefaForm()
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas, 'form': form})
def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('lista_tarefas')