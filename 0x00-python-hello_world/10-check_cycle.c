#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a linked list has a cycle in it or not
 * @list: pointer of type listint_t
 * Return:0 if no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;
	
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}
	return (0);
}
