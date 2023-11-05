#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 * Return: 1 if the list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
listint_t *current = *head;
int arr[10000]; /* Assuming a limit on the number of elements */
int len = 0;

while (current != NULL)
{
	arr[len++] = current->n;
	current = current->next;
}

for (int i = 0, j = len - 1; i < j; i++, j--)
{
	if (arr[i] != arr[j])
	{
		return (0);
	}
}
return (1);
}

