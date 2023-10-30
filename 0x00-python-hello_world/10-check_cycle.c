#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
listint_t *current, *temp;

if (list == NULL)
	return (0);

current = list;
temp = list->next;

while (temp != NULL && temp->next != NULL)
{
	if (current == temp)
		return (1);
	current = current->next;
	temp = temp->next->next;
}
return (0);
}

