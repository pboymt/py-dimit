from decimal import Decimal
import re

__DIMEMSION_REGEX__ = re.compile(r'(?P<dim>\S)(?P<time>-?\d+)?')

__allowed_dimensions__ = ('L', 'M', 'T')


class Dimension:

    def __init__(self, dimension: str = ""):
        self.dim_dict = {
            "L": Decimal(0),
            "M": Decimal(0),
            "T": Decimal(0),
        }
        self.parse(dimension)

    @property
    def dimensionless(self):
        return self.__str__() == ""

    @property
    def L(self) -> Decimal:
        return self.dim_dict["L"]

    @property
    def M(self) -> Decimal:
        return self.dim_dict["M"]

    @property
    def T(self) -> Decimal:
        return self.dim_dict["T"]

    def to_str(self):
        output = ""
        for d in self.dim_dict:
            t = self.dim_dict[d]
            if t == 0:
                continue
            if t == 1:
                output += d
            else:
                output += f"{d}{t}"
        return output

    def parse(self, dimension: str) -> dict[str, Decimal]:
        result = __DIMEMSION_REGEX__.findall(dimension)
        for d, t in result:
            if d in __allowed_dimensions__:
                self.dim_dict[d] += Decimal(t or "1")
            else:
                raise ValueError(f"Dimension {d} is not allowed.")

    def __str__(self) -> str:
        return f"Dimension({self.to_str()})"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash(self.to_str())

    def __mul__(self, other: 'Dimension'):
        return Dimension(self.to_str() + other.to_str())

    def __truediv__(self, other: 'Dimension'):
        return Dimension(self.to_str() + (other ** -1).to_str())

    def __pow__(self, power: int):
        dim = Dimension(self.to_str())
        for d in dim.dim_dict:
            dim.dim_dict[d] *= power
        return dim

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Dimension):
            for d in __allowed_dimensions__:
                if self.dim_dict[d] != __o.dim_dict[d]:
                    return False
            return True
        else:
            return False


L = Dimension('L')
M = Dimension('M')
T = Dimension('T')
DIMLESS = Dimension()
