import bisect

def otimizar_agenda(jobs_data):
    """
    Recebe uma lista de dicionários: [{'nome': 'A', 'inicio': 0, 'fim': 10, 'valor': 100}, ...]
    Retorna o lucro máximo e a lista de jobs escolhidos.
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

        # Busca Binária para achar o job compatível anterior
        # bisect_right retorna o ponto de inserção para manter a ordem
        idx = bisect.bisect_right(end_times, current_job['inicio'], 0, i) - 1
        
        if idx >= 0:
            prev_profit, prev_selection = dp[idx]
            profit_incl += prev_profit
            selection_incl = prev_selection + [current_job]
        
        profit_excl = 0
        selection_excl = []
        if i > 0:
            profit_excl, selection_excl = dp[i-1]

        # Decisão
        if profit_incl > profit_excl:
            dp[i] = (profit_incl, selection_incl)
        else:
            dp[i] = (profit_excl, selection_excl)

    return {
        "lucro_total": dp[-1][0] if n > 0 else 0,
        "jobs_escolhidos": dp[-1][1] if n > 0 else []
    }
