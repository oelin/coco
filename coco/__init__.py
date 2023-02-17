from typing import Callable, Any
import dis
import marshal
import pickle


Data = Any
Decoder = Callable[None, Callable]


def encode(data: Data, decoder: Decoder) -> Data:

        decoder = dis.Bytecode(decoder)
        decoder = marshal.dumps(decoder.codeobj)

        return pickle.dumps((data, decoder))


def decode(data: Data) -> Data:

        data, decoder = pickle.loads(data)
        decoder = marshal.loads(decoder)

        return eval(decoder)(data)
