#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer the head of the linked list
 * @number: The number inserted
 *
 * Return: If it fails, return  NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *node = *head, *new;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->num = number;

        if (node == NULL || node->num >= number)
        {
                new->next = node;
                *head = new;
                return (new);
        }

        while (node && node->next && node->next->num < number)
                node = node->next;

        new->next = node->next;
        node->next = new;

        return (new);
}
