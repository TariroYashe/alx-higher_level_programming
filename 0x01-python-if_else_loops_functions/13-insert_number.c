#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: pointer to pointer of first node of listint_t list
* @number: integer to be inserted
* Return: the address of the new node, or NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node, *current, *prev;

/*Allocate memory for the new node*/
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
return (NULL);

/*Initialize the new node with the provided number*/
new_node->n = number;
new_node->next = NULL;

/*Initialize current and prev pointers*/
current = *head;
prev = NULL;

/*Traverse the list to find the correct position to insert the new node*/
while (current != NULL && current->n < number)
{
prev = current;
current = current->next;
}

/*Insert the new node into the list at the correct position*/
if (prev == NULL)
{
/*If the new node should be inserted at the beginning*/
new_node->next = *head;
*head = new_node;
}
else
{
/*If the new node should be inserted in the middle or at the end*/
prev->next = new_node;
new_node->next = current;
}

/* Return the address of the new node*/
return (new_node);
}

