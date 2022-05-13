
import sys
import kclvm.kcl.error as kcl_error
import os

cwd = os.path.dirname(os.path.realpath(__file__))

kcl_error.print_kcl_error_message(
    kcl_error.get_exception(err_type=kcl_error.ErrType.AssertionError_TYPE,
                            file_msgs=[
                                kcl_error.ErrFileMsg(
                                    filename=cwd + "/main.k",
                                    line_no=7,
                                ),
                            ],
                            arg_msg='assert in schema')
    , file=sys.stdout
)

