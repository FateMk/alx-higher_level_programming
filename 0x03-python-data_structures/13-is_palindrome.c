#include "lists.h"
/**
 * is_palidrome - calls the pali_check function
 * @head: pointer to the linked list
 * Return: 0 if it not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (pali_check(head, *head));

}
/**
 * pali_check - to check if th list is palindrome
 * @head: beggining of the list
 * @last: end of the list
 * Return: 0 if not palindrome else 1
 */
int pali_check(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_pal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

