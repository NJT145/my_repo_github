#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

/**
 * this code build after some modifications on code in links:
 *   https://github.com/cfperea/multithreaded-sudoku/blob/master/main.c
 *   https://docs.oracle.com/cd/E19455-01/806-5257/sync-12/index.html
 */

int board[9][9] = {

            {6, 2, 4, 5, 3, 9, 1, 8, 7},

            {5, 1, 9, 7, 2, 8, 6, 3, 4},

            {8, 3, 7, 6, 1, 4, 2, 9, 5},

            {1, 4, 3, 8, 6, 5, 7, 2, 9},

            {9, 5, 8, 2, 4, 7, 3, 6, 1},

            {7, 6, 2, 3, 9, 1, 4, 5, 8},

            {3, 7, 1, 9, 5, 6, 8, 4, 2},

            {4, 9, 6, 1, 8, 2, 5, 7, 3},

            {2, 8, 5, 4, 7, 3, 9, 1, 6}

        };

int main()
{
    SudokuSolutionValidator(board);

    return 0;
}

typedef struct
{
    int row; // The starting row.
    int col; // The starting column.
    int (* board)[9]; // The pointer to the board.
} parameters;

typedef struct
{
    parameters (* param);
    int (* num);
}argss;

// Prototypes for functions...
void * check_row(void * param_args);
void * check_col(void * param_args);
void * check_square(void * params);

// count for end threads...
int count;
// and lock for that count...
pthread_mutex_t count_mutex;

// ====== Create the return values for the threads ======
int check_result;
check_result = 1;

int get_count()
{
    int c;
    pthread_mutex_lock(&count_mutex); // acquire
    c = count;
    pthread_mutex_unlock(&count_mutex); // release
    return (c);
}

void increment_count()
{
    pthread_mutex_lock(&count_mutex);
    count = count + 1;
    pthread_mutex_unlock(&count_mutex);
}

int SudokuSolutionValidator(int board[9][9])
{
    // ====== Create the parameter for the columns and rows check =======
    parameters * param0 = (parameters *) malloc(sizeof(parameters));
    param0->row = 0;
    param0->col = 0;
    param0->board = board;

    // row_args...
    argss * row_arg1 = (argss *) malloc(sizeof(argss)); row_arg1->param = param0; row_arg1->num = 0;
    argss * row_arg2 = (argss *) malloc(sizeof(argss)); row_arg2->param = param0; row_arg2->num = 1;
    argss * row_arg3 = (argss *) malloc(sizeof(argss)); row_arg3->param = param0; row_arg3->num = 2;
    argss * row_arg4 = (argss *) malloc(sizeof(argss)); row_arg4->param = param0; row_arg4->num = 3;
    argss * row_arg5 = (argss *) malloc(sizeof(argss)); row_arg5->param = param0; row_arg5->num = 4;
    argss * row_arg6 = (argss *) malloc(sizeof(argss)); row_arg6->param = param0; row_arg6->num = 5;
    argss * row_arg7 = (argss *) malloc(sizeof(argss)); row_arg7->param = param0; row_arg7->num = 6;
    argss * row_arg8 = (argss *) malloc(sizeof(argss)); row_arg8->param = param0; row_arg8->num = 7;
    argss * row_arg9 = (argss *) malloc(sizeof(argss)); row_arg9->param = param0; row_arg9->num = 8;

    // col_args...
    argss * col_arg1 = (argss *) malloc(sizeof(argss)); col_arg1->param = param0; col_arg1->num = 0;
    argss * col_arg2 = (argss *) malloc(sizeof(argss)); col_arg2->param = param0; col_arg2->num = 1;
    argss * col_arg3 = (argss *) malloc(sizeof(argss)); col_arg3->param = param0; col_arg3->num = 2;
    argss * col_arg4 = (argss *) malloc(sizeof(argss)); col_arg4->param = param0; col_arg4->num = 3;
    argss * col_arg5 = (argss *) malloc(sizeof(argss)); col_arg5->param = param0; col_arg5->num = 4;
    argss * col_arg6 = (argss *) malloc(sizeof(argss)); col_arg6->param = param0; col_arg6->num = 5;
    argss * col_arg7 = (argss *) malloc(sizeof(argss)); col_arg7->param = param0; col_arg7->num = 6;
    argss * col_arg8 = (argss *) malloc(sizeof(argss)); col_arg8->param = param0; col_arg8->num = 7;
    argss * col_arg9 = (argss *) malloc(sizeof(argss)); col_arg9->param = param0; col_arg9->num = 8;

    // ====== Create the parameters for the 3x3 threads ======

    // First 3x3
    parameters * param1 = (parameters *) malloc(sizeof(parameters));
    param1->row = 0;
    param1->col = 0;
    param1->board = board;

    // Second 3x3
    parameters * param2 = (parameters *) malloc(sizeof(parameters));
    param2->row = 0;
    param2->col = 3;
    param2->board = board;

    // Third 3x3
    parameters * param3 = (parameters *) malloc(sizeof(parameters));
    param3->row = 0;
    param3->col = 6;
    param3->board = board;

    // Fourth 3x3
    parameters * param4 = (parameters *) malloc(sizeof(parameters));
    param4->row = 3;
    param4->col = 0;
    param4->board = board;

    // Fifth 3x3
    parameters * param5 = (parameters *) malloc(sizeof(parameters));
    param5->row = 3;
    param5->col = 3;
    param5->board = board;

    // Sixth 3x3
    parameters * param6 = (parameters *) malloc(sizeof(parameters));
    param6->row = 3;
    param6->col = 6;
    param6->board = board;

    // Seventh 3x3
    parameters * param7 = (parameters *) malloc(sizeof(parameters));
    param7->row = 6;
    param7->col = 0;
    param7->board = board;

    // Eighth 3x3
    parameters * param8 = (parameters *) malloc(sizeof(parameters));
    param8->row = 6;
    param8->col = 3;
    param8->board = board;

    // Ninth 3x3
    parameters * param9 = (parameters *) malloc(sizeof(parameters));
    param9->row = 6;
    param9->col = 6;
    param9->board = board;

    // ====== Create the threads ======
    pthread_t thread_row1, thread_row2, thread_row3, thread_row4, thread_row5, thread_row6, thread_row7, thread_row8, thread_row9;
    pthread_t thread_col1, thread_col2, thread_col3, thread_col4, thread_col5, thread_col6, thread_col7, thread_col8, thread_col9;
    pthread_t thread1, thread2, thread3, thread4, thread5, thread6, thread7, thread8, thread9;

    // ====== Initialize the threads ======
    // rows...
    pthread_create(&thread_row1, NULL, check_row, (void *) row_arg1);
    pthread_create(&thread_row2, NULL, check_row, (void *) row_arg2);
    pthread_create(&thread_row3, NULL, check_row, (void *) row_arg3);
    pthread_create(&thread_row4, NULL, check_row, (void *) row_arg4);
    pthread_create(&thread_row5, NULL, check_row, (void *) row_arg5);
    pthread_create(&thread_row6, NULL, check_row, (void *) row_arg6);
    pthread_create(&thread_row7, NULL, check_row, (void *) row_arg7);
    pthread_create(&thread_row8, NULL, check_row, (void *) row_arg8);
    pthread_create(&thread_row9, NULL, check_row, (void *) row_arg9);
    // columns...
    pthread_create(&thread_col1, NULL, check_col, (void *) col_arg1);
    pthread_create(&thread_col2, NULL, check_col, (void *) col_arg2);
    pthread_create(&thread_col3, NULL, check_col, (void *) col_arg3);
    pthread_create(&thread_col4, NULL, check_col, (void *) col_arg4);
    pthread_create(&thread_col5, NULL, check_col, (void *) col_arg5);
    pthread_create(&thread_col6, NULL, check_col, (void *) col_arg6);
    pthread_create(&thread_col7, NULL, check_col, (void *) col_arg7);
    pthread_create(&thread_col8, NULL, check_col, (void *) col_arg8);
    pthread_create(&thread_col9, NULL, check_col, (void *) col_arg9);
    // 3x3 squares...
    pthread_create(&thread1, NULL, check_square, (void *) param1);
    pthread_create(&thread2, NULL, check_square, (void *) param2);
    pthread_create(&thread3, NULL, check_square, (void *) param3);
    pthread_create(&thread4, NULL, check_square, (void *) param4);
    pthread_create(&thread5, NULL, check_square, (void *) param5);
    pthread_create(&thread6, NULL, check_square, (void *) param6);
    pthread_create(&thread7, NULL, check_square, (void *) param7);
    pthread_create(&thread8, NULL, check_square, (void *) param8);
    pthread_create(&thread9, NULL, check_square, (void *) param9);



    // ====== Check whether the Sudoku Puzzle was solved ======
    while (1) // wait for end of all threads
    {
        if (get_count()==27) {break;}
    }
    if ((int) check_result==1) // if all OK
    {
        printf("The Sudoku Puzzle is solved!\n");
    }

    else {
        printf("The Sudoku Puzzle is NOT solved.\n");
    }

    return 0;
}

/**
 * Checks row if it contains all digits 1-9.
 * @param   void *      The argss (pointer).
 * @return  void *      1 if row contains all digits from 1-9, 0 otherwise.
 */
void * check_row(void * param_args) {
    argss * arguments = (parameters *) param_args;
    parameters * data = (parameters *) arguments->param;
    int startRow = arguments->num;
    int startCol = data->col;
    int row[10] = {0};
        for (int j = startCol; j < 9; ++j) {
            int val = data->board[startRow][j];
            if (row[val] != 0) {
                check_result = 0;
                increment_count();
                return (void *) 0;
            }
            else{
                row[val] = 1;
            }
        }
    increment_count();
    return (void *) 1;
}

/**
 * Checks column if it contains all digits 1-9.
 * @param   void *      The argss (pointer).
 * @return  void *      1 if column contains all digits from 1-9, 0 otherwise.
 */
void * check_col(void * param_args) {

    argss * arguments = (parameters *) param_args;
    parameters * data = (parameters *) arguments->param;
    int startRow = data->row;
    int startCol = arguments->num;
    int col[10] = {0};
        for (int j = startRow; j < 9; ++j) {
            int val = data->board[j][startCol];
            if (col[val] != 0) {
                check_result = 0;
                increment_count();
                return (void *) 0;
            }
            else{
                col[val] = 1;
            }
        }
    increment_count();
    return (void *) 1;
}


/**
 * Checks if a square of size 3x3 contains all numbers from 1-9.
 * @param   void *      The parameters (pointer).
 * @return  void *      1 if all rows contain all digits from 1-9, 0 otherwise.
 */
void * check_square(void * params) {
    parameters * data = (parameters *) params;
    int startRow = data->row;
    int startCol = data->col;
    int saved[10] = {0};
    for (int i = startRow; i < startRow + 3; ++i) {
        for (int j = startCol; j < startCol + 3; ++j) {
            int val = data->board[i][j];
            if (saved[val] != 0) {
                check_result = 0;
                increment_count();
                return (void *) 0;
            }
            else{
                saved[val] = 1;
            }
        }
    }
    increment_count();
    return (void *) 1;
}
