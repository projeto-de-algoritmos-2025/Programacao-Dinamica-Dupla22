import bisect
import heapq

def otimizar_agenda(jobs_data):
    """
    PROBLEMA 1: Weighted Interval Scheduling
    Objetivo: Maximizar lucro com apenas 1 recurso (você).
    Estratégia: Programação Dinâmica (O(n log n)).
    """
    # 1. Ordenar por horário de término
    jobs = sorted(jobs_data, key=lambda x: x['fim'])
    
    n = len(jobs)
    end_times = [j['fim'] for j in jobs]
    
    # (lucro_acumulado, lista_de_jobs)
    dp = [(0, [])] * n

    for i in range(n):
        current_job = jobs[i]
        profit_incl = current_job['valor']
        selection_incl = [current_job]

        # Busca Binária: Encontra o job compatível anterior
        idx = bisect.bisect_right(end_times, current_job['inicio'], 0, i) - 1
        
        if idx >= 0:
            prev_profit, prev_selection = dp[idx]
            profit_incl += prev_profit
            selection_incl = prev_selection + [current_job]
        
        profit_excl = 0
        selection_excl = []
        if i > 0:
            profit_excl, selection_excl = dp[i-1]

        # Decisão: Incluir atual ou manter o anterior
        if profit_incl > profit_excl:
            dp[i] = (profit_incl, selection_incl)
        else:
            dp[i] = (profit_excl, selection_excl)

    return {
        "lucro_total": dp[-1][0] if n > 0 else 0,
        "jobs_escolhidos": dp[-1][1] if n > 0 else []
    }

def calcular_equipe_minima(jobs_data):
    """
    PROBLEMA 2: Interval Partitioning
    Objetivo: Descobrir o nº mínimo de pessoas para aceitar TODOS os jobs.
    Estratégia: Algoritmo Guloso + Min-Heap (O(n log n)).
    """
    if not jobs_data:
        return {"tamanho_equipe": 0}

    # 1. Ordenar por horário de inicio
    jobs = sorted(jobs_data, key=lambda x: x['inicio'])
    
    # Heap armazena o horário de término de cada pessoa da equipe
    heap = [] 
    
    for job in jobs:
        # Se houver alguém livre antes desse job começar
        if heap and heap[0] <= job['inicio']:
            heapq.heappop(heap) # Remove o horário antigo dessa pessoa
            heapq.heappush(heap, job['fim']) # Atualiza com o novo horário de término
        else:
            # Ninguém livre, precisamos de uma nova pessoa na equipe
            heapq.heappush(heap, job['fim'])

    # O tamanho do heap no final é o número de pessoas necessárias
    return {
        "tamanho_equipe": len(heap)
    }