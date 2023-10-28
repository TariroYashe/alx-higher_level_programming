#include <Python.h>
#include <stdio.h>

/**
* print_python_list - Print information about a Python list
* @p: PyObject representing the list
*/
void print_python_list(PyObject *p)
{
if (!PyList_Check(p))
{
printf("[ERROR] Invalid List Object\n");
return;
}

Py_ssize_t size = ((PyVarObject *)p)->ob_size;
Py_ssize_t allocated = ((PyListObject *)p)->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);

for (Py_ssize_t i = 0; i < size; i++)
{
PyObject *element = ((PyListObject *)p)->ob_item[i];
printf("Element %ld: %s\n", i, element->ob_type->tp_name);
}
}

/**
* print_python_bytes - Print information about a Python bytes object
* @p: PyObject representing the bytes object
*/
void print_python_bytes(PyObject *p)
{
if (!PyBytes_Check(p))
{
printf("[ERROR] Invalid Bytes Object\n");
return;
}

Py_ssize_t size = ((PyVarObject *)p)->ob_size;
char *data = ((PyBytesObject *)p)->ob_sval;

printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n");

printf("  first 10 bytes: ");
for (int i = 0; i < 10 && i < size; i++)
{
printf("%02x ", data[i] & 0xFF);
}
printf("\n");
}

/**
* print_python_float - Print information about a Python float object
* @p: PyObject representing the float object
*/
void print_python_float(PyObject *p)
{
if (!PyFloat_Check(p))
{
printf("[ERROR] Invalid Float Object\n");
return;
}

double value = ((PyFloatObject *)p)->ob_fval;

printf("[.] float object info\n");
printf("  value: %f\n", value);
}
