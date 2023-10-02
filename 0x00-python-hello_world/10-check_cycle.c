#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle
* @list: pointer to the head of the linked list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
listint_t *slow, *fast;
/*If fast becomes NULL, it means there is no cycle,&  the function returns 0*/
if (list == NULL || list->next == NULL)
return (0);

slow = list;
fast = list->next;

while (fast != NULL && fast->next != NULL)
{
/*slow==fast their *ers point to the same node, it means a cycle is detected*/
if (slow == fast)
return (1); /* Cycle detected */

slow = slow->next;
fast = fast->next->next;
}
/*If the loop exits without detecting a cycle, the function returns 0*/
return (0); /* No cycle detected */
}
