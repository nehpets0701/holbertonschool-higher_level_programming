#include "lists.h"

/**
 *check_cycle-cycle?
 *@list:input
 *Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (list == NULL)
		return (0);
	first = list;
	second = list->next;

	while (second != NULL)
	{
		if (first == second)
			return (1);
		second = second->next;
		if (first == second)
			return (1);
		if (second == NULL)
			break;
		second = second->next;
		first = first->next;
	}
	return (0);
}
