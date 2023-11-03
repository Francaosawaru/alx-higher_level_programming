#include <Python.h>

/**
 * print_python_list_info -  function that prints some basic
 * info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, allocated, elem;
    PyObject *item;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (elem = 0; elem < size; elem++)
    {
        item = PyList_GetItem(p, elem);
        printf("Element %ld: %s\n", elem, item->ob_type->tp_name);
    }
}
