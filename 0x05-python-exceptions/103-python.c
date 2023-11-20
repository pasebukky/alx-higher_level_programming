#include <Python.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < PyList_Size(p); ++i)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
        {
            printf("[.] bytes object info\n");
            printf("  size: %ld\n", PyBytes_Size(item));

            if (PyBytes_Size(item) > 10)
                printf("  trying string: %.*s...\n", 10, PyBytes_AsString(item));
            else
                printf("  trying string: %.*s\n", (int)PyBytes_Size(item), PyBytes_AsString(item));

            printf("  first 10 bytes: ");
            for (int j = 0; j < 10 && j < PyBytes_Size(item); ++j)
                printf("%02x ", (unsigned char)PyBytes_AsString(item)[j]);
            printf("\n");
        }
    }
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t i;

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));

    if (PyBytes_Size(p) > 10)
        printf("  trying string: %.*s...\n", 10, PyBytes_AsString(p));
    else
        printf("  trying string: %.*s\n", (int)PyBytes_Size(p), PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (i = 0; i < 10 && i < PyBytes_Size(p); ++i)
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: Pointer to a Python object
 */
void print_python_float(PyObject *p)
{
    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");
    printf("  value: %f\n", PyFloat_AsDouble(p));
}

