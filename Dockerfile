# Imagem base oficial leve
FROM python:3.10-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos de dependências
COPY app/requirements.txt .

# Instalar dependências sem salvar cache (reduz tamanho da imagem)
# RNF02: Garante inicialização rápida e leveza
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código
COPY ./app ./app

# Expor a porta que a aplicação roda
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]