#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: PyObject pointer to a Python list.
 */
void print_python_list_info(PyObject *p)
{
PyListObject *list = (PyListObject *)p;
Py_ssize_t size;

size = PyList_GET_SIZE(p);
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);

for (Py_ssize_t i = 0; i < size; i++)
{
	PyObject *item = PyList_GET_ITEM(p, i);

	printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
}
}

