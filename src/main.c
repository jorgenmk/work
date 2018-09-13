#include <stdio.h>

int func1(int * int1, int int2)
{
	*int1 = int2;
	printf("func1 got %d\n", int2);
}

int main() {
	printf("STarting\n");
	int i = 24;
	int * j;

	func1(j, i);
}

