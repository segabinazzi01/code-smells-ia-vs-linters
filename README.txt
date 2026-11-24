CORPUS - Code Smells: IA vs Linters (AL0342)

corpus/<id>/        35 trechos: LPL_01-10, CC_01-10, DUP_01-10, LIMPO_01-05
corpus/gabarito.csv gabarito (congelar com commit/data ANTES de rodar qualquer ferramenta)
pylintrc            configuracao fixa do Pylint (limiares padrao)
prompt.txt          prompt fixo enviado ao LLM
gerar_corpus.py     gera o corpus de novo

Rodar o Pylint em um trecho:
  pylint --rcfile=pylintrc corpus/LPL_01/*.py
  (DUP: sempre rodar os 2 arquivos do trecho juntos)

COMO RODAR O EXPERIMENTO (Groq)
1) pip install requests pylint
2) export GROQ_API_KEY="sua_chave"   (nunca coloque a chave em arquivo do projeto)
3) python rodar_llm.py               (175 chamadas; se parar, rode de novo: retoma)
4) python avaliar.py                 (gera resultados/metricas.csv)
Teste sem API: python rodar_llm.py --simular  e  python avaliar.py resultados/llm_bruto_simulado.jsonl
(apague a pasta resultados/ antes da execucao oficial)
