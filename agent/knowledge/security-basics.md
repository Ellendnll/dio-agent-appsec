# Fundamentos de segurança

## Conceitos
- **Vulnerabilidade:** fraqueza em um sistema, código ou processo (ex.: SQL montado com texto do usuário).
- **Ameaça:** algo ou alguém que pode explorar a fraqueza (ex.: atacante externo, funcionário malicioso, malware).
- **Risco:** chance de uma ameaça explorar uma vulnerabilidade e o dano causado. Risco = probabilidade × impacto.
- **Exploração:** o ato de aproveitar a vulnerabilidade.
- **Mitigação:** ação que reduz o risco (correção, controle, monitoramento).

## A tríade CIA
- **Confidencialidade:** só quem deve acessar, acessa (vazamento de dados quebra isso).
- **Integridade:** os dados não são alterados indevidamente (um UPDATE malicioso quebra isso).
- **Disponibilidade:** o sistema funciona quando precisa (queda por ataque ou erro quebra isso).

## Matriz de severidade
| Probabilidade \ Impacto | Baixo | Médio | Alto |
|---|---|---|---|
| Baixa | Baixa | Baixa | Média |
| Média | Baixa | Média | Alta |
| Alta | Média | Alta | Crítica |

Justifique sempre com o contexto: exposição à internet, sensibilidade dos dados, facilidade de exploração, controles existentes.

## Referências
- **OWASP Top 10:** principais categorias de risco em aplicações web.
- **CWE:** catálogo de tipos de falhas de software.
- **MITRE ATT&CK:** catálogo de táticas e técnicas de atacantes. Exemplos: T1190 (explorar aplicação exposta), T1078 (contas válidas).

## Boas práticas
- Consultas parametrizadas, nunca concatenação de entrada em SQL.
- Validar e tratar toda entrada externa.
- Menor privilégio (contas e permissões mínimas).
- Senhas com hash forte e salt, nunca em texto puro.
- Segredos fora do código (variáveis de ambiente, cofres).
- Atualizar sistemas e dependências.
- Expor só o necessário; fechar portas e serviços sem uso.
- Logs e monitoramento; backups testados.
- Defesa em camadas.
- Testar só o que é seu ou está autorizado por escrito.
