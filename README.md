# Code Smells: Uma Análise sobre o Uso de Inteligência Artificial e Linters na Qualidade de Software

## 1. O que é isto
Pacote de replicação do experimento desenvolvido pela Squad 10 (Tema 09) na disciplina de Verificação e Validação (AL0342) da Universidade Federal do Pampa (UNIPAMPA), sob orientação da Profa. Anielle Severo Lisboa de Andrade. O estudo compara experimentalmente o linter estático Pylint (v4.1.3) e o modelo de linguagem `openai/gpt-oss-120b` na detecção de três *code smells* (*Long Parameter List*, *Duplicate Code* e *Complex Conditional*) em 35 casos sintéticos de código Python, mensurando Precisão, Recall, F1-score e estabilidade entre execuções.

**Autores:** Vinicius Dorneles Pereira, José Guilherme Gonzalez Monteiro, Renata Rodrigues Vassalo da Rosa e Lucas Silveira Segabinazzi.

## 2. Como o material está organizado

    ├── corpus/                 # 35 casos em Python (45 arquivos .py) e gabarito de referência
    │   ├── CC_01..CC_10/       # 10 casos de Complex Conditional (4 a 7 níveis de if aninhados)
    │   ├── DUP_01..DUP_10/     # 10 casos de Duplicate Code (pares *_a.py e *_b.py)
    │   ├── LPL_01..LPL_10/     # 10 casos de Long Parameter List (7 a 10 parâmetros)
    │   ├── LIMPO_01..LIMPO_05/ # 5 casos de controle negativo sem code smells
    │   └── gabarito.csv        # Oráculo com caso, tipo de smell, arquivos e linhas
    ├── resultados/             # Saídas brutas (pylint_bruto.json, llm_bruto.jsonl) e metricas.csv
    ├── gerar_corpus.py         # Gera novamente o corpus sintético e o arquivo gabarito.csv
    ├── rodar_llm.py            # Executa as 175 chamadas ao LLM via API Groq (com suporte a retomada)
    ├── avaliar.py              # Compara as saídas com o gabarito e gera resultados/metricas.csv
    ├── pylintrc                # Configuração fixa do Pylint utilizada no experimento
    ├── prompt.txt              # Texto integral do prompt enviado ao modelo de linguagem
    ├── README.txt              # Notas técnicas originais de execução dos scripts
    └── LICENSE                 # Licença MIT do repositório

## 3. Como reproduzir
**Requisitos:** Python 3.10+ e pacotes `requests` e `pylint` (versão `4.1.3` utilizada no estudo):

    pip install requests pylint==4.1.3

1. **Gerar o corpus (opcional — os 35 casos já estão prontos em `corpus/`):**

       python gerar_corpus.py

2. **Executar o Pylint com a configuração fixa do experimento (leva menos de 10 segundos):**
   - Para casos de arquivo único (ex.: `LPL_01`):

         pylint --rcfile=pylintrc corpus/LPL_01/*.py

   - Para casos de `Duplicate Code` (`DUP_01` a `DUP_10`), rodar sempre os dois arquivos do par juntos:

         pylint --rcfile=pylintrc corpus/DUP_01/*.py

3. **Executar as chamadas ao LLM via API Groq (175 chamadas; leva cerca de 3 a 5 minutos; se interrompido, basta rodar novamente para retomar):**

       export GROQ_API_KEY="sua_chave"
       python rodar_llm.py

4. **Calcular as métricas e gerar `resultados/metricas.csv` (leva menos de 5 segundos):**

       python avaliar.py

5. **Verificação offline do pipeline (sem consumo de API, leva menos de 5 segundos):**

       python rodar_llm.py --simular
       python avaliar.py resultados/llm_bruto_simulado.jsonl

## 4. De onde vêm os dados
Os 35 casos em Python (totalizando 45 arquivos) foram gerados sinteticamente em novembro de 2026 pelo script `gerar_corpus.py`, segundo critérios operacionais objetivos definidos pelos autores: mais de 5 parâmetros para *Long Parameter List* (casos com 7 a 10 parâmetros), 4 ou mais níveis de condicionais aninhadas para *Complex Conditional* (casos com 4 a 7 níveis), pelo menos 6 linhas idênticas entre pares de arquivos para *Duplicate Code* e 5 casos limpos de controle negativo (incluindo dois casos de fronteira: 5 parâmetros e 3 níveis de aninhamento). O estudo não envolveu participantes humanos; portanto, não há dados pessoais a serem anonimizados.

## 5. O modelo usado
- **Modelo:** `openai/gpt-oss-120b` (modelo de pesos abertos), acessado via API de *chat completions* do Groq em novembro de 2026 (com identificador do modelo e data/hora exata registrados em cada resposta no arquivo `resultados/llm_bruto.jsonl`).
- **Parâmetros de execução:** estrutura *zero-shot* (mensagem única de usuário, sem mensagem de sistema e sem histórico), `temperature` e `top_p` nos valores padrão do serviço, limite máximo de `4000` tokens de saída, esforço de raciocínio não configurado e 5 execuções independentes por caso (175 chamadas totais) embaralhadas com semente fixa `42`.
- **Prompt:** disponível integralmente em `prompt.txt` (sem limiares numéricos explícitos e com proibição de sugestões de refatoração).

## 6. Mapa para o artigo
- `corpus/gabarito.csv` + `resultados/pylint_bruto.json` + `resultados/llm_bruto.jsonl` -> processados pelo script `avaliar.py` -> geram `resultados/metricas.csv`, que origina integralmente:
  - **Tabela 1** (*Resultados da detecção por ferramenta e tipo de code smell*): valores de TP, FP, FN, Precisão, Recall e F1-score por ferramenta e categoria.
  - **Tabela 2** (*Estabilidade média das classificações do modelo de linguagem*): concordância média das 5 execuções independentes com a classificação majoritária por categoria.

## 7. Licença e como citar
Código e scripts licenciados sob **MIT License** e *corpus*/dados sob **CC BY 4.0**.

> PEREIRA, Vinicius Dorneles; MONTEIRO, José Guilherme Gonzalez; ROSA, Renata Rodrigues Vassalo da; SEGABINAZZI, Lucas Silveira. **Code Smells: Uma Análise sobre o Uso de Inteligência Artificial e Linters na Qualidade de Software**. Universidade Federal do Pampa (UNIPAMPA), Campus Alegrete, 2026. Disponível em: https://github.com/segabinazzi01/code-smells-ia-vs-linters
