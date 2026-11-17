# Lab 9. Kubernetes basics (П09)

## Что было сделано
1. Развернут мини-кластер Kubernetes (Minikube) на виртуальной машине.
2. Настроен доступ к кластеру с хостовой машины через приложение Lens (проброс портов, конфигурация).
3. Собран Docker-образ Flask (`flask:v1`) и загружен в Minikube.
4. Созданы манифесты для развертывания приложения Flask + Redis.
5. Развернуты Deployment для Flask (5 реплик) и Redis (1 реплика).
6. Активирован балансировщик входящих запросов (Service типа LoadBalancer).
7. Проверена работа приложения: счетчик посещений успешно растет.
8. Выполнено обновление веб-сервиса на новую версию (RollingUpdate с `flask:v5`).

## Структура проектов
- `flask_redis/` — исходный код приложения (app.py, Dockerfile, requirements.txt).
- `flask_redis_k8s/` — манифесты Kubernetes для развертывания.

## Файлы манифестов (папка `flask_redis_k8s`)
- `flask.yaml` — манифест Flask Deployment.
- `flask-service.yaml` — манифест Flask Service (LoadBalancer).
- `redis.yaml` — манифест Redis Deployment.
- `redis-service.yaml` — манифест Redis Service (ClusterIP).

## Скриншоты (папка `скрины`)

| Файл | Что изображено на скриншоте |
| :--- | :--- |
| `01-kubectl-and-minikube-install.png` | Установка утилит kubectl и minikube |
| `02-minikube-status.png` | Проверка статуса Minikube и ноды кластера |
| `03-scp-copy.png` | Копирование конфига и сертификатов на Windows (scp) |
| `04-port-forward.png` | Настройка проброса портов в VirtualBox |
| `05-ip-addr.png` | Проверка IP-адреса виртуальной машины |
| `06-iptables.png` | Команда iptables для перенаправления трафика |
| `07-config-fixed.png` | Исправленный конфигурационный файл для Lens |
| `08-lens-connected.png` | Приложение Lens с подключенным кластером |
| `09-build-and-apply.png` | Сборка образов и применение манифестов |
| `10-pods-and-services.png` | Список подов (Running) и сервисов |
| `11-flask-port-forward.png` | Проброс портов для доступа к Flask |
| `12-browser-counter.png` | Работа счетчика посещений (1 раз) |
| `13-browser-counter-2.png` | Работа счетчика посещений (5 раз) |
| `14-app-code-v5.png` | Измененный код приложения (VERSION 5) |
| `15-build-image-v5.png` | Процесс сборки нового образа flask:v5 |
| `16-install-packages-v5.png` | Установка зависимостей при сборке |
| `17-image-exported.png` | Успешное завершение сборки образа |
| `18-update-to-v5.png` | Обновление образа в Deployment |
| `19-describe-deployment.png` | Подробная информация о Deployment  |
| `20-rollout-events.png` | События обновления |
| `21-rollout-success.png` | Статус успешного завершения обновления |
| `22-final-result-v5.png` | Финальный результат в браузере |
