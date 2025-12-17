# 🤖 AI Governance Assistant  

### Uso consciente, rastreável e auditável de Inteligência Artificial
Este projeto faz parte da **Aceleração Microsoft – IA e Arquitetura de Dados (DIO)** e tem como objetivo demonstrar, na prática, **como implementar governança, auditoria e observabilidade no uso de modelos de linguagem (LLMs)** em ambientes corporativos.

Ao invés de focar apenas em “bloquear respostas”, este projeto explora **como monitorar o comportamento de uso da IA**, identificar riscos e manter rastreabilidade completa para fins de compliance, auditoria e segurança.
---

## 🧠 Contexto do Problema
Em ambientes empresariais e governamentais, o risco não está apenas **no que a IA responde**, mas **em como os usuários interagem com ela ao longo do tempo**.

Perguntas reformuladas, tentativas repetidas, mudanças sutis de contexto e engenharia de prompt podem permitir que conteúdos sensíveis ou potencialmente ilegais “passem” pelos filtros tradicionais de segurança.

Este projeto demonstra como **a governança não deve depender apenas do modelo**, mas sim de uma **arquitetura de observabilidade e auditoria**.
---

## 🎯 Objetivos do Projeto
- Demonstrar **governança aplicada ao uso de LLMs**
- Implementar **auditoria de prompts e respostas**
- Detectar **padrões de uso sensíveis ou de risco**
- Manter **rastreamento completo (traceability)**
- Diferenciar **content safety** de **uso indevido**
- Simular cenários reais de ambiente corporativo
---

## 🏗️ Arquitetura e Componentes

### 🔹 Interface
- **Streamlit** para interação com o usuário

### 🔹 Modelo de Linguagem
- **Google Gemini**
- Utilizado como alternativa ao OpenAI por limitações financeiras comuns a estudantes  
- A escolha do modelo **não impacta os princípios de governança demonstrados**

### 🔹 Governança e Observabilidade
- **Langfuse**
  - Tracing de prompts e respostas
  - Registro de tentativas bloqueadas e permitidas
  - Auditoria de comportamento ao longo do tempo
  - Classificação de risco baseada no uso, não apenas no conteúdo

### 🔹 Segurança de Conteúdo
- Regras de compliance aplicadas antes e depois da chamada ao modelo
- Bloqueio explícito de perguntas diretas ilegais
- Registro de tentativas de “prompt refactoring”
---

## 🔍 O Diferencial: Governança Baseada em Uso
Mesmo quando uma pergunta **passa pelos filtros do modelo** por estar formulada de forma educacional ou acadêmica, o sistema:

- Mantém o histórico completo da interação
- Registra tentativas anteriores bloqueadas
- Permite auditoria posterior
- Evidencia padrões de uso sensível

Isso reflete práticas reais de:
- **Auditoria corporativa**
- **Insider risk management**
- **Compliance e governança de IA**
---

## 🔧 Decisão Técnica: Uso do Gemini
Devido a limitações financeiras comuns a estudantes, foi necessário **refatorar o código originalmente pensado para OpenAI**, adaptando-o para uso com **Google Gemini**.

Essa adaptação foi feita de forma consciente, utilizando:
- Engenharia de prompt
- Apoio de IA como ferramenta auxiliar de desenvolvimento
- Avaliação crítica das diferenças entre APIs

Essa decisão **não compromete o objetivo do projeto**, que é demonstrar governança, auditoria e rastreabilidade, independentemente do fornecedor do modelo.
---

## ⚠️ Limitações Conhecidas
- Projeto educacional, não implantado em ambiente produtivo real
- Regras de risco simplificadas para fins didáticos
- Classificação de risco baseada em heurísticas, não em modelos dedicados

Essas limitações são **intencionais** e fazem parte do escopo educacional.
---

## 🚀 Próximos Passos
- Integração com **Azure AI Content Safety**
- Pontuação automática de risco por sessão
- Dashboards executivos de uso e compliance
- Integração com pipelines de MLflow
- Simulação de políticas internas por perfil de usuário
---

## 📜 Aviso Ético
Este projeto tem **finalidade exclusivamente educacional**.  
Nenhuma informação apresentada deve ser interpretada como incentivo, instrução ou apoio a práticas ilegais.

O foco é **prevenção, auditoria e governança** no uso responsável de Inteligência Artificial.
---

Desenvolvido por **Luana Guimarães**  