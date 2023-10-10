#include <Python.h>
#include <stdlib.h>
#include <stdio.h>

/**
* print_python_list_info - Print basic information about a Python list.
* @p: PyObject pointer to the Python list.
*/
void print_python_list_info(PyObject *p) {
/* Declare variables to store list information */
Py_ssize_t size, allocated, i;
PyObject *item;

/* Get the size and allocated memory of the Python list */
size = PyList_Size(p);
allocated = ((PyListObject *)p)->allocated;

/* Print the size and allocated memory of the list */
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", allocated);

/* Iterate through the list elements and print their types */
for (i = 0; i < size; i++) {
item = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
}
}
