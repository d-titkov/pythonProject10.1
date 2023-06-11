# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |

import pandas as pd
import random

# Создание исходного DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Исходный DataFrame:\n", data)

# Преобразование в one hot вид
one_hot_data = pd.get_dummies(data, columns=["whoAmI"])
one_hot_data.columns = ["is_human", "is_robot"]
one_hot_data = one_hot_data[["is_human", "is_robot"]]
print("\nDataFrame в one hot виде:\n", one_hot_data)