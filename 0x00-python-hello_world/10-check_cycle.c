#include "lists.h"

/**
 * check_cycle - Function
 * @list: List
 * bf: Variable
 * af: Variable
 * Return: 0
 */

int check_cycle(listint_t *list)
{
	listint_t *bf = list;
	listint_t *af = list;

	while (af && af->next)
	{
		bf = bf->next;
		af = af->next->next;
		if(bf == af)
		{
			return (1);
		}
	}
	return (0);
}
