import sys
import os

# Exception prints...
def printException(func_name: str, error: str) -> None:
    print(f'{func_name}: {error}')
    _, __, exc_tb = sys.exc_info()
    print(f'Line No: {exc_tb.tb_lineno}')

