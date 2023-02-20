from av.container.input import InputContainer as AvInputContainer
from av2.container.core import Container
from av2.container.streams import StreamContainer


class InputContainer(AvInputContainer, Container):
    streams: StreamContainer

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
