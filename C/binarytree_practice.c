
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	
	int val;
	struct node *left;
	struct node *right;
} node_t;

/*declartion of functions*/
void insert(node_t *next, int new_val);
void printDFS(node_t *search);

/*MAIN*/
int main() {
	
	node_t *list = malloc(sizeof(node_t));
	
	list->val = 5;
	list->right = NULL;
	list->left = NULL;
	
	insert(list, 6);
	insert(list, 3);
	insert(list, 10);
	insert(list, 2);
	
	printDFS(list);
}


void insert(node_t *next, int new_val) {
	
	int boolean = 1;
	node_t *current = next;
	
	if (new_val == 0)	current->val = new_val;
	else {

			while (boolean == 1) {
				if ((new_val > current->val) && (current->right != NULL)) {
					current = current->right;
				} else if ((new_val < current->val) && (current->left != NULL)) {
					current = current->left;
				}	
				else {
					if (new_val > current->val) {
						current->right = malloc(sizeof(node_t));
						current->right->val = new_val;
						current->right->right = NULL;
						current->right->left = NULL;
						boolean = 0;
					} else {
						current->left = malloc(sizeof(node_t));
						current->left->val = new_val;
						current->left->right = NULL;
						current->left->left = NULL;
						boolean = 0;
					}
				}
			}
		}
}
		
void printDFS(node_t *search) {
	
	if (search == NULL)			return;
	if (search->left != NULL)	printDFS(search->left);
	if (search != NULL)			printf("%d ", search->val);
	if (search->right != NULL) 	printDFS(search->right);
}
					
					
					
				
				
			
			
			
			

	
			
	
	
