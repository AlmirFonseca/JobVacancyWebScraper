#!/bin/bash
# Inicie o Xvfb, o servidor X virtual
Xvfb :99 -screen 0 1024x768x24 &

# Aguarde um pouco para o Xvfb iniciar
sleep 5

# Inicie o servidor VNC
x11vnc -display :99 -nopw -listen localhost -xkb -forever &

# Aguarde um pouco para o x11vnc iniciar
sleep 5

# Abre o servidor de email
python -m smtpd -n -c DebuggingServer localhost:1025 &

sleep 5

# Inicie o gerenciador de janelas
fluxbox &

# Inicie o servidor noVNC
/opt/novnc/utils/launch.sh --listen 6080 --vnc localhost:5900 &


# Execute a aplicação Tkinter
python3 app.py


