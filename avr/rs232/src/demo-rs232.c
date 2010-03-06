#include <stdio.h>

#include "rs232.h"

void
init_usart(void)
{
  /* First rs232 port for debugging */
  rs232_init(RS232_PORT_0, USART_BAUD_115200,
             USART_PARITY_NONE | USART_STOP_BITS_1 | USART_DATA_BITS_8);

  /* Redirect stdout to first port */
  rs232_redirect_stdout(RS232_PORT_0);

}

int
main(void)
{

  init_usart();

  sei();

  printf("hello,world\n");
  
  return 0;
}
