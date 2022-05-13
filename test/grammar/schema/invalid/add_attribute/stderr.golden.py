import sys
import kclvm.kcl.error as kcl_error
import os

cwd = os.path.dirname(os.path.realpath(__file__))

kcl_error.print_kcl_error_message(
    kcl_error.get_exception(
        err_type=kcl_error.ErrType.CannotAddMembers_TYPE,
        file_msgs=[
            kcl_error.ErrFileMsg(
                filename=cwd + "/main.k",
                line_no=10,
                col_no=5,
                arg_msg="'first' is not defined in schema 'Girl'"
            )
        ],
        arg_msg="Cannot add member 'first' to schema 'Girl'"
    ),
    file=sys.stdout
)

