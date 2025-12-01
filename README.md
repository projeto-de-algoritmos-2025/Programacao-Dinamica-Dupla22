# Smart Agenda — Otimizador de Freelance

Projeto didático que implementa um otimizador de agenda (problema de interval scheduling com pesos)
usando programação dinâmica. A aplicação possui uma interface web simples (`Flask`) para adicionar
jobs (tarefas com início, fim e valor) e calcular a combinação que maximiza o lucro total sem
sobreposição de horários.

## Alunos

<div align = "center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/DanielFsR"><img style="border-radius: 50%;" src="https://github.com/DanielFsR.png" width="190;" alt=""/><br /><sub><b>Daniel Ferreira</b></sub></a><br /><a href="Link git" title="Rocketseat"></a></td>
    <td align="center"><a href="https://github.com/Diogo-Barboza"><img style="border-radius: 50%;" src="https://github.com/Diogo-Barboza.png" width="190px;" alt=""/><br /><sub><b>Diogo Barboza </b></sub></a><br />
  </tr>
</table>

| Matrícula   | Aluno                             |
| ----------- | ----------------------------------|
| 22/2006632  | Daniel Ferreira                   |
| 22/2006660  | Diogo Rodrigues Barboza           |
</div>


## Descrição

**Resumo rápido**: execute a aplicação com `python app.py`, abra `http://127.0.0.1:5000/` e
adicione jobs pela interface para obter a melhor agenda do dia.

Este repositório implementa um otimizador de agenda que recebe uma lista de jobs (cada job
tem `nome`, `inicio`, `fim` e `valor`) e retorna a melhor seleção de jobs que não se sobrepõem
e que maximiza o lucro total. A lógica está em `logic.py` (algoritmo de programação dinâmica
com busca binária para compatibilidade entre intervalos). A interface web em `templates/index.html`
permite inserir jobs manualmente e visualizar a linha do tempo do dia.

## Requisitos

- Python 3.8+
- Dependências listadas em `requirements.txt` (Flask e bibliotecas relacionadas)

## Instalação (local / desenvolvimento)

1. (Recomendado) crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie a aplicação:

```bash
python app.py
```

A aplicação roda por padrão em `http://127.0.0.1:5000/` com `debug=True` (modo de desenvolvimento).

## Screenshots

![](fotos/image.png)
![](fotos/show.png)

## Uso — Interface web

1. Abra `http://127.0.0.1:5000/` no navegador.
2. Preencha `Nome do Job`, `Início`, `Fim` e `Valor` e clique em `Adicionar à Lista`.
3. Depois de adicionar os jobs desejados, clique em `CALCULAR MELHOR AGENDA`.
4. O resultado mostrará o `Lucro Máximo` e colorirá a timeline: verde para jobs escolhidos e
	 cinza para os rejeitados.

## Estrutura do projeto

- `app.py` — App Flask e rotas (`/` e `/calcular`).
- `logic.py` — Implementação do algoritmo de otimização (programação dinâmica + bisect).
- `requirements.txt` — Dependências do projeto.
- `templates/index.html` — Interface web (HTML + JS) para adicionar jobs e visualizar a timeline.
- `.venv/` — (opcional) ambiente virtual local (pasta gitignored normalmente).

## Detalhes da implementação (breve)

- `logic.py` ordena os jobs por `fim`. Para cada job `i` calcula o melhor lucro incluindo-o
	(somando o lucro de um job compatível anterior, obtido por busca binária em `end_times`) e
	comparando com a opção de não incluí-lo. Retorna o lucro máximo e a lista dos jobs escolhidos.

## Como contribuir

- Abrir issues para bugs ou sugestões.
- Enviar pull requests com pequenas mudanças; mantenha o estilo do código.
- Sugestões de melhoria: testes unitários para `logic.py`, validações mais robustas no backend,
	e suporte a vários dias/recorrências.

## Execução de testes manuais rápidos

1. Levante a aplicação (`python app.py`).
2. Abra a interface e teste casos simples, por exemplo:
	 - Job A: 0–10, valor 100
	 - Job B: 5–15, valor 120
	 - Job C: 10–20, valor 200
	O algoritmo deve escolher A ou B+C dependendo dos valores — verifique o `Lucro Máximo`.

## Apresentação 

<div align="center">
<a href="https://youtu.be/pX8PYBPTqgk"><img src="https://i0.wp.com/noic.com.br/wp-content/uploads/2015/04/fib.png?resize=688%2C409" width="50%"></a>
</div>

[![Assista no YouTube](https://img.shields.io/badge/YouTube-Video-red?logo=youtube)](https://youtu.be/pX8PYBPTqgk)

<font size="3"><p style="text-align: center">Autor: [Diogo Barboza](https://github.com/) e [Daniel Ferreira](https://github.com/).</p></font>