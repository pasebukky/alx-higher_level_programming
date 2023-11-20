#include <Python.h>

/* Function prototypes */
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);



/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
        Py_ssize_t size, alloc, i;
        const char *type;
        PyListObject *list = (PyListObject *)p;
        PyVarObject *var = (PyVarObject *)p;

        size = var->ob_size;
        alloc = list->allocated;

        fflush(stdout);

        printf("[*] Python list info\n");
        if (strcmp(p->ob_type->tp_name, "list") != 0)
        {
                printf("  [ERROR] Invalid List Object\n");
                return;
        }

        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", alloc);

        for (i = 0; i < size; i++)
        {
                type = list->ob_item[i]->ob_type->tp_name;
                printf("Element %ld: %s\n", i, type);
                if (strcmp(type, "bytes") == 0)
                        print_python_bytes(list->ob_item[i]);
                else if (strcmp(type, "float") == 0)
                        print_python_float(list->ob_item[i]);
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
}

printf("[.] bytes object info\n");
printf("  size: %ld\n", PyBytes_Size(p));

if (PyBytes_Size(p) > 10)
	printf("  trying string: %.*s...\n", 10, PyBytes_AsString(p));
else
	printf("  trying string: %.*s\n", 10, PyBytes_AsString(p));

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
}

printf("[.] float object info\n");
printf("  value: %f\n", PyFloat_AsDouble(p));
}
