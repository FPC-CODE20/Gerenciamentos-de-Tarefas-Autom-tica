class Tarefa:
    def __init__(self, nome, duracao, prioridade, prazo, recursos_necessarios, categoria):
        self.nome = nome
        self.duracao = duracao  # em horas
        self.prioridade = prioridade  # 1-5 (5 é mais importante)
        self.prazo = prazo  # data limite
        self.recursos = recursos_necessarios  # lista de recursos necessários
        self.categoria = categoria  # trabalho, pessoal, saúde, etc.
        self.concluida = False
        def agendar_tarefas(tarefas, horas_disponiveis, recursos_disponiveis):
    # Filtra tarefas possíveis com recursos disponíveis
    tarefas_possiveis = [t for t in tarefas if all(recurso in recursos_disponiveis for recurso in t.recursos)]
    
    # Ordena por: 1) proximidade do prazo, 2) prioridade, 3) duração
    tarefas_ordenadas = sorted(tarefas_possiveis, 
                              key=lambda x: (x.prazo, -x.prioridade, x.duracao))
    
    agenda = []
    horas_alocadas = 0
    
    for tarefa in tarefas_ordenadas:
        if horas_alocadas + tarefa.duracao <= horas_disponiveis and not tarefa.concluida:
            agenda.append(tarefa)
            horas_alocadas += tarefa.duracao
    
    return agenda
    def otimizar_agenda(agenda):
    # Implementa algoritmo de otimização (ex: empacotamento de binário)
    # Pode considerar:
    # - Agrupar tarefas por categoria
    # - Alternar entre tipos de tarefas para variedade
    # - Considerar energia do usuário ao longo do dia
    return agenda_otimizada

    class ModeloPreferencias:
    def __init__(self):
        # Carrega modelo treinado nas preferências históricas do usuário
        self.modelo = self.carregar_modelo()
    
    def prever_melhor_horario(self, tarefa):
        # Prediz o melhor horário para a tarefa baseado em padrões históricos
        return self.modelo.predict(tarefa)
        def exibir_agenda(agenda):
    print("📅 Agenda Automática 📅")
    print("-----------------------")
    for i, tarefa in enumerate(agenda, 1):
        print(f"{i}. {tarefa.nome} ({tarefa.duracao}h) - Prioridade: {tarefa.prioridade} - Prazo: {tarefa.prazo}")
        
