# from datetime import date
#
#
# def my_deco(func):
#
#     print("first")
#     func()
#     print("last")
#
# @my_deco
# def another_fucn():
#     print("midle")
#
#
# def bread(func):
#     def wrapper():
#         print("</------\>")
#         func()
#         print("<\______/>")
#
#     return wrapper
#
#
# def ingredients(func):
#     def wrapper():
#         print("#помидоры#")
#         func()
#         print("~салат~")
#
#     return wrapper
#
#
# @bread
# @ingredients
# def sandwich(food="--ветчина--"):
#     print(food)
#
#
# sandwich()
#
# # random Person
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)
#
#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))
#
# person = Person('Adam', 19)
# person.display()
#
# person1 = Person.fromBirthYear('John',  1985)
# person1.display()


#
# from datetime import datetime
# import time
#
# begin = datetime.now()
# print(f'begin function name_of_table at: {begin.strftime("%m/%d/%Y, %H:%M:%S")}')
#
#
# time.sleep(4)
#
# end = datetime.now()
#
# print(f'begin function name_of_table at: {end.strftime("%m/%d/%Y, %H:%M:%S")}')
# print(f"Latency of function name_of_function: {(end - begin).seconds}")
import base64

import yaml
import zlib

param_yaml = """
eJyNVMFu2zAMvfcr9AH+Al/bDjWWxFmSHnoSVJt2hcmSJ1JFg2H/PkpO7cbTit6kR/KR4nsQ2FeJ
oev0WymkdXb0rr0hryx2zg+KtLMSCcbyRogW2jCCbJwJgy1Fq0hJdME3IAk5ri2CJ47bVsfCUthg
DAdG5SkhsjEqIOQCiRSvWfkMMubEVK8H5c/yJ5xLAa9gqWoZXjLVs4rMHjptgRNfHJLEMw8//Ib5
lX+WGvxlSoFgoKF3wkKEMTZtT3qAQhg+2ua8xYLbuwYQte03C0iOlDmCIiyYVojGBUt1dyRFAeVt
vd0XK6w+Pdwf1uCx3tytsf2hvnu8PVX1Tn6vNpscf7X78VgdntaVKX2FPWQ61Pv73USbXXl8Peto
+7jxYiW2+HaotwLJgxpmVD0bWLabrqVIKmgb1+tYFNX3HnruEf1CyvdAH7SLfBg+1e5S83X2lCmx
eYFBzcaJo/PTruSesVl1NjRllU9bS8HFAdP9Xwfk8OSCXCA6YSH/1BG5lIsjcqFY8j/m6I7smOyQ
Cc86JKIwOeiDVeY1rhxDvGIkNYzF+z9xDU5KXIFMfUHXX8pfAXu4EQ==
"""


def get_distinct_partvalues():
    if not partition_columns:
        return ""
    d_df = df.select(partition_columns).drop_duplicates()
    # high cardinality return empty partition clause
    if d_df.count() > 1000:
        return ""
    pc = d_df.collect()
    jc = []
    for r in pc:
        jc.append("(" + " and ".join([f"target.{c} = '{r[c]}'" for c in d_df.columns]) + ")")

param_yaml = yaml.load(zlib.decompress(base64.b64decode(param_yaml.encode())).decode(), Loader=yaml.FullLoader)
pky_cols = [c.strip() for c in param_yaml["transformation_step"]["primary_key"].split(",")]
join_condition = " and ".join([f'target.{c} <=> source.{c}' for c in pky_cols])
test = param_yaml["transformation_step"]["partition_clause"]
partition_columns = [c.strip() for c in param_yaml["transformation_step"]["partition_columns"].split(",")] if param_yaml["transformation_step"]["partition_columns"] else None
print(param_yaml)
print((pky_cols))
print(join_condition)
print(test)
print(partition_columns)
# if param_yaml["transformation_step"]["partition_clause"]:
#     return join_condition + " and " + param_yaml["transformation_step"]["partition_clause"]
# else:
#     return join_condition + get_distinct_partvalues()