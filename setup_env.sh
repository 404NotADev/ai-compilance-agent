#!/bin/bash

# ============================================================
# AI-Комплаенс Агент - Скрипт быстрой настройки окружения
# ============================================================

set -e

echo ""
echo "========================================================"
echo " AI-Комплаенс Агент - Настройка окружения"
echo "========================================================"
echo ""

# Проверяем наличие .env.example
if [ ! -f ".env.example" ]; then
    echo " Ошибка: Файл .env.example не найден!"
    exit 1
fi

# Проверяем, существует ли уже .env
if [ -f ".env" ]; then
    echo "  ВНИМАНИЕ: Файл .env уже существует!"
    read -p "Перезаписать его? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "ℹ  Отменено. Используйте существующий .env файл."
        exit 0
    fi
fi

echo " Копирование .env.example в .env..."
cp .env.example .env

echo ""
echo " Файл .env создан!"
echo ""
echo "========================================================"
echo " СЛЕДУЮЩИЕ ШАГИ:"
echo "========================================================"
echo ""
echo "1. Откройте файл .env для редактирования:"
echo "   nano .env"
echo ""
echo "2. Заполните ОБЯЗАТЕЛЬНЫЕ переменные:"
echo "   - SECRET_KEY (сгенерируйте: python -c \"from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())\")"
echo "   - DATABASE_URL (postgres://...)"
echo "   - REDIS_URL (redis://...)"
echo "   - BACKBLAZE_* (credentials из B2)"
echo "   - REPLICATE_API_TOKEN (токен из replicate.com)"
echo ""
echo "3. Заполните РЕКОМЕНДУЕМЫЕ переменные:"
echo "   - EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD"
echo "   - CLOUDFLARE_CDN_URL (если используете CDN)"
echo ""
echo "4. Проверьте конфигурацию:"
echo "   python backend/compliance_app/config_validator.py"
echo ""
echo "5. Запустите миграции:"
echo "   cd backend"
echo "   python manage.py migrate"
echo "   python manage.py createsuperuser"
echo ""
echo "6. Запустите приложение:"
echo "   gunicorn --bind 0.0.0.0:8000 compliance_app.wsgi:application"
echo ""
echo "========================================================"
echo ""
echo " Документация: см. DEPLOYMENT.md"
echo ""
