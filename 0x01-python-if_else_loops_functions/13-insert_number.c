#include "lists.h"

/**
 * insert_node -
 * @head:
 * @number:
 * Return:
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *previous, *current;
	int check = 0;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;

	if (!head)
		return (NULL);

	if (!*head)
	{
		node->next = NULL;
		*head = node;
		return (node);
	}

	current = *head;
	while (current)
	{
		if (number > (current)->n && check == 0)
		{
			previous = current;
			current = (current)->next;
			if (!current)
			{
				node->next = NULL;
				previous->next = node;
				return (node);
			}
		}
		else if (number < (current)->n)
		{
			check = 1;
			current = previous;
		}
		else
		{
			node->next = (current)->next;
			previous->next = node;
			return (node);
		}
	}
	return (NULL);
}
