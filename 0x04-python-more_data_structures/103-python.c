#include <Python.h>
#include <stdio.h>

/* Macro for printing error message */
/* Macro for printing error message */
#define PRINT_ERROR_MSG(obj_type) \
printf("[.] %s object info\n  [ERROR] Invalid %s Object\n", (#obj_type), (#obj_type))

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: Python object to be printed
 */
void print_python_bytes(PyObject *p)
{
PyBytesObject *bytes;
Py_ssize_t size, i;

/* Check if the object is a valid Python bytes object */
if (!PyBytes_Check(p))
{
	PRINT_ERROR_MSG(bytes);
	return;
}

bytes = (PyBytesObject *)p;
size = PyBytes_Size(p);

/* Print information about the Python bytes object */
printf("[.] bytes object info\n  size: %ld\n", size);
printf("  trying string: %s\n", bytes->ob_sval);
printf("  first 10 bytes: ");
for (i = 0; i < size && i < 10; i++)
{
	printf("%02x ", (unsigned char)bytes->ob_sval[i]);
}
printf("\n");
}

/**
 * print_python_list - Print information about Python lists
 * @p: Python object to be printed
 */
void print_python_list(PyObject *p)
{
PyListObject *list;
Py_ssize_t size, i;
PyObject *item;

/* Check if the object is a valid Python list */
if (!PyList_Check(p))
{
	PRINT_ERROR_MSG(list);
	return;
}
list = (PyListObject *)p;
size = PyList_Size(p);

/* Print information about the Python list */
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);

for (i = 0; i < size; i++)
{
	item = list->ob_item[i];
	printf("Element %ld: ", i);

	if (PyBytes_Check(item))
	{
		/* Recursively print Python bytes object */
		print_python_bytes(item);
	}
	else
	{
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
}

int main(void)
{
Py_Initialize();

/* Create Python bytes objects */
PyObject *s = PyBytes_FromString("Hello");
PyObject *b = PyBytes_FromString("\xff\xf8\x00\x00\x00\x00\x00\x00");

/* Print information about Python bytes objects */
print_python_bytes(s);
print_python_bytes(b);

/* Create a Python list and add Python bytes objects to it */
PyObject *l = PyList_New(2);
PyList_SetItem(l, 0, PyBytes_FromString("Hello"));
PyList_SetItem(l, 1, PyBytes_FromString("World"));

/* Print information about the Python list */
print_python_list(l);

Py_Finalize();

return (0);
}

