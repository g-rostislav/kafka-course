## Введение
### Producer
+ `./producer/Dockerfile` - Dockerfile для сборки образа для клиента продюсера
+ `./producer/main.py` - точка входа в клиент продюсера:
  1. Парсинг аргументов для запуска (CLI args), либо забирает из ENV VARS
  2. Запуск клиента
+ `./producer/producer.py` - код клиента

### Consumer
+ `./consumer/Dockerfile` - Dockerfile для сборки образа для клиента консьюмера
+ `./consumer/main.py` - точка входа в клиент консьюмера:
  1. Парсинг аргументов для запуска (CLI args), либо забирает из ENV VARS
  2. Запуск клиента
+ `/consumer/consumer.py` - код клиента

## Установка зависимостей
1. **Сборка образа для консьюмера**
```bash
make build-consumer 
```
2. **Сборка образа для продюсера**
```bash
make build-producer
```

## Запуск приложений
1. Запуск кластера (три брокера kafka, zookeeper + ui)
```bash
make run-cluster 
```
2. Создаем топик "my_topic"
```bash
make create-topic
```
3. Запускаем продюсер
```bash
make run-producer
```
4. Запускаем single consumer
```bash
make run-consumer-single
```

5. Запускаем batch consumer
```bash
make run-consumer-batch
```