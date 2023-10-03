#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - check list
 * @list: list
 * Return: 1 or  0.
 */
int check_cycle(listint_t *list)
{
	listint_t *i1;
	listint_t *i2;

	i1 = list;
	i2 = list;
	if (list == NULL)
	{
		return (0);
	}
	i2 = i2->next;
	while (i2 != NULL && i2->next != NULL && i1 != NULL)
	{
		if (i1 == i2)
		{
			return (1);
		}
		i1 = i1->next;
		i2 = i2->next->next;
	}
	return (0);
}
