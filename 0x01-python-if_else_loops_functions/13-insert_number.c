#include "lists.h"

/**
 * insert_node - insert a node
 * @head: linked list
 * @number: number to add
 * Return: NULL or pointer to the node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *prev, *cur;

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

	if (number < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}

	cur = (*head)->next;
	prev = *head;

	while (cur && number > cur->n)
	{
		cur = cur->next;
		prev = prev->next;
	}

	prev->next = node;
	node->next = cur;

	return (node);
}
