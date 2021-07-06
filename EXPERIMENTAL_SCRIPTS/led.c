/*
 * Author: Thomas Ingleby <thomas.c.ingleby@intel.com>
 * Contributors: Alex Tereschenko <alext.mkrs@gmail.com>
 * Contributors: Manivannan Sadhasivam <manivannan.sadhasivam@linaro.org>
 * Copyright (c) 2014 Intel Corporation.
 *
 * SPDX-License-Identifier: MIT
 *
 * Example usage: Toggles GPIO's 23 
 *
 */

/* standard headers */
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/* mraa header */
#include "mraa/gpio.h"

/* gpio declaration */
#define GPIO_PIN_1 22

volatile sig_atomic_t flag = 1;
int state = 0;

/* gestisce l'uscita */
void sig_handler(int signum)
{
    if (signum == SIGINT) {
        fprintf(stdout, "Exiting...\n");
        flag = 0;
    }
}

int main(void)
{
    mraa_result_t status = MRAA_SUCCESS;
    mraa_gpio_context gpio_1;

    /* install signal handler */
    signal(SIGINT, sig_handler);

    /* initialize mraa for the platform (not needed most of the times) */
    mraa_init();

    //! [Interesting]
    /* initialize GPIO pin */
    gpio_1 = mraa_gpio_init(GPIO_PIN_1);
    if (gpio_1 == NULL) {
        fprintf(stderr, "Failed to initialize GPIO %d\n", GPIO_PIN_1);
        mraa_deinit();
        return EXIT_FAILURE;
    }


    /* set GPIO to output */
    status = mraa_gpio_dir(gpio_1, MRAA_GPIO_OUT);
    if (status != MRAA_SUCCESS) {
        goto err_exit;
    }


    /* accende e spegne */
    while (flag) {
        // fprintf(stdout, "ciao");
	state = 1 - state;
        status = mraa_gpio_write(gpio_1, state);
	/*
        if (status != MRAA_SUCCESS) {
            goto err_exit;
        }
	*/


        usleep(50000);
    }

    /* release gpio's */
    status = mraa_gpio_close(gpio_1);
    if (status != MRAA_SUCCESS) {
        goto err_exit;
    }


    //! [Interesting]
    /* deinitialize mraa for the platform (not needed most of the times) */
    mraa_deinit();

    return EXIT_SUCCESS;

err_exit:
    mraa_result_print(status);

    /* deinitialize mraa for the platform (not needed most of the times) */
    mraa_deinit();

    return EXIT_FAILURE;
}
