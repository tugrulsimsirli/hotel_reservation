# Resmi Python imajını kullanıyoruz
FROM python:3.12

# Çalışma dizinini oluşturuyoruz
WORKDIR /app

# Gerekli dosyaları kopyalıyoruz
COPY requirements.txt .

# Bağımlılıkları yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyalıyoruz
COPY ./app /app

# Uvicorn ile FastAPI'yi çalıştırıyoruz
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
