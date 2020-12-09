#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = *head;
	*head = new;
	return (*head);
}
