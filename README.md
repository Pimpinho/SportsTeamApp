# SportsTeamApp

 
Aplicação SportsTeamApp, desenvolvida em Django, para o gerenciamento esportivo de times, jogadores, torneios e eventos para a matéria de Projeto de Software.

Padrões de Projeto Utilizados:
Padrão Memento na Classe Player e Proxy, para os itens de inventário.

# Memento
O padrão de projeto Memento foi implementado na classe Player localizada no arquivo models.py. Esse padrão é usado para salvar e restaurar o estado de um objeto, permitindo desfazer mudanças sem expor os detalhes de sua implementação.
Objetivo

Permitir que o estado de um jogador (como estatísticas ou status) seja salvo e restaurado em momentos específicos. 

Classe Originator: A classe Player atua como a classe principal (Originator), cujo estado pode ser salvo ou restaurado.
Classe Memento: Um dicionário ou estrutura serializável que armazena o estado do objeto.
Caretaker: Responsável por gerenciar os mementos.

# Proxy
O padrão Proxy foi implementado no arquivo proxies.py para gerenciar o acesso à funcionalidade de inventário. Este padrão adiciona uma camada intermediária entre o cliente e o objeto real, controlando e otimizando o acesso.

Classe Proxy: Cria uma representação especializada do modelo existente.
Classe Original: Modelo base que é estendido pela Proxy.

No arquivo proxies.py, a classe Proxy especializa o modelo Inventory.
