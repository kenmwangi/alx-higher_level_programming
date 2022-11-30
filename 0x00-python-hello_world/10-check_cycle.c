#include <stdio.h>
#include "lists.h"

/**
 *   check_cycle - checks if a linked list contains a cycle
 *   @list: singly linked list
 *   Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tail;

	if (!list)
		return (0);

	head = list;
	tail = list;

	while (tail != NULL && tail->next != NULL)
	{
		head = head->next;
		tail= tail->next->next;

		if (head == tail)
			return (1);
	}
	return (0);

}
