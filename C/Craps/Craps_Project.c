
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>

int rolling(int *a, int *b); //return sum and address parse the values to the calling function
int playing(double status[5], char *type); //will call the rolling function
void ending(double status[5]); //save bank roll and status info into a file. 
void beginning(double nums[5]);
void animation(); //dice rolling animation
int input_output(); //asks for any input to start rolling and then show dice rolled.
void welcome(); // Fancy intro welcome screen


int main() {

	double status[5] = {100,0,0,0,0};	
	int a, b, x = 1, delay = 1;
	char type[50]; //Have to make buffer long enough to prevent the program from getting stuck. BUG 1. SECURITY!!!

	welcome();
	usleep(delay * 1200000);


	while(x == 1) {

		beginning(status);
		
		//BUG 1
		printf("\nWould you like to bet for or against? [Type 'for' or 'against' or 'quit']: ");
		scanf(" %s", type);
		
		if((strcmp(type, "for") == 0) || (strcmp(type, "against") == 0)) {
			playing(status, type);
			ending(status);
		} else if (strcmp(type, "quit") == 0) {
			x = 0;
		} else {
			printf("\nPlease enter a valid input!\n");
			usleep(delay * 2000000);
		}
	}
  return 0;
}

int playing(double status[5], char type[]) {
	float bet;
	int number, i = 1, tmp_num, delay = 1, a;
	char yn[50];
				
	// BUG 2 NO FIX
	printf("\nHow much would you like to bet? [You must bet at least 5 dollars] $");
	scanf(" %f", &bet);
	
	if(status[0] < bet) {
		printf("\nThat is not possible you do not have enough money. \n");
		printf("Please enter more money to play.\n\n");
		usleep(1200000);
		return -1;
	} else if(bet < 5.00) {
		//BUG 2
		while(bet < 5.00) {
			printf("\nNot a valid input. How much would you like to bet? $");
			scanf(" %f", &bet);
			}
	}
	
	// FOR
	if(strcmp(type, "for") == 0) {
		number = input_output();
		status[3]++;
		//CALCULATIONS
		if(number == 7 || number == 11){
			printf("$$$$$$$$$$$$\n");
			printf("$ YOU WIN! $ \\(ᵔᵕᵔ)/\n");
			printf("$$$$$$$$$$$$\n\n");
			status[0] += bet;
			status[1]++;
			usleep(delay * 2000000);
		} else if(number == 2 || number  == 3 || number == 12) {
			printf("!!!!!!!!!!!!\n");
			printf("! YOU LOSE ! ¯\\_( ツ)_/¯\n");
			printf("!!!!!!!!!!!!\n\n");
			status[0] -= bet;
			status[2]++;
			usleep(delay * 2000000);
		} else {
			
			tmp_num = number;
			printf("Players point! Would you like to double your bet? [Type 'y' or 'n'] ");
			scanf(" %s", yn);
			while((strcmp(yn, "y") != 0) && (strcmp(yn, "n") != 0)){
				printf("Unknown input. [Type 'y' or 'n'] ");
				scanf(" %s", yn);
			}

			if(strcmp(yn, "y") == 0){
				if ((bet * 2) > status[0]) {
					printf("\nYou cannot double your bet because you do not have enough money.");
					printf("\nThe game will continue without doubling the bet.\n\n");
					usleep(1200000);	
				} else {
				bet = bet * 2.0;
				}
			}

			number = 0;

			while((number != tmp_num) && (number != 7)){
				number = input_output();
			}

			if(number == tmp_num){
				printf("$$$$$$$$$$$$\n");
				printf("$ YOU WIN! $ \\(ᵔᵕᵔ)/\n");
				printf("$$$$$$$$$$$$\n\n");
				status[0] += bet;
				status[1]++;
				usleep(delay * 2000000);
			} else {
				printf("!!!!!!!!!!!!\n");
				printf("! YOU LOSE ! ¯\\_( ツ)_/¯\n");
				printf("!!!!!!!!!!!!\n\n");
				status[0] -= bet;
				status[2]++;
				usleep(delay * 2000000);
			}

		}

	//AGAINST
	} else {
		number = input_output();
		status[4]++;
		//CALCULATIONS
		if(number == 2 || number == 3 || number == 12){
			printf("$$$$$$$$$$$$\n");
			printf("$ YOU WIN! $ \\(ᵔᵕᵔ)/\n");
			printf("$$$$$$$$$$$$\n\n");
			status[0] += bet;
			status[1]++;
			usleep(delay * 2000000);
		} else if(number == 7 || number  == 11) {
			printf("!!!!!!!!!!!!\n");
			printf("! YOU LOSE ! ¯\\_( ツ)_/¯\n");
			printf("!!!!!!!!!!!!\n\n");
			status[0] -= bet;
			status[2]++;
			usleep(delay * 2000000);
		} else {
			tmp_num = number;
			printf("Players point! Would you like to double your bet? [Type 'y' or 'n'] ");
			scanf(" %s", yn);
			while((strcmp(yn, "y") != 0) && (strcmp(yn, "n") != 0)){
				printf("Unknown input. [Type 'y' or 'n'] ");
				scanf(" %s", yn);
			}

			if(strcmp(yn, "y") == 0){
				if ((bet * 2) > status[0]) {
					printf("\nYou cannot double your bet because you do not have enough money.");
					printf("\nThe game will continue without doubling the bet.\n\n");
					usleep(1200000);	
				} else {
				bet = bet * 2.0;
				}
			}
			
			number = 0;
			
			while((number != tmp_num) && (number != 7)){
				number = input_output();
			}

			if(number == tmp_num){
				printf("!!!!!!!!!!!!\n");
				printf("! YOU LOSE ! ¯\\_( ツ)_/¯\n");
				printf("!!!!!!!!!!!!\n\n");
				status[0] -= bet;
				status[2]++;
				usleep(delay * 2000000);
			} else {
				printf("$$$$$$$$$$$$\n");
				printf("$ YOU WIN! $ \\(ᵔᵕᵔ)/\n");
				printf("$$$$$$$$$$$$\n\n");
				status[0] += bet;
				status[1]++;
				usleep(delay * 2000000);
			}

		}
	}
	return 0;
}

int rolling(int *a, int *b) {
	// "Seed" the random number generator with the current time 
	srandom((unsigned int)(time(NULL)));
	*a = 1 + random() % 6;
	*b = 1 + random() % 6;
	return(*a + *b);
}

void animation() {
	int delay = 1, i;
	//animation of rolling dice
	for(i = 0; i < 7; i++) {
		if (i % 2 == 0) {
			printf(".      .\n");
			usleep(delay * 190000);
		} else {
			printf(" .      .\n");
			usleep(delay * 190000);
		}	
	}
}

int input_output() {
	char tmp[10];
	int a, b, number;
	char enter;

	fflush(stdin);
	printf("\nPress ENTER to roll! ");
	getchar();
	while (enter != '\r' && enter != '\n') { enter = getchar(); }

	animation();
		
	number = rolling(&a, &b);
	printf("\nDice 1 rolled -> %d  Dice 2 rolled -> %d\n\n", a, b);
	printf("Total number - > %d\n\n", number);
	return number;
}

void welcome() {
	printf("\nYb        dP 888888 88      dP\"\"b8  dP\"Yb  8b    d8 888888    888888  dP\"Yb      dP\"\"b8 88\"\"Yb    db    88\"\"Yb  .dP\"Y8 \n");
	printf(" Yb  db  dP  88__   88     dP   `\" dP   Yb 88b  d88 88__        88   dP   Yb    dP   `\" 88__dP   dPYb   88__dP  `Ybo \n");
	printf("  YbdPYbdP   88\"\"   88  .o Yb      Yb   dP 88YbdP88 88\"\"        88   Yb   dP    Yb      88\"Yb   dP__Yb  88\"\"\"  o.`Y8b \n");
	printf("   YP  YP    888888 88ood8  YboodP  YbodP  88 YY 88 888888      88    YbodP      YboodP 88  Yb dP\"\"\"\"Yb 88     8bodP' \n");
	printf("\nBy: Andrew Oliveau\n");
	//printf(" ");
}

void beginning(double status[5]) {
    int i = 0;
    FILE *fp;
 
    if (fp = fopen("stats.txt", "r")) {
        while (fscanf(fp, "%lf", &status[i]) != EOF) {
            i++;
        }
        fclose(fp);
    }

    printf("\n--------------------------------------------------------------------------------------------------------------------------");
	printf("\nBankroll: $%.2lf\n\n", status[0]);
	printf("STATS\n");
	printf("  ○ Games Won: 	      %.0lf\n", status[1]);
	printf("  ○ Games Lost:       %.0lf\n", status[2]);
	printf("  ○ Played For:       %.0lf\n", status[3]);
	printf("  ○ Played Against:   %.0lf\n", status[4]);
	printf("--------------------------------------------------------------------------------------------------------------------------\n");

	 
}

void ending(double status[5]) {
	int i;
    FILE *fp;
 	fp = fopen("stats.txt", "w");

 	for(i = 0; i < 5; i++) {
 		fprintf(fp, "%lf ", status[i]);
 	}
 	fclose(fp);
}
