#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @left: pointer to a node
 * @right: pointer to another node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int check_palindrome(listint_t **left, listint_t *right)
{
	int pal;

	if (!right)
		return (1);

	pal = check_palindrome(left, right->next);

	if (pal == 0)
		return (0);

	if ((*left)->n != right->n)
		return (0);

	*left = (*left)->next;

	return (pal);
}

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	return (check_palindrome(head, *head));
}
