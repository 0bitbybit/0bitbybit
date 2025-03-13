#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>  

#define CODE_LENGTH 4
#define MAX_DIGIT 8
#define MAX_ROUNDS 9

//declare program functions
void intro(int try_num);
int entry(int usr_code[]);
int wp_check(int usr_code[], int scrt_code[], int wp_array[]);
int mp_check(int usr_code[], int scrt_code[]);

void intro(int try_num) // Prints for each round 
{
    printf("Will you find the secret code?\n");
    printf("Please enter a valid guess\n");
    printf("---\n");
    printf("Round %d\n", try_num);
}



int entry(int usr_code[]) 
{
    
    while (1) 
    {  // Keep asking for input until valid
        char buffer[CODE_LENGTH + 1];
        ssize_t read_bytes = read(STDIN_FILENO, buffer, CODE_LENGTH);

        if (read_bytes == 0) // exits for Ctrl + D
        {       
            return 1;
            
        }
		
		
        if (read_bytes == -1) 
        {       
            printf("Read Error\n");
            continue;  // Ask for input again
        }

        if (read_bytes != CODE_LENGTH) 
        {
            printf("Enter exactly %d digits.\n", CODE_LENGTH);
            continue;  // Ask for input again
        }

        buffer[CODE_LENGTH] = '\0'; //avoids crashing

        bool valid_input = true;
        for (int i = 0; i < CODE_LENGTH; i++) 
        {
            if (buffer[i] < '0' || buffer[i] > '0' + MAX_DIGIT) 
            {
                printf("Invalid input. Please enter digits between 0 and %d.\n", MAX_DIGIT);
                valid_input = false;
                break;
            }
            usr_code[i] = buffer[i] - '0';
        }

        if (valid_input) 
        {
            // Consume any extra characters (like a newline)
            char extra;
            while (read(STDIN_FILENO, &extra, 1) > 0 && extra != '\n'); //read input
            return 0;  // Valid input received, exit the function return control to main()
        }
    }
}


// Checks for well-placed pieces
int wp_check(int usr_code[], int scrt_code[], int wp_array[]) 
{
    int wp = 0;
    for (int i = 0; i < CODE_LENGTH; i++) // Loops thru each digit of code
    {
        if (scrt_code[i] == usr_code[i]) // Check if match at each index element
        {
            wp_array[wp] = usr_code[i];     // Store a wp digit
            wp++;                         // Increment wp tally
        }
    }
    printf("Well placed pieces: %d\n", wp);
    return wp;
}

// Checks for misplaced pieces
int mp_check(int usr_code[], int scrt_code[]) 
{
  
    int mp = 0;
    bool used_usr[CODE_LENGTH] = {false};
    bool used_scrt[CODE_LENGTH] = {false};

    // Mark well-placed pieces as being already "used"
    for (int i = 0; i < CODE_LENGTH; i++) 
    {
        if (usr_code[i] == scrt_code[i]) 
        {
            used_usr[i] = true;
            used_scrt[i] = true;
        }
    }

    // Check for misplaced pieces
    for (int i = 0; i < CODE_LENGTH; i++) 
    {
        if (!used_usr[i]) 
        {
            for (int j = 0; j < CODE_LENGTH; j++) 
            {
                if (!used_scrt[j] && usr_code[i] == scrt_code[j]) 
                {
                    mp++;
                    used_usr[i] = true;
                    used_scrt[j] = true;
                    break;
                }
            }
        }
    }

    printf("Misplaced pieces: %d\n", mp);
    return mp;
}




int main(int argc, char *argv[]) // Command line input
{
    srand(time(NULL));  // Seed with elapsed seconds since Jan 1, 1970, unix epoch

     
    int scrt_code[CODE_LENGTH]; 
    int usr_code[CODE_LENGTH];
    int wp_list[CODE_LENGTH];
    //int wp_count;
     
    bool secret_code_set = false; // Check if scrt code is set
    
    // -t flag, the following sets number of rounds 
    int usr_rounds = 0;
    bool usr_rounds_set = false;
    for (int i = 2; i < argc; i++)
    {
    	if (strcmp(argv[i], "-t") == 0 && i + 1 < argc)  
       { // Check for -t flag
     
    		usr_rounds = atoi(argv[i + 1]); // convert string to integer
    		if (usr_rounds <= 0 || usr_rounds > MAX_ROUNDS)
    		{
    			printf("Round number must be between 1 and %d.\n", MAX_ROUNDS);
        		return 1; //entry error
        	}
        usr_rounds_set = true;  // Scrt code is set
        break;  // Exit the loop after handling the -c argument
    }
	}

    // -c flag sets secret code
    for (int i = 1; i < argc; i++) 
    { // Loop thru command line args
        if (strcmp(argv[i], "-c") == 0 && i + 1 < argc) 
        { // Check for -c flag
            char *code_str = argv[i + 1]; // Assign secret code string to char pointer
            if (strlen(code_str) != CODE_LENGTH) 
            { // Check secret code length is correct
                printf("Secret code must be %d digits.\n", CODE_LENGTH);
                return 1; //entry error
            }
            for (int j = 0; j < CODE_LENGTH; j++) 
            { // Loop thru each code digit
                int digit = code_str[j] - '0'; // Convert code digit to integer
                if (digit < 0 || digit > MAX_DIGIT) 
                {
                    printf("Secret code must be between 0 and %d.\n", MAX_DIGIT);
                    return 1;
                }
                scrt_code[j] = digit; // Store digit to scrt code array
            }
            secret_code_set = true;  // Scrt code is set
            break;  // Exit the loop after handling the -c argument
        }
    }

    // Random digit generator 
    if (!secret_code_set) 
    { 
        for (int i = 0; i < CODE_LENGTH; i++) 
        {
            scrt_code[i] = rand() % (MAX_DIGIT + 1); 
        }
    }
    
    
     //  Default to max allowed number of rounds
    if (!usr_rounds_set) 
    { 
        usr_rounds = MAX_ROUNDS;
    }
    


	// run for loop for each round 
    for (int round = 0; round < usr_rounds && round < MAX_ROUNDS; round++) 
    {
        intro(round); //prints game intro messages
        
        memset(usr_code, 0, sizeof(usr_code));   //resets user code guess to zeros each round
        
       
        // exits program when ctrl + D pressed
        if (entry(usr_code))
        	{
        		return 1;
        	}	


        // Check if usr guess is correct using a manual comparison instead of memcmp.
        bool is_correct_guess = true;
        for (int i = 0; i < CODE_LENGTH; i++) 
        {
            if (usr_code[i] != scrt_code[i]) 
            {
                is_correct_guess = false;
                break;
            }
        }

        if (is_correct_guess) {
            printf("Congratz! You did it!\n");
            return 0;
        }


		wp_check(usr_code, scrt_code, wp_list);
        //wp_count = wp_check(usr_code, scrt_code, wp_list);
        //mp_check(usr_code, scrt_code, wp_list, wp_count);
        mp_check(usr_code, scrt_code);
    }

    
    printf("Sorry, you've run out of attempts.\n");
    printf("The secret code was: ");
    
    for (int i = 0; i < CODE_LENGTH; i++) 
    {
        printf("%d", scrt_code[i]);
    }
    
    printf("\n");

    return 0;
}