FROM --platform=linux/amd64 python:3.11

# Instalar dependências
RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb \
    x11vnc \
    fluxbox \
    net-tools \
    git

# Clonar noVNC e websockify
RUN git clone --branch v0.6.2 https://github.com/novnc/noVNC.git /opt/novnc && \
    git clone https://github.com/novnc/websockify /opt/novnc/utils/websockify


# Copie seu aplicativo e scripts para o container
COPY . .
COPY start-vnc.sh /start-vnc.sh

# Dê permissão de execução aos scripts
RUN chmod +x /start-vnc.sh

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe as portas corretas
EXPOSE 5900 6080

# Defina a variável de ambiente para o Xvfb
ENV DISPLAY=:99

# Usar o script para iniciar o servidor X virtual e o noVNC
CMD ["/start-vnc.sh"]
