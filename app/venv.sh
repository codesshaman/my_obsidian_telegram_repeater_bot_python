#!/bin/bash
if [ ! -d "venv" ]; then
    python3 -m venv venv
    chmod +x venv/bin/activate
    source venv/bin/activate
    pip install --upgrade pip
fi
echo "Теперь можно запустить виртуальное окружение командой"
echo "source venv/bin/activate"
echo "и запустить скрипт ./environment.sh"