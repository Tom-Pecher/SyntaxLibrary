
## Python: 1.1.2.19 - Other Internal Types

# Python’s types module gives official names for many internal types:
import types
type(lambda x: x) == types.FunctionType  # True

# Others include:
#  - FunctionType
#  - LambdaType
#  - GeneratorType
#  - ModuleType
#  - MethodType
#  - BuiltinFunctionType
#  - CoroutineType, AsyncGeneratorType
#  - ClassType
