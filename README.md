# Получить прогноз погоды

Скрипт печатает в терминал прогноз погоды с сайта [wttr.in](https://wttr.in) для городов из списка `locations`

Если сайт с погодой сломался, воспользуйтесь [дубликатом сайта](http://wttr.dvmn.org/)

В запросе передаются следующие параметры:

`n` - Погода в “узком формате”, прогноз только на день и ночь, без “утра” или “вечера”

`T` - чтобы отключить терминальные последовательности (без цветов)

`q` - тихая версия (без текста "Прогноз погоды")

`m` - для метрических (СИ)

`M` - скорость ветра в м/с

Подробнее обо всех параметрах [здесь](https://wttr.in/:help)

## Установка

Скачайте код с GitHub.
Python3 должен быть уже установлен.
Установите зависимости:

```
pip install -r requirements.txt
```

## Запуск

```
python main.py
```

Вы увидите русифицированный прогноз погоды на ближайшие 3 дня:
```
London

      \   /     Солнечно
       .-.      +1(-2) °C
    ― (   ) ―   ← 3 м/c
       `-’      10 км
      /   \     0.0 мм
                        ┌─────────────┐
┌───────────────────────┤ Вт. 13 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │               Пасмурно       │
│      .--.     +2(-1) °C      │      .--.     +2(0) °C       │
│   .-(    ).   ← 2-3 м/c      │   .-(    ).   ↙ 1-2 м/c      │
│  (___.__)__)  10 км          │  (___.__)__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Ср. 14 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│     \   /     Ясно           │
│  _ /"".-.     +3(-1) °C      │      .-.      0(-4) °C       │
│    \_(   ).   ↓ 4-5 м/c      │   ― (   ) ―   ↓ 3-4 м/c      │
│    /(___(__)  10 км          │      `-’      10 км          │
│               0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Чт. 15 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Ясно           │
│      .-.      +4(2) °C       │      .-.      0(-3) °C       │
│   ― (   ) ―   ↘ 2 м/c        │   ― (   ) ―   ↓ 2-3 м/c      │
│      `-’      10 км          │      `-’      10 км          │
│     /   \     0.0 мм | 0%    │     /   \     0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

svo

                Пасмурно
       .--.     0(-2) °C
    .-(    ).   ↑ 5 м/c
   (___.__)__)  10 км
                0.0 мм
                        ┌─────────────┐
┌───────────────────────┤ Вт. 13 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Умеренный снег │      .-.      Сильный снег   │
│     (   ).    -1(-5) °C      │     (   ).    -1(-2) °C      │
│    (___(__)   ↑ 2-3 м/c      │    (___(__)   ← 0-1 м/c      │
│    * * * *    5 км           │    * * * *    2 км           │
│   * * * *     0.1 мм | 0%    │   * * * *     0.4 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Ср. 14 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Сильный снег   │               Облачно        │
│     (   ).    -5(-10) °C     │      .--.     -8(-15) °C     │
│    (___(__)   → 3-5 м/c      │   .-(    ).   ↗ 3-6 м/c      │
│    * * * *    2 км           │  (___.__)__)  10 км          │
│   * * * *     1.7 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Чт. 15 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │      .-.      Сильный снег   │
│      .--.     -8(-13) °C     │     (   ).    -5(-12) °C     │
│   .-(    ).   ↖ 2-4 м/c      │    (___(__)   ↖ 6-10 м/c     │
│  (___.__)__)  10 км          │    * * * *    2 км           │
│               0.0 мм | 0%    │   * * * *     0.4 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Все новые фичи публикуются здесь: @igor_chubin

Cherepovets

     \  /       Переменная облачность
   _ /"".-.     -4(-9) °C
     \_(   ).   ↑ 3 м/c
     /(___(__)  10 км
                0.0 мм
                        ┌─────────────┐
┌───────────────────────┤ Вт. 13 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│               Облачно        │
│  _ /"".-.     -3(-7) °C      │      .--.     -4(-9) °C      │
│    \_(   ).   ↑ 3-5 м/c      │   .-(    ).   ↖ 2-4 м/c      │
│    /(___(__)  10 км          │  (___.__)__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Ср. 14 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Дымка          │               Пасмурно       │
│  _ - _ - _ -  -7(-11) °C     │      .--.     -7(-14) °C     │
│   _ - _ - _   ↖ 2-3 м/c      │   .-(    ).   ↗ 4-6 м/c      │
│  _ - _ - _ -  2 км           │  (___.__)__)  10 км          │
│               0.0 мм | 0%    │               0.0 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Чт. 15 дек. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │      .-.      Сильный снег   │
│      .-.      -8(-13) °C     │     (   ).    -6(-13) °C     │
│   ― (   ) ―   ↑ 3-5 м/c      │    (___(__)   ↖ 5-7 м/c      │
│      `-’      10 км          │    * * * *    2 км           │
│     /   \     0.0 мм | 0%    │   * * * *     0.4 мм | 0%    │
└──────────────────────────────┴──────────────────────────────┘
```

## Цель проекта
Проект написан в образовательных целях.
