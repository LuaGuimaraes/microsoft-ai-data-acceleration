# 🚀 Microsoft AI & Data Architecture Acceleration

Repositório com projetos práticos desenvolvidos durante a aceleração de **Arquitetura de Dados e Inteligência Artificial da Microsoft (DIO)**, com foco em **engenharia de dados, governança de IA e aplicações reais para ambientes corporativos**.

Os projetos priorizam **arquiteturas reais**, decisões técnicas justificadas e preocupações práticas como **rastreabilidade, segurança e governança**.

---

## 🗂️ Estrutura do Repositório

### 📁 01. Lakehouse Architecture with Microsoft Fabric ✅
**Status:** Concluído  

Implementação de uma arquitetura **Medallion (Bronze, Silver, Gold)** ponta a ponta utilizando **Microsoft Fabric**.

**Principais pontos abordados:**
- Ingestão de dados
- Transformações com PySpark
- Delta Lake
- Modelo semântico
- Consumo via Power BI (Direct Lake)

📂 Pasta: [`01-fabric-lakehouse`](./01-fabric-lakehouse)

---

### 📁 02. AI Governance Assistant (Gemini + Langfuse) ✅
**Status:** Concluído  

Criação de um **assistente de IA corporativo** com foco em **governança, segurança e rastreabilidade**, demonstrando na prática os riscos de um uso não governado de LLMs e como mitigá-los.

O projeto contém **duas versões do mesmo bot**:

- **Versão Vulnerável:**  
  Sem filtros de segurança e sem rastreabilidade, ilustrando riscos reais em ambientes empresariais.

- **Versão Governada:**  
  Com **Content Safety** e **rastreabilidade completa via Langfuse**, permitindo auditoria de:
  - Prompts
  - Respostas
  - Tentativas de bypass
  - Uso indevido por usuários internos

⚠️ Mesmo quando um prompt “refatorado” consegue passar por filtros de conteúdo, o **Langfuse registra e sinaliza o uso**, permitindo controle não apenas do *conteúdo gerado*, mas também do *comportamento do usuário*.

📌 **Observação importante:**  
O workshop original utilizava **OpenAI + Azure AI Content Safety**.  
Devido a limitações financeiras, este projeto foi **adaptado para Google Gemini**, mantendo os mesmos conceitos de governança, segurança e observabilidade. A adaptação do código foi feita com **engenharia de prompt e apoio de ferramentas de IA**, sem perda conceitual ou arquitetural.

📂 Pasta: [`02-AI-governance-assistant`](./02-AI-governance-assistant)

---

### 📁 03. Multi-Agent Sales System 🚧
**Status:** Planejado  

Desenvolvimento de um sistema **multi-agente** voltado para fluxos de vendas B2B, integrando tomada de decisão automatizada e orquestração de agentes.

**Tecnologias previstas:**
- Microsoft Agent Framework
- Azure AI Foundry
- Integração com dados corporativos

---

## 🎯 Objetivo do Repositório

Este repositório serve como:
- Portfólio técnico
- Registro de aprendizado prático
- Demonstração de capacidade de adaptação técnica
- Aplicação real de conceitos de dados e IA em contextos corporativos

---

*Desenvolvido por **Luana Guimarães***