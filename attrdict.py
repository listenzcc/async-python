"""
File: attrdict.py
Author: Chuncheng Zhang
Date: 2024-03-15
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Define AttrDict

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2024-03-15 ------------------------
# Requirements and constants
import traceback


# %% ---- 2024-03-15 ------------------------
# Function and class
class AttrDict(dict):
    def __getattr__(self, key):
        try:
            return self.__getitem__(key)
        except AttributeError as err:
            raise err
        except Exception as err:
            raise AttributeError(
                f'__getattr__ only allows AttributeError, the real is: {traceback.format_exc()}')

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)


# %% ---- 2024-03-15 ------------------------
# Play ground


# %% ---- 2024-03-15 ------------------------
# Pending


# %% ---- 2024-03-15 ------------------------
# Pending
