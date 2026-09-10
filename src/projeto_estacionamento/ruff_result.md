(.venv) PS C:\Users\ferna\dev\reativacao\Fase0\src\projeto_estacionamento> ruff check .                
I001 [*] Import block is un-sorted or un-formatted
 --> main.py:1:1
  |
1 | / from datetime import datetime
2 | | from abc import ABC, abstractmethod
3 | | from dataclasses import dataclass, field
  | |________________________________________^
4 |
5 |   @dataclass
  |
help: Organize imports
  |
  - from datetime import datetime
1 | from abc import ABC, abstractmethod
2 | from dataclasses import dataclass, field
3 + from datetime import datetime
4 +
5 |
  |

DTZ005 `datetime.datetime.now()` called without a `tz` argument
  --> main.py:36:32
   |
35 |     def registra_entrada(self):
36 |         self.horario_entrada = datetime.now()
   |                                ^^^^^^^^^^^^^^
37 |
38 |     @abstractmethod
   |
help: Pass a `datetime.timezone` object to the `tz` parameter

I001 [*] Import block is un-sorted or un-formatted
 --> test_estacionamento.py:1:1
  |
1 | / from main import Sistema, Veiculo, Carro, Caminhao, Moto
2 | | import pytest
  | |_____________^
3 |
4 |   @pytest.fixture
  |
help: Organize imports
  |
  - from main import Sistema, Veiculo, Carro, Caminhao, Moto
1 | import pytest
2 |
3 + from main import Caminhao, Carro, Moto, Sistema, Veiculo
4 +
5 +
6 | @pytest.fixture
  |

F401 [*] `main.Veiculo` imported but unused
 --> test_estacionamento.py:1:27
  |
1 | from main import Sistema, Veiculo, Carro, Caminhao, Moto
  |                           ^^^^^^^
2 | import pytest
  |
help: Remove unused import
  |
  - from main import Sistema, Veiculo, Carro, Caminhao, Moto
1 + from main import Sistema, Carro
2 | import pytest
  |

F401 [*] `main.Caminhao` imported but unused
 --> test_estacionamento.py:1:43
  |
1 | from main import Sistema, Veiculo, Carro, Caminhao, Moto
  |                                           ^^^^^^^^
2 | import pytest
  |
help: Remove unused import
  |
  - from main import Sistema, Veiculo, Carro, Caminhao, Moto
1 + from main import Sistema, Carro
2 | import pytest
  |

F401 [*] `main.Moto` imported but unused
 --> test_estacionamento.py:1:53
  |
1 | from main import Sistema, Veiculo, Carro, Caminhao, Moto
  |                                                     ^^^^
2 | import pytest
  |
help: Remove unused import
  |
  - from main import Sistema, Veiculo, Carro, Caminhao, Moto
1 + from main import Sistema, Carro
2 | import pytest
  |

Found 6 errors.
[*] 5 fixable with the `--fix` option.