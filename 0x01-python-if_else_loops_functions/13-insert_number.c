#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to a pointer to a singly linked list
 * @number: New node value.
 *
 * Return: The address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	while (*head && (*head)->n < number)
		head = &((*head)->next);

	new_node->next = *head;
	*head = new_node;
	return (new_node);
}
