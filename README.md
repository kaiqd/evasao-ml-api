#  Evasão ML API

API em **Python (FastAPI)** responsável por expor o modelo de Machine Learning que prevê risco de evasão acadêmica.

---

## 📌 Objetivo

Este projeto disponibiliza, via **REST API**, um modelo de **XGBoost** previamente treinado.  
O objetivo é permitir que aplicativos clientes (como o [evasao-ios-app](https://github.com/skaiqd/evasao-ios-app)) enviem dados de alunos e recebam de volta a **probabilidade de evasão**.

---

## 🚀 Como rodar o projeto

### Pré-requisitos
- Python **3.10+**
- Ambiente virtual configurado (recomendado)
- Dependências listadas em `requirements.txt`

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/evasao-ml-api.git
cd evasao-ml-api
```

### 2. Criar ambiente virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Rodar o servidor
```bash
uvicorn app:app --host 0.0.0.0 --port $PORT --reload
```

### Exemplo de fluxo

1. Aplicativo cliente envia:

```json
{
  "alunos": [
    {
      "faltas": 25,
      "nota_media": 60.5,
      "horas_trabalho": 20,
      "idade": 22
    }
  ]
}
```

2.	A API processa os dados e aplica o modelo de Machine Learning.
3.	O backend retorna um JSON com a probabilidade de evasão:

```json
{
  "results": [
    {
      "risk_score": 0.73,
      "model_version": "xgb_v1"
    }
  ]
}
```
4. O aplicativo exibe o resultado para o usuário.




