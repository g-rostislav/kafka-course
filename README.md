# Установка зависимостей

1. **Сборка образа для консьюмера**
```bash
make build-consumer 
```

2. **Сборка образа для продюсера**
```bash
make build-producer
```


# Запуск приложений

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