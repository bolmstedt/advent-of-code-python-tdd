import pathlib
import pkgutil
from importlib import machinery
from types import ModuleType

from aoc import solver


def create_solver(module_path: pathlib.Path) -> solver.Solver:
    module = machinery.SourceFileLoader("solution", str(module_path)).load_module()

    try:
        solution_class = getattr(module, "Solution")  # noqa: B009
    except AttributeError as err:
        raise ValueError("Package is not a valid solution module") from err

    return solver.Solver(solution_class(get_input_data(module)))


def get_file_data(module: str, file_name: str) -> str:
    input_data = pkgutil.get_data(module, file_name)

    if not input_data:
        raise FileNotFoundError(
            "No file named {name} found in {module}".format(
                name=file_name,
                module=str(module),
            ),
        )

    return input_data.decode("utf-8")


def get_module_data(module: ModuleType, file_name: str) -> str:
    return get_file_data(module.__name__, file_name)


def get_input_data(module: ModuleType) -> str:
    return get_module_data(module, "input.txt")
