#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* reverse_list - Reverses a linked list in-place.
* @head: Pointer to pointer to the head of the list.
*/
void reverse_list(listint_t **head) {
listint_t *prev = NULL;
listint_t *current = *head;
listint_t *next = NULL;

while (current != NULL) {
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
}

/**
* is_palindrome - Checks if a linked list is a palindrome.
* @head: Pointer to pointer to the head of the list.
*
* Return: 1 if the list is a palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head) {
listint_t *slow_ptr = *head;
listint_t *fast_ptr = *head;
listint_t *second_half, *prev_of_slow_ptr = *head;
int is_palindrome = 1;

if (*head == NULL || (*head)->next == NULL) {
/* An empty list or a list with only one element is a palindrome. */
return 1;
}

/* Find the middle of the list using the two-pointer technique. */
while (fast_ptr != NULL && fast_ptr->next != NULL) {
fast_ptr = fast_ptr->next->next;
prev_of_slow_ptr = slow_ptr;
slow_ptr = slow_ptr->next;
}

if (fast_ptr != NULL) {
/* The list has an odd number of elements, so skip the middle element. */
slow_ptr = slow_ptr->next;
}

/* Reverse the second half of the list. */
second_half = slow_ptr;
reverse_list(&second_half);

/* Compare the first half and the reversed second half of the list. */
while (second_half != NULL) {
if ((*head)->n != second_half->n) {
is_palindrome = 0;
break;
}
*head = (*head)->next;
second_half = second_half->next;
}

/* Restore the original list. */
reverse_list(&slow_ptr);
prev_of_slow_ptr->next = slow_ptr;

return is_palindrome;
}
