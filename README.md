Игра в пьяницу
=======
![сравнение картинок](https://github.com/discobunnyy/drunkard_card_game/blob/main/similar.png?raw=true "сравнение королевы бубнов и королевы пиков")

Данная программа получает на вход фото(скриншоты) двух карт: первое от первого игрока и второе карты от второго игрока. Далее происходит сравнение карт - введеных и уже имеющихся в системе. На основе количества сходств определяется, какая карта была передана пользователем. После пользователь вводит козырную масть и происходит игра. 

Праивла игры
----
1. Если обе карты козырные, то выигрывает карта с большим номиналом (если номинал карт равен, то это ничья)
2. Если одна из карт козырная, товыигрывает именно она, вне зависимости от второй карты
3. Если ни одна из карт не козырная, то выигрывает та, что имеет больший номинал (если номинал карт равен, то это ничья)

Некоторые замечания
---
1. Козырная масть должна вводиться на английском языке с маленькой буквы без ошибок и единственном числе
2. Карта первого игрока должна называться "card_1.png" и быть в формате PNG соответсвенно 
3. Карта второго игрока должна называться "card_2.png" и быть в формате PNG соответсвенно 
4. Можно использовать карты, хранящиеся в папке images, другие карты программа не распознает или сделает это непраивльно
