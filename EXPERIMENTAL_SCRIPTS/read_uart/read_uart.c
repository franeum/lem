/* standard headers */
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/* mraa header */
#include "mraa/uart.h"

#define UART 1

volatile sig_atomic_t flag = 1;

void
sig_handler(int signum)
{
    if (signum == SIGINT) {
        fprintf(stdout, "Exiting...\n");
        flag = 0;
    }
}

int main(int argc, char** argv) {
    mraa_uart_context uart;
    char buffer[] = { 0, 0 };

    /* install signal handler */
    signal(SIGINT, sig_handler);

    /* initialize mraa for the platform (not needed most of the times) */
    mraa_init();

    //! [Interesting]
    /* initialize UART */
    uart = mraa_uart_init(UART);
    mraa_uart_set_baudrate(uart, 115200);

    if (uart == NULL) {
        fprintf(stderr, "Failed to initialize UART\n");
        goto err_exit;
    }



    while (flag) {
        if (mraa_uart_data_available(uart,0)) {
	    	mraa_uart_read(uart, buffer, sizeof(buffer));
        	printf("%d: %d\n", buffer[0], buffer[1]);
        	//sleep(1);
	
	}
    }

    /* stop UART */
    mraa_uart_stop(uart);

    //! [Interesting]
    /* deinitialize mraa for the platform (not needed most of the times) */
    mraa_deinit();

    return EXIT_SUCCESS;

err_exit:
    /* deinitialize mraa for the platform (not needed most of the times) */
    mraa_deinit();

    return EXIT_FAILURE;
}
