from dagstermill import define_dagstermill_op, local_output_notebook_io_manager
from dagster import (
    job,
    Out,
    In
)


op1 = define_dagstermill_op(
    name='nb_1',
    notebook_path="/app/nb_1.ipynb",
    output_notebook_name="out_nb_1",
    outs={
        'val': Out(str)
    },
    save_notebook_on_failure=True)


op2 = define_dagstermill_op(
    name='nb_2',
    notebook_path="/app/nb_2.ipynb",
    output_notebook_name="out_nb_2",
    ins={
        'val': In(str)
    },
    save_notebook_on_failure=True)


@job(
    resource_defs={
        "output_notebook_io_manager": local_output_notebook_io_manager,
    }
)
def pipeline():
    out_1, _ = op1()
    op2(out_1)
