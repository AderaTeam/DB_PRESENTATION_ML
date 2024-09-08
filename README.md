# API для генерации презентаций

## Сервисы

- `./topic_modelling_service` - сервис для выделения топиков и контекстов из текста; 
- `./gpt_service` - сервис для нормализации выделеннных контекстов и преобразования их в текст презентации;
- `./image_generation_service` - сервис для генерации изображений;
- `./presentation_generation_service` - сервис для удобной комуникации ;


## Алгортм

1) Текст подаётся на вход сервиса `./presentation_generation_service` по эндпоинту *generate_presentation*;
2) Текст разбивается на сегменты по абзацам;
3) `./presentation_generation_service` обращается к сервису `./topic_modde` по эндпоинту *topic_moddeling*;
4) ``