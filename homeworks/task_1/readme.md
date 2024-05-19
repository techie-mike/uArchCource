# Oracle conditional branch predictor

Реализация branch predictor находится в отдельной ветке [task_1_oracle](https://github.com/techie-mike/uArchCource/tree/task_1_oracle) данного репозитория. 100% "угадывание" достигнуто путём пропатчивания cpu, я игнорирую branch predictor и btb predictor, и в качестве предсказаний использую фактические результаты.

## IPC
Как видно по гистрограмме, IPC в случае использования oracle branch predictor дает результаты лучше чем hashed perceptron во всех случаях, исключая `623.xalan...` и `654.roms...`.

GeoMean: $IPC_{oracle} = 2.025$, $IPC_{hp} = 1.694$

![CMP_IPC](/homeworks/task_1/png/cmp_ipc.png)

## MPKI
Рассмотрим MPKI. Использвание oracle branch predictor существенно улучшило данный показатель, то нулевым он стал не на всех бенчмарках. Это связано с тем, что помимо conditional branch существуют другие типы ветвлений, которые тоже вносят вклад суммарный MKPI.

GeoMean: $MPKI_{hp} = 0.486$, $MPKI_{oracle} = NaN$

*(NOTE: получаем ошибку вычисления в случае oracle, так как некоторые MPKI равны 0)*

![CMP_IPC](/homeworks/task_1/png/cmp_mpki.png "")
