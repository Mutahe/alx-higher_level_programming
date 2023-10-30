#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @listint_t: singly linked list
 * @list: points to next
 *
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *now, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	now = list;
	check = now->next;

	while (now != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (now == check)
			return (1);
		now = now->next;
		check = check->next->next;
	}
	return (0);
}
