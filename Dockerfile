# Resmi Python imajını kullanıyoruz
FROM python:3.12

# Çalışma dizinini /hotel_reservation olarak ayarlıyoruz
WORKDIR /hotel_reservation

# Gereken dosyaları kopyalıyoruz
COPY requirements.txt .

# Bağımlılıkları yüklüyoruz
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodlarını kopyalıyoruz
COPY ./app /hotel_reservation/app

# Uvicorn ile FastAPI'yi çalıştırıyoruz
CMD ["uvicorn", "app.main:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]
