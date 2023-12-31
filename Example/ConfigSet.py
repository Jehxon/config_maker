# THIS DOCUMENT IS AUTOGENERATED BY THE CONFIGURATION MAKER PACKAGE.
# IT IS PROVIDED AS IS, DO NOT MODIFY

import yaml
import os
from dataclasses import dataclass

def EvalExpression(e):
    if(type(e) == list):
        return [EvalExpression(elt) for elt in e]
    res = str(e)
    try:
        res = eval(res)
    except:
        pass
    return res

@dataclass
class _ConfigurationSet_Category1:
    var3: str
    var4: float
    var5: str
    @classmethod
    def _fromDict(cls, param_dict: dict):
        return cls(
            EvalExpression(param_dict['var3']),
            EvalExpression(param_dict['var4']),
            EvalExpression(param_dict['var5'])
            )

@dataclass
class _ConfigurationSet_Category2_Sub_category1:
    array1: list
    text1: str
    scientific_notation_float: float
    array2: list
    @classmethod
    def _fromDict(cls, param_dict: dict):
        return cls(
            EvalExpression(param_dict['array1']),
            EvalExpression(param_dict['text1']),
            EvalExpression(param_dict['scientific_notation_float']),
            EvalExpression(param_dict['array2'])
            )

@dataclass
class _ConfigurationSet_Category2:
    sub_category1: _ConfigurationSet_Category2_Sub_category1
    var7: list
    var8: str
    var9: int
    @classmethod
    def _fromDict(cls, param_dict: dict):
        return cls(
            _ConfigurationSet_Category2_Sub_category1._fromDict(param_dict['sub_category1']),
            EvalExpression(param_dict['var7']),
            EvalExpression(param_dict['var8']),
            EvalExpression(param_dict['var9'])
            )

@dataclass
class _ConfigurationSet:
    category1: _ConfigurationSet_Category1
    category2: _ConfigurationSet_Category2
    var1: int
    var2: float
    var6: float
    var10: float
    var11: str
    @classmethod
    def _fromDict(cls, param_dict: dict):
        return cls(
            _ConfigurationSet_Category1._fromDict(param_dict['category1']),
            _ConfigurationSet_Category2._fromDict(param_dict['category2']),
            EvalExpression(param_dict['var1']),
            EvalExpression(param_dict['var2']),
            EvalExpression(param_dict['var6']),
            EvalExpression(param_dict['var10']),
            EvalExpression(param_dict['var11'])
            )

    @classmethod
    def FromFile(cls, config_file: str):
        with open(config_file, "r") as f :
            param_dict = yaml.load(f, Loader=yaml.CLoader)
            return cls._fromDict(param_dict)

config = _ConfigurationSet.FromFile(os.path.join(os.path.dirname(__file__), "config_example.yaml"))
print(config.category2.sub_category1.array1)
print(config.category2.sub_category1.array2)
print(config.var6)