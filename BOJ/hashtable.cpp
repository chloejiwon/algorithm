#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHAR 32
#define MAX_TABLE 1223
/* Implement Hash table containing string values in C */
/* Chaining strategy */

typedef struct _Hash
{
    char value[MAX_CHAR] = {
        0,
    };
    _Hash *next = NULL;
} Hash;

typedef struct _h
{
    int num = 0; // number of chained values
    Hash *values;
} hash;

hash hashtable[MAX_TABLE];
void init()
{
    for (int i = 0; i < MAX_TABLE; i++)
    {
        hashtable[i].num = 0;
        hashtable[i].values = NULL;
    }
}
int hash_key(const char *input)
{
    int res = 0;
    while (*input != '\0')
    {
        res += (int)(*input);
        input++;
    }
    return (res % MAX_TABLE);
}
void insert(char *input)
{
    int key = hash_key(input);
    printf("hash_key is %d\n", key);
    Hash *curr = hashtable[key].values;

    Hash *newnode = (Hash *)malloc(sizeof(Hash));
    int length = strlen(input);
    for (int i = 0; i < length; i++)
    {
        newnode->value[i] = input[i];
    }
    printf("newnode->value :%s\n", newnode->value);
    newnode->next = NULL;

    if (curr == NULL)
    {
        // first node
        printf("First Node\n");
        hashtable[key].values = newnode;
    }
    else
    {
        printf("not first one \n");
        newnode->next = curr;
        hashtable[key].values = newnode;
    }
}
int main()
{
    init();
    char input[MAX_CHAR] = {
        0,
    };
    printf("문자열을 입력하세요.:");
    scanf("%s", input);
    printf("입력받은 문자열:%s\n", input);
    insert(input);
    printf("문자열을 입력하세요.:");
    scanf("%s", input);
    printf("입력받은 문자열:%s\n", input);
    insert(input);
    /* print if the hash table is coreectly inserted */
    for (int i = 0; i < MAX_TABLE; i++)
    {
        Hash *curr = hashtable[i].values;
        while (curr)
        {
            printf("[%d] %s\n", i, curr->value);
            curr = curr->next;
        }
    }
    return 0;
}