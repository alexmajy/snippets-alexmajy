#include <stdio.h>

int m_state = 0;

void
foo(void)
{
    m_state += 10;
}

int main (int argc, char const* argv[])
{
    m_state = 1;
    foo();
    printf("m_state: %d\n", m_state);
    return 0;
}

