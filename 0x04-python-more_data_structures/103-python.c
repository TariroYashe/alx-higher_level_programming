#include <Python.h>
#include <stdio.h>

/**
* print_python_bytes - Print information about a Python bytes object
* @p: A pointer to the Python bytes object
*/
void print_python_bytes(PyObject *p)
{
if (PyBytes_Check(p))
{
Py_ssize_t size = PyBytes_GET_SIZE(p);
char *str = PyBytes_AsString(p);
int i;
printf("[.] bytes object info\n");
printf("  size: %ld\n", size);
printf("  trying string: %s\n");
printf("  first 10 bytes: ");
for (i = 0; i < size && i < 10; i++)
{
printf("%02x ", (unsigned char)str[i]);
}
printf("\n");
}
else
{
printf("[ERROR] Invalid Bytes Object\n");
}
}

/**
* print_python_list - Print information about a Python list object
* @p: A pointer to the Python list object
*/
void print_python_list(PyObject *p)
{
int i;
if (PyList_Check(p))
{
int size = (int)PyList_Size(p);
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
for (i = 0; i < size; i++)
{
PyObject *element = PyList_GetItem(p, i);
printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
if (PyBytes_Check(element))
{
print_python_bytes(element);
}
else
{
if (PyUnicode_Check(element))
{
Py_ssize_t len;
char *str;
PyUnicode_AsUTF8AndSize(element, &str, &len);
printf("[.] string info\n");
printf("  length: %ld\n", len);
printf("  string: %s\n", str);
}
}
}
}
else
{
printf("[ERROR] Invalid Bytes Object\n");
}
}
