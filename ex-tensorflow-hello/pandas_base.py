#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-02-19 16:51:22
# @Author  : ZubinGou (zebgou@gmail.com)
# @Link    : https://github.com/ZubinGou
# @Version : $Id$

from __future__ import print_function

import numpy as np
import pandas as pd


def main():
    print(pd.__version__)
    names = pd.Series(['saun', 'funnuy', 'rainy'])
    money = pd.Series([35432, 2345234,99999])
    people = pd.DataFrame({'Name': names, 'money':money})
    print(people)
    # california_housing_dataframe = pd.read_csv("https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv", sep=",")
    # california_housing_dataframe.describe()
    # california_housing_dataframe.head()
    # california_housing_dataframe.hist('housing_median_age')
    print()
    print(type(people['Name'][1]))
    print(people['Name'][1])
    print(type(people[0:2]))
    print(people[0:2])

    print(money/1000)

    print(np.log(money))

if __name__ == "__main__":
    main()
