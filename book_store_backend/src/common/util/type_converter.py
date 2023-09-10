from typing import List, Type, Union


class TypeConverter:
    @staticmethod
    def convert_to_dict(obj: Union[object, tuple], types: List[Type] = None) -> dict:
        if types is None:
            types = []

        def convert_recursive(value):
            if isinstance(value, tuple(types)):
                return TypeConverter.convert_to_dict(value, types)
            elif isinstance(value, list):
                return [convert_recursive(sub)
                        if isinstance(sub, str)
                        else TypeConverter.convert_to_dict(sub, types)
                        for sub in value]
            else:
                return value

        result_dict = {}

        for key, value in vars(obj).items():
            if key.startswith('__'):
                continue
            result_dict[key] = convert_recursive(value)

        return result_dict
