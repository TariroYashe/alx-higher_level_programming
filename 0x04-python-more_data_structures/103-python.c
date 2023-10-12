#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - Prints bytes information
*
* @p: Python Object
*
* Description:
* This function prints information about Python bytes objects.
*
* @p: A pointer to the Python object (bytes).
*/
void print_python_bytes(PyObject *p)
{
char *string;
long int size, i, limit;

printf("[.] bytes object info\n");

/*Check if the object is a valid bytes object*/
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = ((PyVarObject *)(p))->ob_size;
string = ((PyBytesObject *)p)->ob_sval;

/* Print the size of the bytes object*/
printf("  size: %ld\n", size);
printf("  trying string: %s\n", string);

if (size >= 10)
limit = 10;
else
limit = size + 1;

/*Print the first 10 bytes (or less) in hexadecimal format*/
printf("  first %ld bytes:", limit);

for (i = 0; i < limit; i++)
{
if (string[i] >= 0)
printf(" %02x", string[i]);
else
printf(" %02x", 256 + string[i]);
}

printf("\n");
}

/**
* print_python_list - Prints list information
*
* @p: Python Object
*
* Description:
* This function prints information about Python list objects.
*
* @p: A pointer to the Python object (list).
*/
void print_python_list(PyObject *p)
{
long int size, i;
PyListObject *list;
PyObject *obj;

size = ((PyVarObject *)(p))->ob_size;
list = (PyListObject *)p;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);

for (i = 0; i < size; i++)
{
obj = ((PyListObject *)p)->ob_item[i];

/*Print the type of the element*/
printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);

/*If the element is a bytes object, call print_python_bytes*/
if (PyBytes_Check(obj))
print_python_bytes(obj);
}
}

