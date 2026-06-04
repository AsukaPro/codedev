#include<stdio.h>
int main()
{
    int price = 0;
    scanf("%d",&price);
    printf("The price is: ");
    int change = 100 - price;
    int bush = change / 20;
    change = change % 20;
    int ten = change / 10;
    printf("\nThe change is: %d",change);
    return 0;
}