FROM python:3.10-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    python3-pip \
    ffmpeg \
    wget \
    bash \
    neofetch \
    software-properties-common \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir wheel && \
    pip3 install --no-cache-dir -U -r requirements.txt

COPY . .

ENV PORT=10000
EXPOSE 10000

CMD sh -c "python3 app.py & python3 -m ggn"
