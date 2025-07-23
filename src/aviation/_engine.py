"""Define SystemsModel class to create links between transforms."""

import collections.abc
import typing

from aviation._model import Transform


class SystemsModel:
    def __init__(self, transforms: collections.abc.Collection[Transform[typing.Any, ...]]) -> None:
        self.transforms = set(transforms)

    def evaluate(self, inputs: dict[str, typing.Any], output: str) -> typing.Any:  # noqa: ANN401
        # if the `output` is in the `inputs`, return the value
        if output in inputs:
            return inputs[output]
        # The requested `output` is not in `inputs`, so is in `self.transforms`
        for transform in self.transforms:
            if transform.name == output:
                break
        else:  # if we never get break, then the `output` is not in `self.transforms`
            message = f"No transform with name {output}"
            raise ValueError(message)
        for parameter in transform.parameters:
            if parameter not in inputs:
                inputs[parameter] = self.evaluate(inputs, parameter)

        # Evaluate and return the `transform` associated with the passed `output`
        arguments = {parameter: inputs[parameter] for parameter in transform.parameters}
        return transform(**arguments)
