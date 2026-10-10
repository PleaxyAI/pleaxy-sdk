from typing import Literal, Set, cast

ListEmployeesRole = Literal["buyer", "supplier"]

LIST_EMPLOYEES_ROLE_VALUES: Set[ListEmployeesRole] = {
    "buyer",
    "supplier",
}


def check_list_employees_role(value: str) -> ListEmployeesRole:
    if value in LIST_EMPLOYEES_ROLE_VALUES:
        return cast(ListEmployeesRole, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_EMPLOYEES_ROLE_VALUES!r}"
    )
