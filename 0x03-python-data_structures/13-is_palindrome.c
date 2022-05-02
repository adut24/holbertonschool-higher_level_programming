#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr1 = *head, *ptr2 = *head;
	int i, j, nb_nodes = 0;

	if (!head)
		return (1);

	if (!*head)
		return (1);

	for (i = 0; ptr2->next != NULL; i++, nb_nodes++)
		ptr2 = ptr2->next;

	if (ptr1->n != ptr2->n)
		return (0);

	for (i = 0; ptr1->next != ptr2->next; i++)
	{
		ptr2 = *head;
		for (j = 0; j != nb_nodes; j++)
			ptr2 = ptr2->next;
		if (ptr1->n != ptr2->n)
			return (0);
		ptr1 = ptr1->next;
		nb_nodes--;
	}
	return (1);
}
