#include "lists.h"
/**
 * is_palindrome - My function that checks palindrome
 * @head:list
 *Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
const listint_t *current;
int length;
int integer, j;
int arr[10000];
if (*head == NULL)
return (1);
current = *head;
length = 0;
while (current != NULL)
{
current = current->next;
length++;
}
if (length == 1)
return (1);
current = *head;
integer = 0;
while (current != NULL)
{
arr[integer] = current->n;
integer++;
current = current->next;
}
j = 0;
integer--;
length--;
while (integer >= (length / 2))
{
if (arr[integer] != arr[j])
return (0);
integer--;
j++;
}
return (1);
}
