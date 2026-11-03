# 🛡️ dio-agent-appsec

Especialização do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) em
**cibersegurança (AppSec)**. Este repositório contém **apenas o que foi acrescentado** ao
agente base. Nenhum modelo foi treinado: o agente aprende pelo que está escrito nos arquivos.

## Especialização e por quê
Em vez de responder direto, o agente entende o contexto, avalia impacto, probabilidade e
severidade e orienta a correção, como um profissional de segurança. Em segurança, o mesmo
problema muda de gravidade conforme o ambiente; por isso perguntar antes de agir é o ponto central.

## O que há neste repositório
| Arquivo | O que é |
|---|---|
| `skills/vulnerability-analysis/SKILL.md` | Roteiro que o agente segue (novo) |
| `skills/vulnerability-analysis/README.md` | Explicação da skill para pessoas (novo) |
| `agent/knowledge/security-basics.md` | Vulnerabilidade, ameaça, risco, tríade CIA, matriz de severidade e boas práticas (novo) |
| `agent/persona.md` | Apenas o trecho "Modo mentor de cibersegurança" a acrescentar à persona original |
| `AGENTS.md` | Apenas as linhas a acrescentar ao `AGENTS.md` original: conhecimento, linha da tabela de skills e limite de segurança |
| `lab/app.py` | App de laboratório com SQL Injection, vulnerável de propósito |
| `lab/app_corrigido.py` | Versão com consulta parametrizada |
| `docs/img/` | Prints da análise |

## Como rodar no harness
1. Instale o Hermes: https://hermes-agent.nousresearch.com/docs
2. Baixe o agente base e este repositório:
git clone https://github.com/digitalinnovationone/dio-agent.git
git clone https://github.com/SEU-USUARIO/dio-agent-appsec.git
3. Copie as novidades para dentro do `dio-agent`:
   - a pasta `skills/vulnerability-analysis` para `dio-agent/skills/`
   - o arquivo `agent/knowledge/security-basics.md` para `dio-agent/agent/knowledge/`
   - a pasta `lab` para a raiz de `dio-agent/`
4. Abra `agent/persona.md` deste repositório e cole o trecho no final do `dio-agent/agent/persona.md`.
5. Abra `AGENTS.md` deste repositório e acrescente cada bloco na seção indicada do `dio-agent/AGENTS.md`.
6. Abra um terminal **dentro da pasta `dio-agent`** e rode `hermes`. Aberto em outro lugar, ele não encontra os arquivos.
7. Peça: "Analise o lab/app.py como especialista em AppSec."

## Melhoria escolhida
Relatório sempre no mesmo formato (contexto, achado, ATT&CK, tríade CIA, impacto,
probabilidade, severidade, correção, validação e o que não foi analisado), para comparar casos.

## Evidências
![Análise do app.py](docs/img/01-analise-app-py.png)
![Perguntas de contexto](docs/img/02-perguntas-contexto.png)
![Validação após a correção](docs/img/03-validacao.png)
![Mesma pergunta em chat genérico](docs/img/04-chat-generico.png)

## Aviso
Todos os testes usam apenas código e servidores meus, de laboratório.
